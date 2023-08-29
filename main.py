#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: leeyoshinari
import os
import asyncio
import traceback
import jinja2
import aiohttp_jinja2
from aiohttp import web

host = '127.0.0.1'
port = 15678
context = '/home'

async def home(request):
    return aiohttp_jinja2.render_template('index.html', request, context={'context': context})


async def app_server():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    app.router.add_static(f'{context}/static',
                          path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
                          append_version=True)

    app.router.add_route('GET', f'{context}', home)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()


def main_server():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app_server())
    loop.run_forever()


if __name__ == '__main__':
    main_server()
