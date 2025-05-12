"""
ChatBot API Example Program

Demonstrates usage of:
- AiohttpChatbotAPI
- HttpxChatbotAPI
- RequestsChatbotAPI

Run with:
    python chatbot_example.py [aiohttp|httpx|requests]
"""


from TaskoraApi import AiohttpChatbotAPI
from TaskoraApi import HttpxChatbotAPI
from TaskoraApi import RequestsChatbotAPI


async def run_aiohttp():
    client = AiohttpChatbotAPI(api_key="your_api_key")
    response = await client.chatbot("Hello!")
    print("Bot:", response)
    await client.close()


async def run_httpx():
    client = HttpxChatbotAPI(api_key="your_api_key")
    response = await client.chatbot("Hello!")
    print("Bot:", response)
    await client.close()


def run_requests():
    client = RequestsChatbotAPI(api_key="your_api_key")
    response = client.chatbot("Hello!")
    print("Bot:", response)
