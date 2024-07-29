from dataclasses import asdict, dataclass
from typing import Dict, Sequence, Union

from httpx import Response

from ._types import JSONType
from ._utils import to_snake_case


@dataclass(frozen=True)
class VTEXResponse:
    response: Response
    data: JSONType
    status: int
    headers: Dict[str, str]

    @classmethod
    def from_response(cls, response: Response) -> "VTEXResponse":
        return cls(
            response=response,
            data=to_snake_case(response.json()),
            status=int(response.status_code),
            headers=dict(response.headers.items()),
        )


@dataclass(frozen=True)
class PaginatedResponse(VTEXResponse):
    total: int
    pages: int
    page_size: int
    page: int
    previous_page: Union[int, None]
    next_page: Union[int, None]
    items: Sequence[JSONType]

    @classmethod
    def from_vtex_response(cls, vtex_response: VTEXResponse) -> "PaginatedResponse":
        pagination = vtex_response.data["paging"]
        page = pagination["page"]

        return cls(
            **asdict(vtex_response),
            total=pagination["total"],
            pages=pagination["pages"],
            page_size=pagination["per_page"],
            page=page,
            previous_page=page - 1 if page > 1 else None,
            next_page=page + 1 if page < pagination["pages"] else None,
            items=vtex_response.data["items"],
        )
