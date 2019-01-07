#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging

logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


def index(request):
    logging.info("index is called")
    return web.Response(body='<h1>中文</h1>'.encode("gb2312"), content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    srv = yield from loop.create_server(app.make_handler(), "127.0.0.1", 8080)
    logging.info("server started at http://127.0.0.1:8080")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
