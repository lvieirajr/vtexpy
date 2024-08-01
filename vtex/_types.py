from typing import (
    List,
    Literal,
    Mapping,
    Set,
    Tuple,
    TypeVar,
    Union,
)


class UndefinedType:
    def __repr__(self) -> str:
        return "Undefined"

    def __str__(self) -> str:
        return repr(self)


IterableValueType = TypeVar("IterableValueType")
IterableType = Union[
    Tuple[IterableValueType, ...],
    Set[IterableValueType],
    List[IterableValueType],
]

HTTPMethodType = Literal[
    "DELETE",
    "GET",
    "HEAD",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
    "delete",
    "get",
    "head",
    "options",
    "patch",
    "post",
    "put",
]

PrimitiveTypes = Union[None, bool, int, float, str]
JSONType = Union[PrimitiveTypes, IterableType["JSONType"], Mapping[str, "JSONType"]]
