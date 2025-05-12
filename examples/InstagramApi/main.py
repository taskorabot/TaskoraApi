"""
Instagram API Example Program

Demonstrates usage of Instagram API clients implemented with aiohttp, httpx, and requests.

Clients:
- AiohttpClient
- HttpxClient
- RequestsClient

Run with:
    python instagramapi_example.py [aiohttp|httpx|requests]
"""


from TaskoraApi import AiohttpInstagramAPI
from TaskoraApi import HttpxInstagramAPI
from TaskoraApi import RequestsInstagramAPI


async def run_aiohttp_example():
    client = AiohttpInstagramAPI(api_key="your_api_key")
    response = await client.get_profile("instagram_username")
    print("AiohttpClient response:", response)
    await client.close()


async def run_httpx_example():
    client = HttpxInstagramAPI(api_key="your_api_key")
    response = await client.get_profile("instagram_username")
    print("HttpxClient response:", response)
    await client.close()


def run_requests_example():
    client = RequestsInstagramAPI(api_key="your_api_key")
    response = client.get_profile("instagram_username")
    print("RequestsClient response:", response)

