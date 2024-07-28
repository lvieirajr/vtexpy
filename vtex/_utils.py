from re import compile
from typing import Any

TO_SNAKE_CASE_STEP_1_PATTERN = compile(r"(.)([A-Z][a-z]+)")
TO_SNAKE_CASE_STEP_2_PATTERN = compile(r"([a-z0-9])([A-Z])")


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
