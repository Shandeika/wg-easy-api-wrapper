import aiohttp

from .client import Client
from .errors import AlreadyLoggedInError


class Server:
    def __init__(self, host: str, port: int, password: str, session: aiohttp.ClientSession = None):
        self.host = host
        self.port = port
        self._password = password
        self._session = aiohttp.ClientSession() if session is None else session

    async def is_logged_in(self):
        session = await self.get_session()
        json_response = await session.json()
        return json_response["authenticated"]

    def url_builder(self, path: str) -> str:
        return f"http://{self.host}:{self.port}{path}"

    async def __aenter__(self):
        await self.login()
        return self

    async def __aexit__(self, exc_type, exc, exc_tb):
        if await self.is_logged_in():
            await self.logout()
        await self._session.close()
        if exc:
            raise exc

    async def login(self):
        if await self.is_logged_in():
            raise AlreadyLoggedInError("You are already logged in")
        await self._session.post(self.url_builder("/api/session"), json={"password": self._password})
        session = await self.get_session()
        return session

    async def logout(self) -> None:
        if not await self.is_logged_in():
            raise AlreadyLoggedInError("You are not logged in")
        await self._session.delete(self.url_builder("/api/session"))

    async def get_session(self):
        # GET to /api/session
        answer = await self._session.get(self.url_builder("/api/session"))
        return answer

    async def get_clients(self):
        # GET to /api/clients
        answer = await self._session.get(self.url_builder("/api/wireguard/client"))
        return [Client.from_json(client, self._session, self) for client in await answer.json()]

    async def remove_client(self, uid: str):
        # DELETE to /api/clients/{list_id}
        await self._session.delete(self.url_builder("/api/wireguard/client/{}".format(uid)))

    async def create_client(self, name: str):
        await self._session.post(
            self.url_builder("/api/wireguard/client"),
            json={"name": name},
        )

    async def get_client(self, uid: str):
        for client in await self.get_clients():
            if client.uid == uid:
                return client
        return None
