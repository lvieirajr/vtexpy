from http import HTTPStatus
from json import JSONDecodeError
from logging import WARNING
from typing import Any, Union, Type, cast
from urllib.parse import urljoin

from httpx import (
    Client,
    CookieConflict,
    Headers,
    HTTPError,
    InvalidURL,
    Response,
    StreamError,
)
from httpx._types import(
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestFiles,
)
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from .._config import Config
from .._constants import APP_KEY_HEADER, APP_TOKEN_HEADER
from .._dto import VTEXResponse, VTEXResponseType
from .._exceptions import VTEXRequestError, VTEXResponseError
from .._logging import get_logger
from .._types import HTTPMethodType
from .._utils import redact_headers


class BaseAPI:
    """
    Base client for VTEX API.
    """

    def __init__(self, config: Union[Config, None] = None) -> None:
        self._config = config or Config()
        self._logger = get_logger(type(self).__name__)

    def _request(
        self,
        method: HTTPMethodType,
        environment: str,
        endpoint: str,
        headers: Union[HeaderTypes, None] = None,
        cookies: Union[CookieTypes, None] = None,
        params: Union[QueryParamTypes, None] = None,
        json: Union[Any, None] = None,
        data: Union[RequestData, None] = None,
        content: Union[RequestContent, None] = None,
        files: Union[RequestFiles, None] = None,
        config: Union[Config, None] = None,
        response_class: Union[Type[VTEXResponseType], None] = None,
    ) -> VTEXResponseType:
        request_config = self._get_config(config=config)
        url = self._get_url(
            config=request_config,
            environment=environment,
            endpoint=endpoint,
        )
        headers = self._get_headers(config=request_config, headers=headers)

        @retry(
            stop=stop_after_attempt(
                max_attempt_number=request_config.get_retries() + 1,
            ),
            wait=wait_exponential(multiplier=1, max=64, exp_base=2, min=1),
            retry=retry_if_exception_type(
                exception_types=(HTTPError, InvalidURL, CookieConflict, StreamError),
            ),
            before_sleep=before_sleep_log(
                logger=self._logger,
                log_level=WARNING,
                exc_info=True,
            ),
            reraise=True,
        )
        def _send_request() -> Response:
            with Client(timeout=request_config.get_timeout()) as client:
                return client.request(
                    method.upper(),
                    url,
                    headers=headers,
                    cookies=cookies,
                    params=params,
                    json=json,
                    data=data,
                    content=content,
                    files=files,
                )

        try:
            response = _send_request()
        except (HTTPError, InvalidURL, CookieConflict, StreamError) as exception:
            headers = redact_headers(dict(headers))

            details = {
                "exception": exception,
                "method": str(method).upper(),
                "url": str(url),
                "headers": headers,
            }

            self._logger.error(str(exception), extra=details, exc_info=True)

            raise VTEXRequestError(**details) from None  # type: ignore[arg-type]
        else:
            response.headers = Headers(redact_headers(dict(response.headers)))
            response.request.headers = headers = Headers(redact_headers(dict(headers)))

            self._raise_from_response(response=response, config=request_config)

            return cast(
                VTEXResponseType,
                (response_class or VTEXResponse).factory(response),
            )

    def _get_config(self, config: Union[Config, None]) -> Config:
        return config or self._config

    def _get_url(self, config: Config, environment: str, endpoint: str) -> str:
        return urljoin(
            f"https://{config.get_account_name()}.{environment}.com.br",
            endpoint,
        )

    def _get_headers(
        self,
        config: Config,
        headers: Union[HeaderTypes, None] = None,
    ) -> Headers:
        request_headers = Headers(headers=headers)

        request_headers[APP_KEY_HEADER] = config.get_app_key()
        request_headers[APP_TOKEN_HEADER] = config.get_app_token()

        request_headers["Content-Type"] = "application/json; charset=utf-8"
        request_headers["Accept"] = "application/json"

        return request_headers

    def _raise_from_response(self, response: Response, config: Config) -> None:
        if response.is_error and config.get_raise_for_status():
            try:
                data = response.json(strict=False)
            except JSONDecodeError:
                data = response.text or HTTPStatus(response.status_code).phrase

            details = {
                "method": str(response.request.method).upper(),
                "url": str(response.request.url),
                "request_headers": response.request.headers,
                "status": response.status_code,
                "data": data,
                "response_headers": response.headers,
            }

            if response.is_server_error:
                self._logger.error(data, extra=details)
            else:
                self._logger.warning(data, extra=details)

            raise VTEXResponseError(data, **details) from None
