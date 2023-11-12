from functools import cached_property
from typing import Optional

from ._api import (
    CatalogAPI,
    LogisticsAPI,
    OrdersAPI,
)


class VTEX:
    """
    Entrypoint for the VTEX SDK.
    From this class you can access all the APIs on VTEX
    """

    def __init__(
        self: "VTEX",
        account_name: Optional[str] = None,
        app_key: Optional[str] = None,
        app_token: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> None:
        self.account_name = account_name
        self.app_key = app_key
        self.app_token = app_token
        self.environment = environment
        self._api_kwargs = {
            "account_name": account_name,
            "app_key": app_key,
            "app_token": app_token,
            "environment": environment,
        }

    @cached_property
    def catalog(self: "VTEX") -> CatalogAPI:
        return CatalogAPI(**self._api_kwargs)

    @cached_property
    def logistics(self: "VTEX") -> LogisticsAPI:
        return LogisticsAPI(**self._api_kwargs)

    @cached_property
    def orders(self: "VTEX") -> OrdersAPI:
        return OrdersAPI(**self._api_kwargs)
