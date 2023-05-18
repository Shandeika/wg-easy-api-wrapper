from datetime import datetime
from typing import TYPE_CHECKING

import aiohttp

time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

if TYPE_CHECKING:
    from .server import Server


class Client:
    def __init__(self,
                 address: str,
                 created_at: str,
                 enabled: bool,
                 uid: str,
                 last_handshake_at: str,
                 name: str,
                 persistent_keepalive: str,
                 public_key: str,
                 transfer_rx: int,
                 transfer_tx: int,
                 updated_at: str,
                 session: aiohttp.ClientSession,
                 server: 'Server', ):
        self._address = address
        self._created_at = datetime.strptime(created_at, time_format)
        self._enabled = bool(enabled)
        self._uid = uid
        self._last_handshake_at = datetime.strptime(last_handshake_at, time_format) if last_handshake_at else None
        self._name = name
        self._persistent_keepalive = persistent_keepalive
        self._public_key = public_key
        self._transfer_rx = transfer_rx
        self._transfer_tx = transfer_tx
        self._updated_at = datetime.strptime(updated_at, time_format)
        self._session = session
        self._server = server

    @classmethod
    def from_json(cls, json, session: aiohttp.ClientSession, server: 'Server'):
        return cls(
            address=json["address"],
            created_at=json["createdAt"],
            enabled=bool(json["enabled"]),
            uid=json["id"],
            last_handshake_at=json["latestHandshakeAt"],
            name=json["name"],
            persistent_keepalive=json["persistentKeepalive"],
            public_key=json["publicKey"],
            transfer_rx=json["transferRx"],
            transfer_tx=json["transferTx"],
            updated_at=json["updatedAt"],
            session=session,
            server=server,
        )

    @property
    def name(self):
        return self._name

    @name.setter
    async def name(self, value):
        await self._session.put(
            self._server.url_builder("/api/wireguard/client/{}/name".format(self._uid)),
            json={"name": value}
        )
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    async def address(self, value):
        await self._session.put(
            self._server.url_builder("/api/wireguard/client/{}/address".format(self._uid)),
            json={"address": value}
        )
        self._address = value

    @property
    def created_at(self):
        return self._created_at

    @property
    def last_handshake_at(self):
        return self._last_handshake_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def enabled(self):
        return self._enabled

    @property
    def uid(self):
        return self._uid

    @property
    def persistent_keepalive(self):
        return self._persistent_keepalive

    @property
    def public_key(self):
        return self._public_key

    @property
    def transfer_rx(self):
        return self._transfer_rx

    @property
    def transfer_tx(self):
        return self._transfer_tx

    async def enable(self):
        if self._enabled:
            raise ValueError("Client is already enabled")
        await self._session.put(
            self._server.url_builder("/api/wireguard/client/{}/enable".format(self._uid)),
            json={"enable": True}
        )
        self._enabled = True

    async def disable(self):
        if not self._enabled:
            raise ValueError("Client is already disabled")
        await self._session.post(
            self._server.url_builder("/api/wireguard/client/{}/disable".format(self._uid)),
        )
        self._enabled = False

    async def get_qr_code(self):
        return await self._session.get(
            self._server.url_builder("/api/wireguard/client/{}/qrcode.svg".format(self._uid))
        )

    async def get_configuration(self):
        config_file = await self._session.get(
            self._server.url_builder("/api/wireguard/client/{}/configuration".format(self._uid))
        )
        # вернуть как текст
        return await config_file.text()
