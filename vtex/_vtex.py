from functools import cached_property
from typing import Union

from ._api import (
    CatalogAPI,
    CustomAPI,
    LogisticsAPI,
    OrdersAPI,
    TransactionsAPI,
)
from ._config import Config


class VTEX:
    """
    Entrypoint for the VTEX SDK.
    From this class you can access all the APIs on VTEX
    """

    def __init__(
        self,
        account_name: Union[str, None] = None,
        app_key: Union[str, None] = None,
        app_token: Union[str, None] = None,
        timeout: Union[int, None] = None,
        retries: Union[int, None] = None,
        raise_for_status: Union[bool, None] = False,
    ) -> None:
        self.config = Config(
            account_name=account_name,
            app_key=app_key,
            app_token=app_token,
            timeout=timeout,
            retries=retries,
            raise_for_status=raise_for_status,
        )

    @cached_property
    def custom(self) -> CustomAPI:
        return CustomAPI(config=self.config)

    @cached_property
    def catalog(self) -> CatalogAPI:
        return CatalogAPI(config=self.config)

    @cached_property
    def logistics(self) -> LogisticsAPI:
        return LogisticsAPI(config=self.config)

    @cached_property
    def orders(self) -> OrdersAPI:
        return OrdersAPI(config=self.config)

    @cached_property
    def transactions(self) -> TransactionsAPI:
        return TransactionsAPI(config=self.config)
