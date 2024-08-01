from typing import Any

from .._dto import VTEXListResponse
from .base import BaseAPI


class TransactionsAPI(BaseAPI):
    """
    Client for the Transactions API.
    This is not in the VTEX API documentation.
    """

    ENVIRONMENT = "vtexpayments"

    def list_transaction_interactions(
        self,
        transaction_id: str,
        **kwargs: Any,
    ) -> VTEXListResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint=f"/api/pvt/transactions/{transaction_id}/interactions/",
            config=self._config.with_overrides(**kwargs),
            response_class=VTEXListResponse,
        )
