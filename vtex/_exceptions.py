from typing import Any, Union

from ._types import JSONType


class RequestError(Exception):
    pass


class VTEXError(Exception):
    def __init__(
        self,
        *args: Any,
        exception: Union[Exception, None] = None,
        method: Union[str, None] = None,
        url: Union[str, None] = None,
        headers: Union[JSONType, None] = None,
        status: Union[int, None] = None,
        data: Union[JSONType, None] = None,
        **kwargs: Any,
    ) -> None:
        self.exception = exception
        self.method = method
        self.url = url
        self.headers = headers
        self.status = status
        self.data = data

        super().__init__(str(exception or data or "VTEXError"), *args, **kwargs)
