import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, Optional

from pythonit_toolkit.pastaporto.test import (
    fake_pastaporto_token_for_user,
    fake_service_to_service_token,
)
from pythonit_toolkit.starlette_backend.pastaporto_backend import PASTAPORTO_X_HEADER
from ward import fixture

from pythonit_toolkit.headers import SERVICE_JWT_HEADER
from .test_client import testclient

logger = logging.getLogger(__name__)


@dataclass
class Response:
    errors: Optional[Dict[str, Any]]
    data: Optional[Dict[str, Any]]


class GraphQLClient:
    def __init__(
        self, client,
        *,
        pastaporto_secret: Optional[str] = None,
        service_to_service_secret: Optional[str] = None,
        admin_endpoint: bool = False,
        internal_api_endpoint: bool = False
    ):
        self._client = client
        self._pastaporto_secret = pastaporto_secret
        self._service_to_service_secret = service_to_service_secret
        self.pastaporto_token = None
        self.service_to_service_token = None

        if internal_api_endpoint:
            self.endpoint = "/internal-api"
        elif admin_endpoint:
            self.endpoint = "/admin-api"
        else:
            self.endpoint = "/graphql"

    async def query(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        body = {"query": query}
        headers = headers or {}

        if variables:
            body["variables"] = variables

        if self.pastaporto_token:
            headers[PASTAPORTO_X_HEADER] = self.pastaporto_token

        if self.service_to_service_token:
            headers[SERVICE_JWT_HEADER] = self.service_to_service_token

        resp = await self._client.post(self.endpoint, json=body, headers=headers)
        data = json.loads(resp.content.decode())
        return Response(errors=data.get("errors"), data=data.get("data"))

    def force_login(self, user):
        self.pastaporto_token = fake_pastaporto_token_for_user(
            {"id": user.id, "email": user.email},
            str(self._pastaporto_secret),
            staff=user.is_staff,
        )

    def force_service_login(self, key: Optional[str] = None):
        self.service_to_service_token = fake_service_to_service_token(
            str(key or self._service_to_service_secret), issuer="gateway", audience="users-service"
        )


@fixture()
async def graphql_client(testclient=testclient):
    async with testclient:
        yield GraphQLClient(testclient)


@fixture()
async def admin_graphql_client(testclient=testclient):
    async with testclient:
        yield GraphQLClient(testclient, admin_endpoint=True)


@fixture()
async def internalapi_graphql_client(testclient=testclient):
    async with testclient:
        yield GraphQLClient(testclient, internal_api_endpoint=True)
