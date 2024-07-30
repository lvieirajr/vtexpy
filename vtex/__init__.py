from . import _constants as VTEXConstants  # noqa: N812
from ._exceptions import VTEXError, VTEXRequestError, VTEXResponseError
from ._vtex import VTEX

__all__ = [
    "VTEX",
    "VTEXConstants",
    "VTEXError",
    "VTEXRequestError",
    "VTEXResponseError",
]


for name in __all__:
    locals()[name].__module__ = "vtex"
