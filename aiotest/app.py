__author__ = 'hunter'

import asyncio
from aiohttp import web
import os
import fnmatch

settings = {
    "port" : 8000
}

def get_features():
    features = {}
    lst = os.listdir("aiotest/features")
    dir = []
    for d in lst:
        s = os.path.abspath("aiotest/features") + os.sep + d
        if os.path.isdir(s) and os.path.exists(s + os.sep + "__init__.py"):
            dir.append(d)
    for d in dir:
        features[d] = __import__("aiotest.features." + d, fromlist = ["*"])
    return features

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    features = get_features()
    for feature in features:
        config = features.get(feature).config
        for path in config:
            routes = config.get(path)
            for method in routes:
                app.router.add_route(method.get('method'), path, method.get('handler'))

    srv = yield from loop.create_server(app.make_handler(),
                                        '127.0.0.1', settings.get("port"))
    print("Server started at http://127.0.0.1:%s" % settings.get("port"))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
