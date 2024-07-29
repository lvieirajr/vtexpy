from re import compile
from typing import Any, Dict

from distutils.util import strtobool

from ._types import JSONType, UndefinedType

TO_SNAKE_CASE_STEP_1_PATTERN = compile(r"(.)([A-Z][a-z]+)")
TO_SNAKE_CASE_STEP_2_PATTERN = compile(r"([a-z0-9])([A-Z])")

UNDEFINED = UndefinedType()


def is_nullish_str(value: str) -> bool:
    return not value or value.lower() in {"null", "none", "nil"}


def is_undefined(value: Any) -> bool:
    return isinstance(value, UndefinedType)


def exclude_undefined_values(obj: Dict[Any, Any]) -> Dict[Any, Any]:
    return {key: value for key, value in obj.items() if not is_undefined(value)}


def str_to_bool(value: str) -> bool:
    return bool(strtobool(value))


def to_snake_case(string: str) -> str:
    return TO_SNAKE_CASE_STEP_2_PATTERN.sub(
        r"\1_\2",
        TO_SNAKE_CASE_STEP_1_PATTERN.sub(r"\1_\2", string),
    ).lower()


def to_snake_case_deep(obj: JSONType) -> JSONType:
    if isinstance(obj, dict):
        return {
            (to_snake_case(key) if isinstance(key, str) else key): (
                to_snake_case_deep(value)
            )
            for key, value in obj.items()
        }

    if isinstance(obj, (list, set, tuple)):
        return type(obj)([to_snake_case_deep(element) for element in obj])

    return obj
