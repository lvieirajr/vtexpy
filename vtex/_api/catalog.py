from typing import Any, Union

from .._dto import VTEXListResponse
from .._types import UndefinedType
from .._utils import UNDEFINED, exclude_undefined_values
from .base import BaseAPI


class CatalogAPI(BaseAPI):
    """
    Client for the Catalog API.
    https://developers.vtex.com/docs/api-reference/catalog-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def list_sellers(
        self,
        sales_channel: Union[int, UndefinedType] = UNDEFINED,
        seller_type: Union[int, UndefinedType] = UNDEFINED,
        is_better_scope: Union[bool, UndefinedType] = UNDEFINED,
        **kwargs: Any,
    ) -> VTEXListResponse:
        return VTEXListResponse.factory(
            vtex_response=self._request(
                method="GET",
                environment=self.ENVIRONMENT,
                endpoint="/api/catalog_system/pvt/seller/list",
                params=exclude_undefined_values({
                    "sc": sales_channel,
                    "sellerType": seller_type,
                    "isBetterScope": is_better_scope,
                }),
                config=self._config.with_overrides(**kwargs),
            ),
        )
