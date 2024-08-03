from typing import Any, Union

from .._constants import (
    LIST_SKU_IDS_MAX_PAGE_SIZE,
    LIST_SKU_IDS_START_PAGE,
    MIN_PAGE_SIZE,
)
from .._dto import VTEXListResponse, VTEXResponse
from .._types import UndefinedType
from .._utils import UNDEFINED, exclude_undefined_values
from .base import BaseAPI


class CatalogAPI(BaseAPI):
    """
    Client for the Catalog API.
    https://developers.vtex.com/docs/api-reference/catalog-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def list_sku_ids(
        self,
        page: int = LIST_SKU_IDS_START_PAGE,
        page_size: int = LIST_SKU_IDS_MAX_PAGE_SIZE,
        **kwargs: Any,
    ) -> VTEXListResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint="/api/catalog_system/pvt/sku/stockkeepingunitids",
            params={
                "page": max(page, LIST_SKU_IDS_START_PAGE),
                "pagesize": max(
                    min(page_size, LIST_SKU_IDS_MAX_PAGE_SIZE),
                    MIN_PAGE_SIZE,
                ),
            },
            config=self._config.with_overrides(**kwargs),
            response_class=VTEXListResponse,
        )

    def get_sku_with_context(self, sku_id: int, **kwargs: Any) -> VTEXResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/catalog_system/pvt/sku/stockkeepingunitbyid/{sku_id}",
            config=self._config.with_overrides(**kwargs),
            response_class=VTEXResponse,
        )

    def list_sellers(
        self,
        sales_channel: Union[int, UndefinedType] = UNDEFINED,
        seller_type: Union[int, UndefinedType] = UNDEFINED,
        is_better_scope: Union[bool, UndefinedType] = UNDEFINED,
        **kwargs: Any,
    ) -> VTEXListResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint="/api/catalog_system/pvt/seller/list",
            params=exclude_undefined_values({
                "sc": sales_channel,
                "sellerType": seller_type,
                "isBetterScope": is_better_scope,
            }),
            config=self._config.with_overrides(**kwargs),
            response_class=VTEXListResponse,
        )
