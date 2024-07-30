from datetime import datetime
from typing import Any, Union

from .._constants import (
    LIST_ORDERS_MAX_PAGE,
    LIST_ORDERS_MAX_PAGE_SIZE,
    LIST_ORDERS_START_PAGE,
    MIN_PAGE_SIZE,
)
from .._dto import VTEXPaginatedListResponse, VTEXResponse
from .._types import UndefinedType
from .._utils import UNDEFINED, is_undefined, now, start_of_two_years_ago
from .base import BaseAPI


class OrdersAPI(BaseAPI):
    """
    Client for the Orders API.
    https://developers.vtex.com/docs/api-reference/orders-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def list_orders(
        self,
        creation_date_from: Union[datetime, UndefinedType] = UNDEFINED,
        creation_date_to: Union[datetime, UndefinedType] = UNDEFINED,
        order_by: str = "creationDate,desc",
        page: int = LIST_ORDERS_START_PAGE,
        page_size: int = LIST_ORDERS_MAX_PAGE_SIZE,
        **kwargs: Any,
    ) -> VTEXPaginatedListResponse:
        if page > LIST_ORDERS_MAX_PAGE:
            raise ValueError("List Orders endpoint can only return up to page 30")

        params = {
            "orderBy": order_by,
            "page": max(
                min(page, LIST_ORDERS_MAX_PAGE),
                LIST_ORDERS_START_PAGE,
            ),
            "per_page": max(
                min(page_size, LIST_ORDERS_MAX_PAGE_SIZE),
                MIN_PAGE_SIZE,
            ),
        }

        if not is_undefined(creation_date_from) or not is_undefined(creation_date_to):
            if not isinstance(creation_date_from, datetime):
                creation_date_from = start_of_two_years_ago()

            if not isinstance(creation_date_to, datetime):
                creation_date_to = now()

            start = creation_date_from.isoformat(timespec="milliseconds").split("+")[0]
            end = creation_date_to.isoformat(timespec="milliseconds").split("+")[0]

            params["f_creationDate"] = f"creationDate:[{start}Z TO {end}Z]"

        response = VTEXPaginatedListResponse.factory(
            vtex_response=self._request(
                method="GET",
                environment=self.ENVIRONMENT,
                endpoint=f"/api/oms/pvt/orders/",
                params=params,
                config=self._config.with_overrides(**kwargs),
            )
        )

        if isinstance(response.next_page, int) and response.next_page > 30:
            response.next_page = None

        return response


    def get_order(self, order_id: str, **kwargs: Any) -> VTEXResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/oms/pvt/orders/{order_id}",
            config=self._config.with_overrides(**kwargs),
        )
