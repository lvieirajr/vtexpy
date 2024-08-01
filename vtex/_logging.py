from logging import Logger, getLogger

from ._utils import to_snake_case


def get_child_logger(logger: Logger, name: str) -> Logger:
    return logger.getChild(to_snake_case(name))


def get_logger(name: str) -> Logger:
    return getLogger(f"vtex.{to_snake_case(name)}")
