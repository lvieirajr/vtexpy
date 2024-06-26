from dataclasses import asdict, dataclass
from typing import Any, Optional, Type

from httpx import Response

from ._types import JsonType, ResponseItemsType


@dataclass(frozen=True)
class VTEXResponse:
    response: Response
    data: Any
    status: int
    headers: JsonType

    @classmethod
    def from_response(cls: Type["VTEXResponse"], response: Response) -> "VTEXResponse":
        return cls(
            response=response,
            data=response.json(),
            status=response.status_code,
            headers=dict(response.headers.items()),
        )


@dataclass(frozen=True)
class PaginatedResponse(VTEXResponse):
    total: int
    pages: int
    page_size: int
    page: int
    previous_page: Optional[int]
    next_page: Optional[int]
    items: ResponseItemsType

    @classmethod
    def from_vtex_response(
        cls: Type["PaginatedResponse"],
        vtex_response: VTEXResponse,
    ) -> "PaginatedResponse":
        pagination = vtex_response.data["paging"]
        page = pagination["page"]

        return cls(
            **asdict(vtex_response),
            total=pagination["total"],
            pages=pagination["pages"],
            page_size=pagination["perPage"],
            page=page,
            previous_page=page - 1 if page > 1 else None,
            next_page=page + 1 if page < pagination["pages"] else None,
            items=vtex_response.data["items"],
        )
