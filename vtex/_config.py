from dataclasses import dataclass
from os import getenv
from typing import Union

from distutils.util import strtobool

from ._constants import DEFAULT_RAISE_FOR_STATUS, DEFAULT_RETRIES, DEFAULT_TIMEOUT


@dataclass(frozen=True)
class Config:
    account_name: Union[str, None] = None
    app_key: Union[str, None] = None
    app_token: Union[str, None] = None

    timeout: Union[int, None] = None
    retries: Union[int, None] = None
    raise_for_status: Union[bool, None] = None

    @property
    def _env_account_name(self) -> Union[str, None]:
        return getenv("VTEX_ACCOUNT_NAME")

    @property
    def _env_app_key(self) -> Union[str, None]:
        return getenv("VTEX_APP_KEY")

    @property
    def _env_app_token(self) -> Union[str, None]:
        return getenv("VTEX_APP_TOKEN")

    @property
    def _env_environment(self) -> Union[str, None]:
        return getenv("VTEX_ENVIRONMENT")

    @property
    def _env_timeout(self) -> Union[str, None]:
        return getenv("VTEX_TIMEOUT")

    @property
    def _env_retries(self) -> Union[str, None]:
        return getenv("VTEX_RETRIES")

    @property
    def _env_raise_for_status(self) -> Union[str, None]:
        return getenv("VTEX_RAISE_FOR_STATUS")

    def with_overrides(
        self,
        account_name: Union[str, None] = None,
        app_key: Union[str, None] = None,
        app_token: Union[str, None] = None,
        timeout: Union[int, None] = None,
        retries: Union[int, None] = None,
        raise_for_status: Union[bool, None] = None,
    ) -> "Config":
        timeout = timeout if isinstance(timeout, int) else self.timeout
        retries = retries if isinstance(retries, int) else self.retries
        raise_for_status = (
            raise_for_status
            if isinstance(raise_for_status, bool)
            else self.raise_for_status
        )

        return Config(
            account_name=account_name or self.account_name,
            app_key=app_key or self.app_key,
            app_token=app_token or self.app_token,
            timeout=timeout,
            retries=retries,
            raise_for_status=raise_for_status,
        )

    def get_account_name(self) -> str:
        account_name = self.account_name or self._env_account_name

        if not account_name:
            raise ValueError("Missing VTEX Account Name")

        return account_name

    def get_app_key(self) -> str:
        app_key = self.app_key or self._env_app_key

        if not app_key:
            raise ValueError("Missing VTEX APP Key")

        return app_key

    def get_app_token(self) -> str:
        app_token = self.app_token or self._env_app_token

        if not app_token:
            raise ValueError("Missing VTEX APP Token")

        return app_token

    def get_timeout(self) -> int:
        timeout = self.timeout or self._env_timeout

        if not timeout:
            return DEFAULT_TIMEOUT

        return int(timeout)

    def get_retries(self) -> int:
        retries = self.retries or self._env_retries

        if not retries:
            return DEFAULT_RETRIES

        return int(retries)

    def get_raise_for_status(self) -> bool:
        raise_for_status = self.raise_for_status or self._env_raise_for_status

        if not raise_for_status:
            return DEFAULT_RAISE_FOR_STATUS

        return bool(
            strtobool(raise_for_status)
            if isinstance(raise_for_status, str)
            else raise_for_status
        )
