__author__ = 'hunter'
import asyncio
from aiotest.clients.rest_client import RestClient
from aiohttp import web


@asyncio.coroutine
def handler(request):
    # name = request.match_info.get('name', "Anonymous")
    client = RestClient()
    text = yield from client.get("http://www.freepeople.com/")
    client.close()
    return web.Response(body=text)

config = {
    "/" : [
        {
            "method" : "GET",
            "handler": handler
        }
    ]
}
