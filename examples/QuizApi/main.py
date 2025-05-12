"""
Quiz API Example Program

This script demonstrates how to use the Quiz API clients implemented using
aiohttp, httpx, and requests libraries.

Clients:
- AiohttpClient
- HttpxClient
- RequestsClient

Requirements:
- aiohttp
- httpx
- requests

Run with:
    python quizapi_example.py [aiohttp|httpx|requests]
"""

import sys
import asyncio

# Import clients
from TaskoraApi import AiohttpClient
from TaskoraApi import HttpxClient
from TaskoraApi import RequestsClient


async def run_aiohttp_example():
    client = AiohttpClient(api_key="your_api_key")
    response = await client.get_random_quiz()
    print("AiohttpClient response:", response)
    await client.close()


async def run_httpx_example():
    client = HttpxClient(api_key="your_api_key")
    response = await client.get_random_quiz()
    print("HttpxClient response:", response)
    await client.close()


def run_requests_example():
    client = RequestsClient(api_key="your_api_key")
    response = client.get_random_quiz()
    print("RequestsClient response:", response)
