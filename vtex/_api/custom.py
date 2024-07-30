from typing import Any, Union

from .._dto import VTEXResponse
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
        headers: Union[HeaderTypes, None] = None,
        cookies: Union[CookieTypes, None] = None,
        params: Union[QueryParamTypes, None] = None,
        json: Union[Any, None] = None,
        data: Union[RequestData, None] = None,
        content: Union[RequestContent, None] = None,
        files: Union[RequestFiles, None] = None,
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
