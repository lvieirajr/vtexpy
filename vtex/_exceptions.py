from typing import Any, Union

from ._types import JSONType


class RequestError(Exception):
    pass


class VTEXError(Exception):
    def __init__(
        self,
        *args: Any,
        method: Union[str, None] = None,
        url: Union[str, None] = None,
        request_headers: Union[JSONType, None] = None,
        status: Union[int, None] = None,
        data: Union[JSONType, None] = None,
        response_headers: Union[JSONType, None] = None,
        **kwargs: Any,
    ) -> None:
        self.method = method
        self.url = url
        self.request_headers = request_headers
        self.status = status
        self.data = data
        self.response_headers = response_headers

        super().__init__(str(data or "VTEXError"), *args, **kwargs)
