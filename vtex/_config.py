from dataclasses import dataclass
from distutils.util import strtobool
from os import getenv
from typing import Optional

from ._constants import DEFAULT_ENVIRONMENT, DEFAULT_TIMEOUT


@dataclass(frozen=True)
class Config:
    account_name: Optional[str] = None
    app_key: Optional[str] = None
    app_token: Optional[str] = None
    environment: Optional[str] = DEFAULT_ENVIRONMENT
    timeout: Optional[int] = DEFAULT_TIMEOUT
    raise_for_status: Optional[bool] = False

    def with_overrides(
        self: "Config",
        account_name: Optional[str] = None,
        app_key: Optional[str] = None,
        app_token: Optional[str] = None,
        environment: Optional[str] = DEFAULT_ENVIRONMENT,
        timeout: Optional[int] = DEFAULT_TIMEOUT,
        raise_for_status: Optional[bool] = False,
    ) -> "Config":
        return Config(
            account_name=account_name or self.account_name,
            app_key=app_key or self.app_key,
            app_token=app_token or self.app_token,
            environment=environment or self.environment,
            timeout=timeout or self.timeout,
            raise_for_status=raise_for_status or self.raise_for_status,
        )

    def get_account_name(self: "Config") -> str:
        env_account_name = getenv("VTEX_ACCOUNT_NAME", "")

        if not (self.account_name or env_account_name):
            raise ValueError("Missing account_name")

        return self.account_name or env_account_name

    def get_app_key(self: "Config") -> str:
        env_app_key = getenv("VTEX_APP_KEY", "")

        if not (self.app_key or env_app_key):
            raise ValueError("Missing app_key")

        return self.app_key or env_app_key

    def get_app_token(self: "Config") -> str:
        env_app_token = getenv("VTEX_APP_TOKEN", "")

        if not (self.app_token or env_app_token):
            raise ValueError("Missing app_token")

        return self.app_token or env_app_token

    def get_environment(self: "Config") -> str:
        return self.environment or getenv("VTEX_ENVIRONMENT") or DEFAULT_ENVIRONMENT

    def get_timeout(self: "Config") -> int:
        return self.timeout or int(getenv("VTEX_TIMEOUT", DEFAULT_TIMEOUT))

    def get_raise_for_status(self: "Config") -> bool:
        return self.raise_for_status or bool(
            strtobool(getenv("VTEX_RAISE_FOR_STATUS", "False"))
        )
