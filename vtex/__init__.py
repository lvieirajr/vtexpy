from . import _constants as VTEXConstants  # noqa: N812
from ._exceptions import RequestError, VTEXError
from ._response import PaginatedResponse, VTEXResponse
from ._vtex import VTEX

__all__ = [
    "PaginatedResponse",
    "RequestError",
    "VTEX",
    "VTEXConstants",
    "VTEXError",
    "VTEXResponse",
]


for name in __all__:
    locals()[name].__module__ = "vtex"
