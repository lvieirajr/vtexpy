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
from ._config import Config  # type: ignore[attr-defined]
from ._logging import get_logger
from ._types import IterableType, UndefinedType
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
        timeout: Union[float, None, UndefinedType] = UNDEFINED,
        retry_attempts: Union[int, UndefinedType] = UNDEFINED,
        retry_backoff_min: Union[float, UndefinedType] = UNDEFINED,
        retry_backoff_max: Union[float, UndefinedType] = UNDEFINED,
        retry_backoff_exponential: Union[bool, float, UndefinedType] = UNDEFINED,
        retry_statuses: Union[IterableType[int], UndefinedType] = UNDEFINED,
        retry_logs: Union[bool, UndefinedType] = UNDEFINED,
        raise_for_status: Union[bool, UndefinedType] = UNDEFINED,
    ) -> None:
        self._logger = get_logger("client")
        self._config = Config(
            account_name=account_name,
            app_key=app_key,
            app_token=app_token,
            timeout=timeout,
            retry_attempts=retry_attempts,
            retry_backoff_min=retry_backoff_min,
            retry_backoff_max=retry_backoff_max,
            retry_backoff_exponential=retry_backoff_exponential,
            retry_statuses=retry_statuses,
            retry_logs=retry_logs,
            raise_for_status=raise_for_status,
        )

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
