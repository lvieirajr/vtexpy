from typing import Any, Union

from httpx import Response


class RequestError(Exception):
    pass


class VTEXError(Exception):
    response: Union[Response, None] = None

    def __init__(
        self,
        *args: Any,
        response: Union[Response, None] = None,
        **kwargs: Any,
    ) -> None:
        self.response = response
        super().__init__(*args, **kwargs)
