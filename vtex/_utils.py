from distutils.util import strtobool
from re import compile
from typing import Any

from box import Box, BoxList

from ._types import UndefinedType

TO_SNAKE_CASE_STEP_1_PATTERN = compile(r"(.)([A-Z][a-z]+)")
TO_SNAKE_CASE_STEP_2_PATTERN = compile(r"([a-z0-9])([A-Z])")


def is_nullish_str(value: str) -> bool:
    return not value or value.lower() in {"null", "none", "nil"}


def is_undefined(value: Any) -> bool:
    return isinstance(value, UndefinedType)


def str_to_bool(value: str) -> bool:
    return bool(strtobool(value))


def string_to_snake_case(string: str) -> str:
    return TO_SNAKE_CASE_STEP_2_PATTERN.sub(
        r"\1_\2",
        TO_SNAKE_CASE_STEP_1_PATTERN.sub(r"\1_\2", string),
    ).lower()


def to_snake_case(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {
            (string_to_snake_case(key) if isinstance(key, str) else key): (
                to_snake_case(value)
            )
            for key, value in obj.items()
        }

    if isinstance(obj, (list, set, tuple)):
        return type(obj)([to_snake_case(element) for element in obj])

    return obj


def to_box(obj: Any, convert_to_snake_case: bool = True) -> Any:
    if convert_to_snake_case:
        obj = to_snake_case(obj)

    if isinstance(obj, dict):
        return Box(obj)

    if isinstance(obj, (list, set, tuple)):
        return type(obj)(BoxList(obj))

    return obj


def box_repr(self: Box) -> str:
    return str(self.to_dict())


def box_list_repr(self: BoxList) -> str:
    return str(self.to_list())


Box.__repr__ = box_repr
BoxList.__repr__ = box_list_repr
