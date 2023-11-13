from functools import cached_property
from typing import Optional

from ._api import (
    CatalogAPI,
    CustomAPI,
    LogisticsAPI,
    OrdersAPI,
)
from ._config import Config
from ._constants import DEFAULT_ENVIRONMENT, DEFAULT_TIMEOUT


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
        environment: Optional[str] = DEFAULT_ENVIRONMENT,
        timeout: Optional[int] = DEFAULT_TIMEOUT,
        raise_for_status: Optional[bool] = False,
    ) -> None:
        self.config = Config(
            account_name=account_name,
            app_key=app_key,
            app_token=app_token,
            environment=environment,
            timeout=timeout,
            raise_for_status=raise_for_status,
        )

    @cached_property
    def custom(self: "VTEX") -> CustomAPI:
        return CustomAPI(config=self.config)

    @cached_property
    def catalog(self: "VTEX") -> CatalogAPI:
        return CatalogAPI(config=self.config)

    @cached_property
    def logistics(self: "VTEX") -> LogisticsAPI:
        return LogisticsAPI(config=self.config)

    @cached_property
    def orders(self: "VTEX") -> OrdersAPI:
        return OrdersAPI(config=self.config)
