# Home

Модуль `wg-easy-api-wrapper` предоставляет простой интерфейс для API [wg-easy](https://github.com/wg-easy/wg-easy). Примеры использования и все доступные методы ниже:

## Получение экземпляра Server
<tabs>
<tab title="С помощью with">

```Python
from wg_easy_api_wrapper import Server


async def main():
    async with Server("wg.example.com", 51821, "SuPerSecret_pass") as server:
        await server.create_client("client_name")

```
</tab>

<tab title="Без помощи with">

```Python
import aiohttp

from wg_easy_api_wrapper import Server


async def main():
    async with aiohttp.ClientSession() as session:
        server = Server("wg.example.com", 51821, "SuPerSecret_pass", session)
        await server.login()
        await server.create_client("client_name")

```
</tab>
</tabs>

Все методы и атрибуты [экземпляра Server описаны на странице](Server.md). Документация [экземпляра Client доступна тут](Client.md).
