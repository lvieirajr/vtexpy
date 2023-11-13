from logging import getLogger
from typing import Any, Optional
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


class BaseAPI:
    """
    Base client for VTEX API.
    """

    def __init__(self: "BaseAPI", config: Optional[Config] = None) -> None:
        self._config = config or Config()
        self._logger = getLogger(type(self).__name__)

    def _request(
        self: "BaseAPI",
        method: HttpMethodTypes,
        endpoint: str,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        params: Optional[QueryParamTypes] = None,
        json: Optional[Any] = None,
        data: Optional[RequestData] = None,
        content: Optional[RequestContent] = None,
        files: Optional[RequestFiles] = None,
        config: Optional[Config] = None,
    ) -> VTEXResponse:
        request_config = self._get_config(config=config)

        with Client(timeout=request_config.get_timeout()) as client:
            try:
                response = client.request(
                    method,
                    self._get_url(config=request_config, endpoint=endpoint),
                    headers=self._get_headers(config=request_config, headers=headers),
                    cookies=cookies,
                    params=params,
                    json=json,
                    data=data,
                    content=content,
                    files=files,
                )
            except (HTTPError, InvalidURL, CookieConflict, StreamError) as exception:
                raise RequestError(exception) from exception

        self._raise_from_response(config=request_config, response=response)

        return VTEXResponse(
            data=response.json(),
            status=response.status_code,
            headers=dict(response.headers.items()),
        )

    def _get_config(self: "BaseAPI", config: Optional[Config]) -> Config:
        return config or self._config

    def _get_url(self: "BaseAPI", config: Config, endpoint: str) -> str:
        return urljoin(
            f"https://{config.get_account_name()}.{config.get_environment()}.com.br",
            endpoint,
        )

    def _get_headers(
        self: "BaseAPI",
        config: Config,
        headers: Optional[HeaderTypes] = None,
    ) -> Headers:
        request_headers = Headers(headers=headers)

        request_headers[APP_KEY_HEADER] = config.get_app_key()
        request_headers[APP_TOKEN_HEADER] = config.get_app_token()

        request_headers["Content-Type"] = "application/json; charset=utf-8"
        request_headers["Accept"] = "application/json"

        return request_headers

    def _raise_from_response(self, config: Config, response: Response) -> None:
        if config.get_raise_for_status():
            try:
                response.raise_for_status()
            except HTTPStatusError as exception:
                raise VTEXError(
                    exception,
                    status=response.status_code,
                ) from exception
