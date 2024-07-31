from dataclasses import asdict, dataclass
from json import JSONDecodeError
from typing import Dict, Sequence, TypeVar, Union

from httpx import Request, Response

from ._types import JSONType
from ._utils import to_snake_case_deep

VTEXResponseType = TypeVar("VTEXResponseType", bound="VTEXResponse", covariant=True)


@dataclass
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
            headers=dict(request.headers),
        )


@dataclass
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
            headers=dict(response.headers),
        )


@dataclass
class VTEXListResponse(VTEXResponse):
    items: Sequence[JSONType]

    @classmethod
    def factory(cls, response: Response) -> "VTEXListResponse":
        vtex_response = VTEXResponse.factory(response)
        data = vtex_response.data

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict) and isinstance(data.get("list"), list):
            items = data["list"]
        elif isinstance(data, dict) and isinstance(data.get("items"), list):
            items = data["items"]
        else:
            raise ValueError(f"Not a valid list response: {data}")

        return cls(**asdict(vtex_response), items=items)


@dataclass
class VTEXPagination:
    total: int
    pages: int
    page_size: int
    page: int
    previous_page: Union[int, None]
    next_page: Union[int, None]

    @classmethod
    def factory(cls, vtex_list_response: VTEXListResponse) -> "VTEXPagination":
        data = vtex_list_response.data

        if isinstance(data, dict) and data.get("paging"):
            pagination = data["paging"]
        else:
            raise ValueError(f"Not a valid paginated list response: {data}")

        total = pagination.get("total")
        pages = pagination.get("pages")
        page_size = pagination.get("per_page")
        page = pagination.get("page") or pagination.get("current_page")

        return cls(
            total=total,
            pages=pages,
            page_size=page_size,
            page=page,
            previous_page=page - 1 if page > 1 else None,
            next_page=page + 1 if page < pages else None,
        )


@dataclass
class VTEXPaginatedListResponse(VTEXListResponse):
    pagination: VTEXPagination

    @classmethod
    def factory(cls, response: Response) -> "VTEXPaginatedListResponse":
        vtex_list_response = VTEXListResponse.factory(response)

        return cls(
            **asdict(vtex_list_response),
            pagination=VTEXPagination.factory(vtex_list_response),
        )


@dataclass
class VTEXScroll:
    token: Union[str, None]

    @classmethod
    def factory(cls, vtex_list_response: VTEXListResponse) -> "VTEXScroll":
        return cls(token=None)


@dataclass
class VTEXScrollListResponse(VTEXListResponse):
    scroll: VTEXScroll

    @classmethod
    def factory(cls, response: Response) -> "VTEXScrollListResponse":
        vtex_list_response = VTEXListResponse.factory(response)

        return cls(
            **asdict(vtex_list_response),
            scroll=VTEXScroll.factory(vtex_list_response),
        )
