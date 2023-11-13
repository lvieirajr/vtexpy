from ._exceptions import RequestError, VTEXError
from ._response import PaginatedResponse, VTEXResponse
from ._vtex import VTEX

__all__ = [
    "PaginatedResponse",
    "RequestError",
    "VTEX",
    "VTEXError",
    "VTEXResponse",
]


for name in __all__:
    locals()[name].__module__ = "vtex"
