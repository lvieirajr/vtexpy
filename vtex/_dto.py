from dataclasses import asdict, dataclass
from json import JSONDecodeError
from typing import Dict, Sequence, Union

from httpx import Request, Response

from ._types import JSONType
from ._utils import to_snake_case_deep


@dataclass(frozen=True)
class VTEXRequest:
    request: Request
    method: str
    url: str
    headers: Dict[str, str]

    @classmethod
    def factory(cls, request: Request) -> "VTEXRequest":
        return cls(
            request=request,
            method=str(request.method).upper(),
            url=str(request.url),
            headers=request.headers,
        )


@dataclass(frozen=True)
class VTEXResponse:
    request: VTEXRequest
    response: Response
    data: JSONType
    status: int
    headers: Dict[str, str]

    @classmethod
    def factory(cls, response: Response) -> "VTEXResponse":
        try:
            data = response.json(strict=False)
        except JSONDecodeError:
            data = response.text

        return cls(
            request=VTEXRequest.factory(response.request),
            response=response,
            data=to_snake_case_deep(data),
            status=int(response.status_code),
            headers=response.headers,
        )


@dataclass(frozen=True)
class VTEXListResponse(VTEXResponse):
    items: Sequence[JSONType]

    @classmethod
    def factory(cls, vtex_response: VTEXResponse) -> "VTEXListResponse":
        data = vtex_response.data

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict) and isinstance(data.get("items"), list):
            items = data["items"]
        else:
            raise ValueError(f"Not a valid list response: {data}")

        return cls(**asdict(vtex_response), items=items)


@dataclass(frozen=True)
class VTEXPagination:
    total: int
    pages: int
    page_size: int
    page: int
    previous_page: Union[int, None]
    next_page: Union[int, None]

    @classmethod
    def factory(cls, vtex_response: VTEXResponse) -> "VTEXPagination":
        data = vtex_response.data

        if isinstance(data, dict) and data.get("paging"):
            pagination = data["paging"]
        else:
            raise ValueError(f"Not a valid paginated list response: {data}")

        return cls(
            total=pagination["total"],
            pages=pagination["pages"],
            page_size=pagination["per_page"],
            page=pagination["page"],
            previous_page=pagination["page"] - 1 if pagination["page"] > 1 else None,
            next_page=(
                pagination["page"] + 1
                if pagination["page"] < pagination["pages"]
                else None
            ),
        )


@dataclass(frozen=True)
class VTEXPaginatedListResponse(VTEXListResponse, VTEXPagination):
    @classmethod
    def factory(cls, vtex_response: VTEXResponse) -> "VTEXPaginatedListResponse":
        return cls(
            **asdict(VTEXListResponse.factory(vtex_response)),
            **asdict(VTEXPagination.factory(vtex_response)),
        )


@dataclass(frozen=True)
class VTEXScroll:
    token: Union[str, None]

    @classmethod
    def factory(cls, vtex_response: VTEXResponse) -> "VTEXScroll":
        return cls(token=None)


@dataclass(frozen=True)
class VTEXScrollListResponse(VTEXListResponse, VTEXScroll):
    @classmethod
    def factory(cls, vtex_response: VTEXResponse) -> "VTEXScrollListResponse":
        return cls(
            **asdict(VTEXListResponse.factory(vtex_response)),
            **asdict(VTEXScroll.factory(vtex_response)),
        )
