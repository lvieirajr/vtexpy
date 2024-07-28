from typing import Any, Optional


class RequestError(Exception):
    pass


class VTEXError(Exception):
    status = None

    def __init__(self, *args: Any, status: Optional[int] = None) -> None:
        super().__init__(*args)
        self.status = status
