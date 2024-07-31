from http.cookiejar import CookieJar
from typing import (
    IO,
    Any,
    AsyncIterable,
    Iterable,
    Literal,
    Mapping,
    Sequence,
    Tuple,
    Union,
)

from httpx import Cookies, Headers, QueryParams


class UndefinedType:
    pass


HTTPMethodType = Literal[
    "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT",
    "delete", "get", "head", "options", "patch", "post", "put",
]

PrimitiveTypes = Union[None, bool, int, float, str]
PrimitiveSequenceType = Sequence[PrimitiveTypes]

JSONType = Union[PrimitiveTypes, Sequence["JSONType"], Mapping[str, "JSONType"]]

RequestContent = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]

RequestData = Mapping[str, Any]

FileContent = Union[IO[bytes], bytes, str]
FileTypes = Union[
    FileContent,
    Tuple[Union[str, None], FileContent],
    Tuple[Union[str, None], FileContent, Union[str, None]],
    Tuple[Union[str, None], FileContent, Union[str, None], Mapping[str, str]],
]
RequestFiles = Union[Mapping[str, FileTypes], Sequence[Tuple[str, FileTypes]]]

QueryParamTypes = Union[
    QueryParams,
    Mapping[str, Union[PrimitiveTypes, PrimitiveSequenceType]],
    Sequence[Tuple[str, PrimitiveTypes]],
    Tuple[Tuple[str, PrimitiveTypes], ...],
    str,
    bytes,
]

HeaderTypes = Union[
    Headers,
    Mapping[str, str],
    Mapping[bytes, bytes],
    Sequence[Tuple[str, str]],
    Sequence[Tuple[bytes, bytes]],
]

CookieTypes = Union[Cookies, CookieJar, Mapping[str, str], Sequence[Tuple[str, str]]]
