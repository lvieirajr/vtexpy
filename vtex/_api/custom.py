from typing import Any, Optional

from .._config import Config
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
from .base import BaseAPI


class CustomAPI(BaseAPI):
    """
    Client for calling endpoints that have not yet been implemented by the SDK.
    You can directly call the `request` method to call any VTEX API.
    """

    def request(
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
        return self._request(
            method=method,
            endpoint=endpoint,
            headers=headers,
            cookies=cookies,
            params=params,
            json=json,
            data=data,
            content=content,
            files=files,
            config=config,
        )
