from dataclasses import dataclass
from os import getenv
from typing import Union

from ._constants import DEFAULT_RAISE_FOR_STATUS, DEFAULT_RETRIES, DEFAULT_TIMEOUT
from ._types import UndefinedType
from ._utils import UNDEFINED, is_nullish_str, is_undefined, str_to_bool


@dataclass
class Config:
    account_name: Union[str, UndefinedType] = UNDEFINED
    app_key: Union[str, UndefinedType] = UNDEFINED
    app_token: Union[str, UndefinedType] = UNDEFINED
    timeout: Union[float, int, None, UndefinedType] = UNDEFINED
    retries: Union[int, UndefinedType] = UNDEFINED
    raise_for_status: Union[bool, UndefinedType] = UNDEFINED

    def __init__(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
        app_key: Union[str, UndefinedType] = UNDEFINED,
        app_token: Union[str, UndefinedType] = UNDEFINED,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
        retries: Union[int, UndefinedType] = UNDEFINED,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> None:
        self.account_name = self._parse_account_name(account_name)
        self.app_key = self._parse_app_key(app_key)
        self.app_token = self._parse_app_token(app_token)
        self.timeout = self._parse_timeout(timeout)
        self.retries = self._parse_retries(retries)
        self.raise_for_status = self._parse_raise_for_status(raise_for_status)

    def with_overrides(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
        app_key: Union[str, UndefinedType] = UNDEFINED,
        app_token: Union[str, UndefinedType] = UNDEFINED,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
        retries: Union[int, UndefinedType] = UNDEFINED,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> "Config":
        return Config(
            account_name=(
                self.account_name if is_undefined(account_name) else account_name
            ),
            app_key=self.app_key if is_undefined(app_key) else app_key,
            app_token=self.app_token if is_undefined(app_token) else app_token,
            timeout=self.timeout if is_undefined(timeout) else timeout,
            retries=self.retries if is_undefined(retries) else retries,
            raise_for_status=(
                self.raise_for_status
                if is_undefined(raise_for_status)
                else raise_for_status
            ),
        )

    def get_account_name(self) -> str:
        if is_undefined(self.account_name):
            raise ValueError("Missing VTEX Account Name")

        return self.account_name  # type: ignore[return-value]

    def get_app_key(self) -> str:
        if is_undefined(self.app_key):
            raise ValueError("Missing VTEX APP Key")

        return self.app_key  # type: ignore[return-value]

    def get_app_token(self) -> str:
        if is_undefined(self.app_token):
            raise ValueError("Missing VTEX APP Token")

        return self.app_token  # type: ignore[return-value]

    def get_timeout(self) -> Union[float, int, None]:
        if is_undefined(self.timeout):
            return DEFAULT_TIMEOUT

        return self.timeout  # type: ignore[return-value]

    def get_retries(self) -> int:
        if is_undefined(self.retries):
            return DEFAULT_RETRIES

        return self.retries  # type: ignore[return-value]

    def get_raise_for_status(self) -> bool:
        if is_undefined(self.raise_for_status):
            return DEFAULT_RAISE_FOR_STATUS

        return self.raise_for_status  # type: ignore[return-value]

    def _parse_account_name(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
    ) -> Union[str, UndefinedType]:
        if isinstance(account_name, str) and account_name:
            return account_name

        if is_undefined(account_name):
            env_account_name = getenv("VTEX_ACCOUNT_NAME", UNDEFINED)

            if is_undefined(env_account_name) or env_account_name:
                return env_account_name

            raise ValueError(f"Invalid value for VTEX_ACCOUNT_NAME: {env_account_name}")

        raise ValueError(f"Invalid value for account_name: {account_name}")

    def _parse_app_key(
        self,
        app_key: Union[str, UndefinedType] = UNDEFINED,
    ) -> Union[str, UndefinedType]:
        if isinstance(app_key, str) and app_key:
            return app_key

        if is_undefined(app_key):
            env_app_key = getenv("VTEX_APP_KEY", UNDEFINED)

            if is_undefined(env_app_key) or env_app_key:
                return env_app_key

            raise ValueError(f"Invalid value for VTEX_APP_KEY: {env_app_key}")

        raise ValueError(f"Invalid value for app_key: {app_key}")

    def _parse_app_token(
        self,
        app_token: Union[str, UndefinedType] = UNDEFINED,
    ) -> Union[str, UndefinedType]:
        if isinstance(app_token, str) and app_token:
            return app_token

        if is_undefined(app_token):
            env_app_token = getenv("VTEX_APP_TOKEN", UNDEFINED)

            if is_undefined(env_app_token) or env_app_token:
                return env_app_token

            raise ValueError(f"Invalid value for VTEX_APP_TOKEN: {env_app_token}")

        raise ValueError(f"Invalid value for app_token: {app_token}")

    def _parse_timeout(
        self,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
    ) -> Union[float, int, None, UndefinedType]:
        if isinstance(timeout, (float, int)) and timeout > 0:
            return float(timeout)

        if timeout is None:
            return timeout

        if is_undefined(timeout):
            env_timeout = getenv("VTEX_TIMEOUT", UNDEFINED)

            if is_undefined(env_timeout):
                return env_timeout  # type: ignore[return-value]

            if is_nullish_str(env_timeout):  # type: ignore[arg-type]
                return None

            if env_timeout.isnumeric():  # type: ignore[union-attr]
                return float(env_timeout)  # type: ignore[arg-type]

            raise ValueError(f"Invalid value for VTEX_TIMEOUT: {env_timeout}")

        raise ValueError(f"Invalid value for timeout: {timeout}")

    def _parse_retries(
        self,
        retries: Union[int, UndefinedType] = UNDEFINED,
    ) -> Union[int, UndefinedType]:
        if isinstance(retries, int) and retries >= 0:
            return retries

        if is_undefined(retries):
            env_retries = getenv("VTEX_RETRIES", UNDEFINED)

            if is_undefined(env_retries):
                return env_retries  # type: ignore[return-value]

            if env_retries.isnumeric():  # type: ignore[union-attr]
                return int(round(float(env_retries), 0))  # type: ignore[arg-type]

            raise ValueError(f"Invalid value for VTEX_RETRIES: {env_retries}")

        raise ValueError(f"Invalid value for retries: {retries}")

    def _parse_raise_for_status(
        self,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> Union[bool, UndefinedType]:
        if isinstance(raise_for_status, bool):
            return raise_for_status

        if is_undefined(raise_for_status):
            env_raise_for_status = getenv("VTEX_RAISE_FOR_STATUS", UNDEFINED)

            if is_undefined(env_raise_for_status):
                return env_raise_for_status  # type: ignore[return-value]

            try:
                self.raise_for_status = str_to_bool(str(env_raise_for_status))
            except ValueError:
                raise ValueError(
                    f"Invalid value for VTEX_RAISE_FOR_STATUS: {env_raise_for_status}"
                ) from None

        raise ValueError(f"Invalid value for raise_for_status: {raise_for_status}")
