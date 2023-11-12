from http.cookiejar import CookieJar
from typing import (
    IO,
    Any,
    AsyncIterable,
    Dict,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from httpx import Cookies, Headers, QueryParams

HttpMethodTypes = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]

PrimitiveTypes = Union[str, int, float, bool, None]
PrimitiveSequenceType = Sequence[PrimitiveTypes]

JsonType = Dict[str, Union[PrimitiveTypes, PrimitiveSequenceType]]
JsonSequenceType = Sequence[JsonType]

ResponseItemsType = Union[PrimitiveSequenceType, JsonSequenceType]

RequestContent = Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]]

RequestData = Mapping[str, Any]

FileContent = Union[IO[bytes], bytes, str]
FileTypes = Union[
    FileContent,
    Tuple[Optional[str], FileContent],
    Tuple[Optional[str], FileContent, Optional[str]],
    Tuple[Optional[str], FileContent, Optional[str], Mapping[str, str]],
]
RequestFiles = Union[Mapping[str, FileTypes], Sequence[Tuple[str, FileTypes]]]

QueryParamTypes = Union[
    QueryParams,
    Mapping[str, Union[PrimitiveTypes, PrimitiveSequenceType]],
    List[Tuple[str, PrimitiveTypes]],
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

CookieTypes = Union[Cookies, CookieJar, Dict[str, str], List[Tuple[str, str]]]
