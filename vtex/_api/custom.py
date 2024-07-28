from typing import Any, Optional

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
        self,
        method: HttpMethodTypes,
        environment: str,
        endpoint: str,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        params: Optional[QueryParamTypes] = None,
        json: Optional[Any] = None,
        data: Optional[RequestData] = None,
        content: Optional[RequestContent] = None,
        files: Optional[RequestFiles] = None,
        **kwargs: Any,
    ) -> VTEXResponse:
        return self._request(
            method=method,
            environment=environment,
            endpoint=endpoint,
            headers=headers,
            cookies=cookies,
            params=params,
            json=json,
            data=data,
            content=content,
            files=files,
            config=self._config.with_overrides(**kwargs),
        )
