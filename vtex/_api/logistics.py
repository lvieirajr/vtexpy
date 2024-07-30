from typing import Any

from .._constants import (
    LIST_CARRIERS_MAX_PAGE_SIZE,
    LIST_CARRIERS_START_PAGE,
    LIST_DOCKS_MAX_PAGE_SIZE,
    LIST_DOCKS_START_PAGE,
)
from .._dto import VTEXPaginatedListResponse, VTEXResponse
from .base import BaseAPI


class LogisticsAPI(BaseAPI):
    """
    Client for the Logistics API.
    https://developers.vtex.com/docs/api-reference/logistics-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def list_carriers(
        self,
        page: int = LIST_CARRIERS_START_PAGE,
        page_size: int = LIST_CARRIERS_MAX_PAGE_SIZE,
        **kwargs: Any,
    ) -> VTEXPaginatedListResponse:
        return VTEXPaginatedListResponse.factory(
            vtex_response=self._request(
                method="GET",
                environment=self.ENVIRONMENT,
                endpoint="/api/logistics/pvt/configuration/carriers",
                params={
                    "page": max(page, LIST_CARRIERS_START_PAGE),
                    "perPage": max(min(page_size, LIST_CARRIERS_MAX_PAGE_SIZE), 1),
                },
                config=self._config.with_overrides(**kwargs),
            ),
        )

    def get_carrier(
        self,
        carrier_id: str,
        **kwargs: Any,
    ) -> VTEXResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/logistics/pvt/configuration/carriers/{carrier_id}",
            config=self._config.with_overrides(**kwargs),
        )

    def list_docks(
        self,
        page: int = LIST_DOCKS_START_PAGE,
        page_size: int = LIST_DOCKS_MAX_PAGE_SIZE,
        **kwargs: Any,
    ) -> VTEXPaginatedListResponse:
        return VTEXPaginatedListResponse.factory(
            vtex_response=self._request(
                method="GET",
                environment=self.ENVIRONMENT,
                endpoint="/api/logistics/pvt/configuration/docks",
                params={
                    "page": max(page, LIST_DOCKS_START_PAGE),
                    "perPage": max(min(page_size, LIST_DOCKS_MAX_PAGE_SIZE), 1),
                },
                config=self._config.with_overrides(**kwargs),
            ),
        )

    def get_dock(self, dock_id: str, **kwargs: Any) -> VTEXResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/logistics/pvt/configuration/docks/{dock_id}",
            config=self._config.with_overrides(**kwargs),
        )
