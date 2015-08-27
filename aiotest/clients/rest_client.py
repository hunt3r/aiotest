
import asyncio
from aiohttp import web, ClientSession
import json

class RestClient():

    def __init__(self):
        self.client = ClientSession()

    def close(self):
        self.client.close()

    @asyncio.coroutine
    def post(self, url, headers={}):
        if 'content-type' not in headers:
            headers['content-type'] = 'application/json'
        resp = yield from self.client.post(url, headers=headers)
        data = yield from resp.read()
        yield from resp.release()
        return data.decode('utf-8')

    @asyncio.coroutine
    def get(self, url, headers={}, to_json=False):
        resp = yield from self.client.post(url)
        data = yield from resp.read()
        yield from resp.release()
        if to_json:
            data = json.loads(data.decode('utf-8'))
        return data

    @asyncio.coroutine
    def put(self, url, headers={}):
        resp = yield from self.client.post(url)
        data = yield from resp.read()
        yield from resp.release()
        return json.loads(data)

    @asyncio.coroutine
    def delete(self, url):
        resp = yield from self.client.post(url)
        data = yield from resp.read()
        yield from resp.release()
        return json.loads(data)

    @asyncio.coroutine
    def patch(self, url):
        resp = yield from self.client.post(url)
        data = yield from resp.read()
        yield from resp.release()
        return json.loads(data)

