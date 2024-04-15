# wg-easy-api-wrapper
Python module for convenient interaction with the application API [wg-easy](https://github.com/wg-easy/wg-easy)

You can see all the methods in the documentation on [GitHub Pages](https://shandeika.github.io/wg-easy-api-wrapper/)

## Usage
A quick example of creating a client:
```python
import asyncio

from wg_easy_api_wrapper import Server


async def main():
    async with Server("http://wg.example.com:51821", "SuPerSecret_pass") as server:
        await server.create_client("client_name")


asyncio.run(main())
```
Or a slightly more complicated way:
```python
import asyncio

import aiohttp

from wg_easy_api_wrapper import Server


async def main():
    async with aiohttp.ClientSession() as session:
        server = Server("http://wg.example.com:51821", "SuPerSecret_pass", session)
        await server.login()
        await server.create_client("client_name")


asyncio.run(main())
```