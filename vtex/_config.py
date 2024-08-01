# type: ignore
from os import getenv
from typing import Union

from ._constants import (
    ACCOUNT_NAME_ENV_VAR,
    APP_KEY_ENV_VAR,
    APP_TOKEN_ENV_VAR,
    DEFAULT_RAISE_FOR_STATUS,
    DEFAULT_RETRY_ATTEMPTS,
    DEFAULT_RETRY_BACKOFF_EXPONENTIAL,
    DEFAULT_RETRY_BACKOFF_MAX,
    DEFAULT_RETRY_BACKOFF_MIN,
    DEFAULT_RETRY_LOGS,
    DEFAULT_RETRY_STATUSES,
    DEFAULT_TIMEOUT,
    RAISE_FOR_STATUS_ENV_VAR,
    RETRY_ATTEMPTS_ENV_VAR,
    RETRY_BACKOFF_EXPONENTIAL_ENV_VAR,
    RETRY_BACKOFF_MAX_ENV_VAR,
    RETRY_BACKOFF_MIN_ENV_VAR,
    RETRY_LOGS_ENV_VAR,
    RETRY_STATUSES_ENV_VAR,
    TIMEOUT_ENV_VAR,
)
from ._types import IterableType, UndefinedType
from ._utils import UNDEFINED, is_nullish_str, is_undefined, str_to_bool


class Config:
    def __init__(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
        app_key: Union[str, UndefinedType] = UNDEFINED,
        app_token: Union[str, UndefinedType] = UNDEFINED,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
        retry_attempts: Union[int, UndefinedType] = UNDEFINED,
        retry_backoff_min: Union[float, int, UndefinedType] = UNDEFINED,
        retry_backoff_max: Union[float, int, UndefinedType] = UNDEFINED,
        retry_backoff_exponential: Union[bool, float, int, UndefinedType] = UNDEFINED,
        retry_statuses: Union[IterableType[int], UndefinedType] = UNDEFINED,
        retry_logs: Union[bool, UndefinedType] = UNDEFINED,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> None:
        self._account_name = self._parse_account_name(account_name)
        self._app_key = self._parse_app_key(app_key)
        self._app_token = self._parse_app_token(app_token)
        self._timeout = self._parse_timeout(timeout)
        self._retry_attempts = self._parse_retry_attempts(retry_attempts)
        self._retry_backoff_min = self._parse_retry_backoff_min(retry_backoff_min)
        self._retry_backoff_max = self._parse_retry_backoff_max(retry_backoff_max)
        self._retry_backoff_exponential = self._parse_retry_backoff_exponential(
            retry_backoff_exponential,
        )
        self._retry_statuses = self._parse_retry_statuses(retry_statuses)
        self._retry_logs = self._parse_retry_logs(retry_logs)
        self._raise_for_status = self._parse_raise_for_status(raise_for_status)

    def with_overrides(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
        app_key: Union[str, UndefinedType] = UNDEFINED,
        app_token: Union[str, UndefinedType] = UNDEFINED,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
        retry_attempts: Union[int, UndefinedType] = UNDEFINED,
        retry_backoff_min: Union[float, int, UndefinedType] = UNDEFINED,
        retry_backoff_max: Union[float, int, UndefinedType] = UNDEFINED,
        retry_backoff_exponential: Union[bool, int, float, UndefinedType] = UNDEFINED,
        retry_statuses: Union[IterableType[int], UndefinedType] = UNDEFINED,
        retry_logs: Union[bool, UndefinedType] = UNDEFINED,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> "Config":
        return Config(
            account_name=(
                self._account_name if is_undefined(account_name) else account_name
            ),
            app_key=self._app_key if is_undefined(app_key) else app_key,
            app_token=self._app_token if is_undefined(app_token) else app_token,
            timeout=self._timeout if is_undefined(timeout) else timeout,
            retry_attempts=(
                self._retry_attempts if is_undefined(retry_attempts) else retry_attempts
            ),
            retry_backoff_min=(
                self._retry_backoff_min
                if is_undefined(retry_backoff_min)
                else retry_backoff_min
            ),
            retry_backoff_max=(
                self._retry_backoff_max
                if is_undefined(retry_backoff_max)
                else retry_backoff_max
            ),
            retry_backoff_exponential=(
                self._retry_backoff_exponential
                if is_undefined(retry_backoff_exponential)
                else retry_backoff_exponential
            ),
            retry_statuses=(
                self._retry_statuses if is_undefined(retry_statuses) else retry_statuses
            ),
            retry_logs=(self._retry_logs if is_undefined(retry_logs) else retry_logs),
            raise_for_status=(
                self._raise_for_status
                if is_undefined(raise_for_status)
                else raise_for_status
            ),
        )

    def get_account_name(self) -> str:
        if is_undefined(self._account_name):
            raise ValueError("Missing VTEX Account Name")

        return self._account_name

    def get_app_key(self) -> str:
        if is_undefined(self._app_key):
            raise ValueError("Missing VTEX APP Key")

        return self._app_key

    def get_app_token(self) -> str:
        if is_undefined(self._app_token):
            raise ValueError("Missing VTEX APP Token")

        return self._app_token

    def get_timeout(self) -> Union[float, None]:
        if is_undefined(self._timeout):
            return DEFAULT_TIMEOUT

        return self._timeout

    def get_retry_attempts(self) -> int:
        if is_undefined(self._retry_attempts):
            return DEFAULT_RETRY_ATTEMPTS

        return self._retry_attempts

    def get_retry_backoff_min(self) -> float:
        if is_undefined(self._retry_backoff_min):
            return DEFAULT_RETRY_BACKOFF_MIN

        return self._retry_backoff_min

    def get_retry_backoff_max(self) -> float:
        if is_undefined(self._retry_backoff_max):
            return DEFAULT_RETRY_BACKOFF_MAX

        return self._retry_backoff_max

    def get_retry_backoff_exponential(self) -> float:
        if is_undefined(self._retry_backoff_exponential):
            return DEFAULT_RETRY_BACKOFF_EXPONENTIAL

        return self._retry_backoff_exponential

    def get_retry_statuses(self) -> IterableType[int]:
        if is_undefined(self._retry_statuses):
            return DEFAULT_RETRY_STATUSES

        return self._retry_statuses

    def get_retry_logs(self) -> bool:
        if is_undefined(self._retry_logs):
            return DEFAULT_RETRY_LOGS

        return self._retry_logs

    def get_raise_for_status(self) -> bool:
        if is_undefined(self._raise_for_status):
            return DEFAULT_RAISE_FOR_STATUS

        return self._raise_for_status

    def _parse_account_name(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
    ) -> Union[str, UndefinedType]:
        if isinstance(account_name, str) and account_name:
            return account_name

        if is_undefined(account_name):
            env_account_name = getenv(ACCOUNT_NAME_ENV_VAR, UNDEFINED)

            if is_undefined(env_account_name) or env_account_name:
                return env_account_name

            raise ValueError(
                f"Invalid value for {ACCOUNT_NAME_ENV_VAR}: {env_account_name}",
            )

        raise ValueError(f"Invalid value for account_name: {account_name}")

    def _parse_app_key(
        self,
        app_key: Union[str, UndefinedType] = UNDEFINED,
    ) -> Union[str, UndefinedType]:
        if isinstance(app_key, str) and app_key:
            return app_key

        if is_undefined(app_key):
            env_app_key = getenv(APP_KEY_ENV_VAR, UNDEFINED)

            if is_undefined(env_app_key) or env_app_key:
                return env_app_key

            raise ValueError(f"Invalid value for {APP_KEY_ENV_VAR}: {env_app_key}")

        raise ValueError(f"Invalid value for app_key: {app_key}")

    def _parse_app_token(
        self,
        app_token: Union[str, UndefinedType] = UNDEFINED,
    ) -> Union[str, UndefinedType]:
        if isinstance(app_token, str) and app_token:
            return app_token

        if is_undefined(app_token):
            env_app_token = getenv(APP_TOKEN_ENV_VAR, UNDEFINED)

            if is_undefined(env_app_token) or env_app_token:
                return env_app_token

            raise ValueError(f"Invalid value for {APP_TOKEN_ENV_VAR}: {env_app_token}")

        raise ValueError(f"Invalid value for app_token: {app_token}")

    def _parse_timeout(
        self,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
    ) -> Union[float, None, UndefinedType]:
        if isinstance(timeout, (float, int)) and timeout > 0:
            return float(timeout)

        if timeout is None:
            return timeout

        if is_undefined(timeout):
            env_timeout = getenv(TIMEOUT_ENV_VAR, UNDEFINED)

            if is_undefined(env_timeout):
                return env_timeout

            if is_nullish_str(env_timeout):
                return None

            try:
                env_timeout = float(env_timeout)

                if env_timeout > 0:
                    return env_timeout
            except ValueError:
                pass

            raise ValueError(f"Invalid value for {TIMEOUT_ENV_VAR}: {env_timeout}")

        raise ValueError(f"Invalid value for timeout: {timeout}")

    def _parse_retry_attempts(
        self,
        retry_attempts: Union[int, UndefinedType] = UNDEFINED,
    ) -> Union[int, UndefinedType]:
        if isinstance(retry_attempts, int) and retry_attempts >= 0:
            return retry_attempts

        if is_undefined(retry_attempts):
            env_retry_attempts = getenv(RETRY_ATTEMPTS_ENV_VAR, UNDEFINED)

            if is_undefined(env_retry_attempts):
                return env_retry_attempts

            try:
                env_retry_attempts = int(env_retry_attempts)

                if env_retry_attempts >= 0:
                    return env_retry_attempts
            except ValueError:
                pass

            raise ValueError(
                f"Invalid value for {RETRY_ATTEMPTS_ENV_VAR}: {env_retry_attempts}",
            )

        raise ValueError(f"Invalid value for retry_attempts: {retry_attempts}")

    def _parse_retry_backoff_min(
        self,
        retry_backoff_min: Union[float, int, UndefinedType] = UNDEFINED,
    ) -> Union[float, UndefinedType]:
        if isinstance(retry_backoff_min, (float, int)) and retry_backoff_min > 0:
            return float(retry_backoff_min)

        if is_undefined(retry_backoff_min):
            env_retry_backoff_min = getenv(RETRY_BACKOFF_MIN_ENV_VAR, UNDEFINED)

            if is_undefined(env_retry_backoff_min):
                return env_retry_backoff_min

            try:
                env_retry_backoff_min = float(env_retry_backoff_min)

                if env_retry_backoff_min > 0:
                    return env_retry_backoff_min
            except ValueError:
                pass

            raise ValueError(
                f"Invalid value for {RETRY_BACKOFF_MIN_ENV_VAR}: "
                f"{env_retry_backoff_min}",
            )

        raise ValueError(f"Invalid value for retry_backoff_min: {retry_backoff_min}")

    def _parse_retry_backoff_max(
        self,
        retry_backoff_max: Union[float, UndefinedType] = UNDEFINED,
    ) -> Union[float, UndefinedType]:
        if isinstance(retry_backoff_max, (float, int)) and retry_backoff_max > 0:
            return float(retry_backoff_max)

        if is_undefined(retry_backoff_max):
            env_retry_backoff_max = getenv(RETRY_BACKOFF_MAX_ENV_VAR, UNDEFINED)

            if is_undefined(env_retry_backoff_max):
                return env_retry_backoff_max

            try:
                env_retry_backoff_max = float(env_retry_backoff_max)

                if env_retry_backoff_max > 0:
                    return env_retry_backoff_max
            except ValueError:
                pass

            raise ValueError(
                f"Invalid value for {RETRY_BACKOFF_MAX_ENV_VAR}: "
                f"{env_retry_backoff_max}",
            )

        raise ValueError(f"Invalid value for retry_backoff_max: {retry_backoff_max}")

    def _parse_retry_backoff_exponential(
        self,
        retry_backoff_exponential: Union[bool, float, int, UndefinedType] = UNDEFINED,
    ) -> Union[float, UndefinedType]:
        if (
            isinstance(retry_backoff_exponential, (float, int))
            and retry_backoff_exponential >= 1
        ):
            return float(retry_backoff_exponential)
        elif isinstance(retry_backoff_exponential, bool):
            return retry_backoff_exponential

        if is_undefined(retry_backoff_exponential):
            env_retry_backoff_exponential = getenv(
                RETRY_BACKOFF_EXPONENTIAL_ENV_VAR,
                UNDEFINED,
            )

            if is_undefined(env_retry_backoff_exponential):
                return env_retry_backoff_exponential

            try:
                env_retry_backoff_exponential = float(env_retry_backoff_exponential)

                if env_retry_backoff_exponential >= 1:
                    return env_retry_backoff_exponential
            except ValueError:
                pass

            try:
                return str_to_bool(env_retry_backoff_exponential)
            except ValueError:
                raise ValueError(
                    f"Invalid value for {RETRY_BACKOFF_EXPONENTIAL_ENV_VAR}: "
                    f"{env_retry_backoff_exponential}",
                ) from None

        raise ValueError(
            f"Invalid value for retry_backoff_exponential: {retry_backoff_exponential}",
        )

    def _parse_retry_statuses(
        self,
        retry_statuses: Union[IterableType[int], UndefinedType] = UNDEFINED,
    ) -> Union[IterableType[int], UndefinedType]:
        if isinstance(retry_statuses, (list, set, tuple)) and all(
            isinstance(status, int) for status in retry_statuses
        ):
            return retry_statuses

        if is_undefined(retry_statuses):
            env_retry_statuses = getenv(RETRY_STATUSES_ENV_VAR, UNDEFINED)

            if is_undefined(env_retry_statuses):
                return env_retry_statuses

            try:
                return [int(status) for status in env_retry_statuses.split(",")]
            except ValueError:
                raise ValueError(
                    f"Invalid value for {RETRY_STATUSES_ENV_VAR}: {env_retry_statuses}",
                ) from None

        raise ValueError(f"Invalid value for retry_statuses: {retry_statuses}")

    def _parse_retry_logs(
        self,
        retry_logs: Union[bool, UndefinedType] = UNDEFINED,
    ) -> Union[bool, UndefinedType]:
        if isinstance(retry_logs, bool):
            return retry_logs

        if is_undefined(retry_logs):
            env_retry_logs = getenv(RETRY_LOGS_ENV_VAR, UNDEFINED)

            if is_undefined(env_retry_logs):
                return env_retry_logs

            try:
                return str_to_bool(env_retry_logs)
            except ValueError:
                raise ValueError(
                    f"Invalid value for {RETRY_LOGS_ENV_VAR}: {env_retry_logs}"
                ) from None

        raise ValueError(f"Invalid value for retry_logs: {retry_logs}")

    def _parse_raise_for_status(
        self,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> Union[bool, UndefinedType]:
        if isinstance(raise_for_status, bool):
            return raise_for_status

        if is_undefined(raise_for_status):
            env_raise_for_status = getenv(RAISE_FOR_STATUS_ENV_VAR, UNDEFINED)

            if is_undefined(env_raise_for_status):
                return env_raise_for_status

            try:
                return str_to_bool(env_raise_for_status)
            except ValueError:
                raise ValueError(
                    f"Invalid value for {RAISE_FOR_STATUS_ENV_VAR}: "
                    f"{env_raise_for_status}"
                ) from None

        raise ValueError(f"Invalid value for raise_for_status: {raise_for_status}")
