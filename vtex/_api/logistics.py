from .._response import PaginatedResponse
from .base import BaseAPI


class LogisticsAPI(BaseAPI):
    """
    Client for the Logistics API.
    https://developers.vtex.com/docs/api-reference/logistics-api
    """

    _DEFAULT_ENVIRONMENT = "vtexcommercestable"

    def list_carriers(
        self: "LogisticsAPI",
        *,
        page: int,
        page_size: int = 1000,
    ) -> PaginatedResponse:
        return PaginatedResponse.from_vtex_response(
            vtex_response=self._request(
                method="GET",
                endpoint="api/logistics/pvt/configuration/carriers",
                params={"page": page, "perPage": page_size},
                environment=self._DEFAULT_ENVIRONMENT,
            ),
        )

    def list_docks(
        self: "LogisticsAPI",
        *,
        page: int,
        page_size: int = 1000,
    ) -> PaginatedResponse:
        return PaginatedResponse.from_vtex_response(
            vtex_response=self._request(
                method="GET",
                endpoint="api/logistics/pvt/configuration/carriers",
                params={"page": page, "perPage": page_size},
                environment=self._DEFAULT_ENVIRONMENT,
            ),
        )
