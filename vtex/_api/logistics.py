from typing import Any

from .._constants import DEFAULT_ENVIRONMENT
from .._response import PaginatedResponse, VTEXResponse
from .base import BaseAPI


class LogisticsAPI(BaseAPI):
    """
    Client for the Logistics API.
    https://developers.vtex.com/docs/api-reference/logistics-api
    """

    ENVIRONMENT = DEFAULT_ENVIRONMENT

    def list_carriers(
        self: "LogisticsAPI",
        page: int = 1,
        page_size: int = 1000,
        **kwargs: Any,
    ) -> PaginatedResponse:
        return PaginatedResponse.from_vtex_response(
            vtex_response=self._request(
                method="GET",
                endpoint="api/logistics/pvt/configuration/carriers",
                params={"page": page, "perPage": page_size},
                config=self._config.with_overrides(
                    **kwargs,
                    environment=self.ENVIRONMENT,
                ),
            ),
        )

    def get_carrier(
        self: "LogisticsAPI",
        carrier_id: str,
        **kwargs: Any,
    ) -> VTEXResponse:
        return self._request(
            method="GET",
            endpoint=f"api/logistics/pvt/configuration/carriers/{carrier_id}",
            config=self._config.with_overrides(
                **kwargs,
                environment=self.ENVIRONMENT,
            ),
        )

    def list_docks(
        self: "LogisticsAPI",
        page: int = 1,
        page_size: int = 1000,
        **kwargs: Any,
    ) -> PaginatedResponse:
        return PaginatedResponse.from_vtex_response(
            vtex_response=self._request(
                method="GET",
                endpoint="api/logistics/pvt/configuration/docks",
                params={"page": page, "perPage": page_size},
                config=self._config.with_overrides(
                    **kwargs,
                    environment=self.ENVIRONMENT,
                ),
            ),
        )

    def get_dock(self: "LogisticsAPI", dock_id: str, **kwargs: Any) -> VTEXResponse:
        return self._request(
            method="GET",
            endpoint=f"api/logistics/pvt/configuration/docks/{dock_id}",
            config=self._config.with_overrides(
                **kwargs,
                environment=self.ENVIRONMENT,
            ),
        )
