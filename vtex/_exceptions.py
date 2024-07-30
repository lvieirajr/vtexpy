from typing import Any, Dict, Union

from ._types import JSONType


class VTEXError(Exception):
    def __init__(self, *args: Any, **kwags: Any) -> None:
        super().__init__(*args, **kwags)


class VTEXRequestError(VTEXError):
    def __init__(
        self,
        *args: Any,
        exception: Union[Exception, None] = None,
        method: Union[str, None] = None,
        url: Union[str, None] = None,
        headers: Union[Dict[str, str], None] = None,
        **kwargs: Any,
    ) -> None:
        self.exception = exception
        self.method = method
        self.url = url
        self.headers = headers

        super().__init__(str(exception or "VTEXRequestError"), *args, **kwargs)


class VTEXResponseError(VTEXError):
    def __init__(
        self,
        *args: Any,
        method: Union[str, None] = None,
        url: Union[str, None] = None,
        request_headers: Union[Dict[str, str], None] = None,
        status: Union[int, None] = None,
        data: JSONType = None,
        response_headers: Union[Dict[str, str], None] = None,
        **kwargs: Any,
    ) -> None:
        self.method = method
        self.url = url
        self.request_headers = request_headers
        self.status = status
        self.data = data
        self.response_headers = response_headers

        super().__init__(str(data or "VTEXResponseError"), *args, **kwargs)
