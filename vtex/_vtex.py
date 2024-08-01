from functools import cached_property
from typing import Union

from ._api import (
    CatalogAPI,
    CustomAPI,
    LicenseManagerAPI,
    LogisticsAPI,
    OrdersAPI,
    TransactionsAPI,
)
from ._config import Config
from ._logging import get_logger
from ._types import UndefinedType
from ._utils import UNDEFINED


class VTEX:
    """
    Entrypoint for the VTEX SDK.
    From this class you can access all the APIs on VTEX
    """

    def __init__(
        self,
        account_name: Union[str, UndefinedType] = UNDEFINED,
        app_key: Union[str, UndefinedType] = UNDEFINED,
        app_token: Union[str, UndefinedType] = UNDEFINED,
        timeout: Union[float, int, None, UndefinedType] = UNDEFINED,
        retries: Union[int, UndefinedType] = UNDEFINED,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> None:
        self._config = Config(
            account_name=account_name,
            app_key=app_key,
            app_token=app_token,
            timeout=timeout,
            retries=retries,
            raise_for_status=raise_for_status,
        )
        self._logger = get_logger("client")

    @cached_property
    def custom(self) -> CustomAPI:
        return CustomAPI(config=self._config, logger=self._logger)

    @cached_property
    def catalog(self) -> CatalogAPI:
        return CatalogAPI(config=self._config, logger=self._logger)

    @cached_property
    def license_manager(self) -> LicenseManagerAPI:
        return LicenseManagerAPI(config=self._config, logger=self._logger)

    @cached_property
    def logistics(self) -> LogisticsAPI:
        return LogisticsAPI(config=self._config, logger=self._logger)

    @cached_property
    def orders(self) -> OrdersAPI:
        return OrdersAPI(config=self._config, logger=self._logger)

    @cached_property
    def transactions(self) -> TransactionsAPI:
        return TransactionsAPI(config=self._config, logger=self._logger)
