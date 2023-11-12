from logging import getLogger
from typing import Any, Optional

from httpx import (
    Client,
    CookieConflict,
    Headers,
    HTTPError,
    InvalidURL,
    StreamError,
)

from .._exceptions import RequestError
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
    Base client for all VTEX API collections.
    """

    _BASE_URL = "https://{account_name}.{environment}.com.br/{endpoint}"
    _APP_KEY_HEADER = "X-VTEX-API-AppKey"
    _APP_TOKEN_HEADER = "X-VTEX-API-AppToken"  # noqa: S105
    _DEFAULT_TIMEOUT = 60

    def __init__(
        self: "BaseAPI",
        account_name: Optional[str] = None,
        app_key: Optional[str] = None,
        app_token: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> None:
        self._account_name = account_name
        self._app_key = app_key
        self._app_token = app_token
        self._environment = environment
        self._logger = getLogger(type(self).__name__)

    def _request(
        self: "BaseAPI",
        method: HttpMethodTypes,
        endpoint: str,
        content: Optional[RequestContent] = None,
        data: Optional[RequestData] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        timeout: int = _DEFAULT_TIMEOUT,
        **kwargs: Any,
    ) -> VTEXResponse:
        url = self._get_url(
            endpoint=endpoint,
            account_name=kwargs.get("account_name"),
            environment=kwargs.get("environment"),
        )
        headers = self._get_headers(
            headers=headers,
            app_key=kwargs.get("app_key"),
            app_token=kwargs.get("app_token"),
        )

        with Client() as client:
            try:
                response = client.request(
                    method,
                    url,
                    content=content,
                    data=data,
                    files=files,
                    json=json,
                    params=params,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                )
            except (HTTPError, InvalidURL, CookieConflict, StreamError) as exception:
                raise RequestError() from exception

        return VTEXResponse(
            data=response.json(),
            status=response.status_code,
            headers=dict(response.headers.items()),
        )

    def _get_url(
        self: "BaseAPI",
        endpoint: str,
        account_name: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> str:
        if not (account_name or self._account_name):
            raise ValueError("Missing account_name")

        if not (environment or self._environment):
            raise ValueError("Missing environment")

        return self._BASE_URL.format(
            endpoint=endpoint,
            account_name=account_name or self._account_name,
            environment=environment or self._environment,
        )

    def _get_headers(
        self: "BaseAPI",
        headers: Optional[HeaderTypes],
        app_key: Optional[str] = None,
        app_token: Optional[str] = None,
    ) -> Headers:
        request_headers = Headers(headers=headers)

        if app_key:
            request_headers[self._APP_KEY_HEADER] = app_key
        elif self._APP_KEY_HEADER not in request_headers and self._app_key:
            request_headers[self._APP_KEY_HEADER] = self._app_key
        elif self._APP_KEY_HEADER not in request_headers:
            raise ValueError("Missing app_key")

        if app_token:
            request_headers[self._APP_TOKEN_HEADER] = app_token
        elif self._APP_TOKEN_HEADER not in request_headers and self._app_token:
            request_headers[self._APP_TOKEN_HEADER] = self._app_token
        elif self._APP_TOKEN_HEADER not in request_headers:
            raise ValueError("Missing app_token")

        return request_headers
