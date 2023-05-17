import aiohttp
from .client import Client


class Server:
    def __init__(self, host: str, port: int, password: str, session: aiohttp.ClientSession = None):
        self.host = host
        self.port = port
        self._password = password
        self._session = session
        self.clients = []

    def url_builder(self, path: str) -> str:
        return f"http://{self.host}:{self.port}{path}"

    def __enter__(self):
        if self._session is None:
            self._session = aiohttp.ClientSession()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    async def login(self):
        # POST to /api/session
        await self._session.post(self.url_builder("/api/session"), json={"password": self._password})
        session = await self.get_session()
        return session

    async def logout(self) -> None:
        # DELETE to /api/session
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




