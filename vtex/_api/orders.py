from typing import Any

from .._dto import VTEXResponse
from .base import BaseAPI


class OrdersAPI(BaseAPI):
    """
    Client for the Orders API.
    https://developers.vtex.com/docs/api-reference/orders-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def get_order(self, order_id: str, **kwargs: Any) -> VTEXResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/oms/pvt/orders/{order_id}",
            config=self._config.with_overrides(**kwargs),
        )
