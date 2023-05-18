# wg-easy-api-wrapper
Python module for convenient interaction with the application API [wg-easy](https://github.com/wg-easy/wg-easy)

You can see all the methods in the documentation on GitHub

## Usage
A quick example of creating a client:
```python
async with Server("wg.example.com", 51821, "SuPerSecret_pass") as server:
    await server.create_client("client_name")
```
Or a slightly more complicated way:
```python
async with aiohttp.ClientSession() as session:
    server = Server("wg.example.com", 51821, "SuPerSecret_pass", session)
    await server.login()
    await server.create_client("client_name")
```