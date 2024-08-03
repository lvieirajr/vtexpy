from typing import Any, Iterable, Union

from .._constants import (
    MIN_PAGE_SIZE,
    SEARCH_DOCUMENTS_MAX_PAGE_SIZE,
    SEARCH_DOCUMENTS_START_PAGE,
)
from .._dto import VTEXPaginatedListResponse
from .._types import IterableType, OrderingDirectionType, UndefinedType
from .._utils import UNDEFINED, exclude_undefined_values, is_undefined
from .base import BaseAPI


class MasterDataAPI(BaseAPI):
    """
    Client for the Master Data API.
    https://developers.vtex.com/docs/api-reference/master-data-api-v2
    """

    ENVIRONMENT = "vtexcommercestable"

    def search_documents(
        self,
        entity_name: str,
        where: Union[str, UndefinedType] = UNDEFINED,
        fields: Union[IterableType[str], str, UndefinedType] = UNDEFINED,
        order_by_field: str = "id",
        order_by_direction: OrderingDirectionType = "DESC",
        page: int = SEARCH_DOCUMENTS_START_PAGE,
        page_size: int = SEARCH_DOCUMENTS_MAX_PAGE_SIZE,
        **kwargs: Any,
    ) -> VTEXPaginatedListResponse:
        params = {
            "_where": where,
            "_sort": f"{order_by_field} {order_by_direction.upper()}",
        }

        if is_undefined(fields):
            params["_fields"] = "all"
        elif not isinstance(fields, str) and isinstance(fields, Iterable):
            params["_fields"] = ",".join(fields)
        else:
            params["_fields"] = fields

        page = max(page, SEARCH_DOCUMENTS_START_PAGE)
        page_size = max(
            min(page_size, SEARCH_DOCUMENTS_MAX_PAGE_SIZE),
            MIN_PAGE_SIZE,
        )

        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/dataentities/{entity_name}/search",
            params=exclude_undefined_values(params),
            headers={
                "REST-Range": f"resources={(page - 1) * page_size}-{page * page_size}",
            },
            config=self._config.with_overrides(**kwargs),
            response_class=VTEXPaginatedListResponse,
        )
