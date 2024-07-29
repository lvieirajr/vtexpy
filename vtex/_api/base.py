from logging import INFO, getLogger
from typing import Any, Union
from urllib.parse import urljoin

from httpx import (
    Client,
    CookieConflict,
    Headers,
    HTTPError,
    HTTPStatusError,
    InvalidURL,
    Response,
    StreamError,
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
from .._exceptions import RequestError, VTEXError
from .._response import VTEXResponse
from .._types import (
    CookieTypes,
    HeaderTypes,
    HttpMethodTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestFiles,
)
from .._utils import string_to_snake_case


class BaseAPI:
    """
    Base client for VTEX API.
    """

    def __init__(self, config: Union[Config, None] = None) -> None:
        self._config = config or Config()
        self._logger = getLogger(f"vtex.{string_to_snake_case(type(self).__name__)}")

    def _request(
        self,
        method: HttpMethodTypes,
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
    ) -> VTEXResponse:
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
                log_level=INFO,
                exc_info=True,
            ),
            reraise=True,
        )
        def _send_request() -> Response:
            return client.request(
                method,
                url,
                headers=headers,
                cookies=cookies,
                params=params,
                json=json,
                data=data,
                content=content,
                files=files,
            )

        with Client(timeout=request_config.get_timeout()) as client:
            try:
                response = _send_request()
            except (HTTPError, InvalidURL, CookieConflict, StreamError) as exception:
                raise RequestError(exception) from None

        self._raise_from_response(response=response, config=request_config)

        return VTEXResponse.from_response(response=response)

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
        if config.get_raise_for_status():
            try:
                response.raise_for_status()
            except HTTPStatusError as exception:
                self._logger.error(
                    exception,
                    extra={"response": response.__dict__},
                    exc_info=True,
                    stack_info=True,
                )
                raise VTEXError(exception, response=response) from None
