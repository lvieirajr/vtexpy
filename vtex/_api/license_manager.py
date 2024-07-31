from typing import Any

from .._dto import VTEXResponse
from .base import BaseAPI


class LicenseManagerAPI(BaseAPI):
    """
    Client for the License Manager API.
    https://developers.vtex.com/docs/api-reference/license-manager-api
    """

    ENVIRONMENT = "vtexcommercestable"

    def get_account(self, **kwargs: Any) -> VTEXResponse:
        return self._request(
            method="GET",
            environment=self.ENVIRONMENT,
            endpoint="/api/vlm/account",
            config=self._config.with_overrides(**kwargs),
            response_class=VTEXResponse,
        )
