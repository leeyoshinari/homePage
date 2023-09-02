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

async def s1(request):
    return aiohttp_jinja2.render_template('s1.html', request, context=None)
async def s2(request):
    return aiohttp_jinja2.render_template('s2.html', request, context=None)
async def s3(request):
    return aiohttp_jinja2.render_template('s3.html', request, context=None)
async def s4(request):
    return aiohttp_jinja2.render_template('s4.html', request, context=None)
async def s5(request):
    return aiohttp_jinja2.render_template('s5.html', request, context=None)
async def s6(request):
    return aiohttp_jinja2.render_template('s6.html', request, context=None)
async def s7(request):
    return aiohttp_jinja2.render_template('s7.html', request, context=None)
async def s99(request):
    return aiohttp_jinja2.render_template('s99.html', request, context=None)


async def app_server():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    app.router.add_static(f'{context}/static',
                          path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
                          append_version=True)

    app.router.add_route('GET', f'{context}', home)
    app.router.add_route('GET', f'{context}/s1', s1)
    app.router.add_route('GET', f'{context}/s2', s2)
    app.router.add_route('GET', f'{context}/s3', s3)
    app.router.add_route('GET', f'{context}/s4', s4)
    app.router.add_route('GET', f'{context}/s5', s5)
    app.router.add_route('GET', f'{context}/s6', s6)
    app.router.add_route('GET', f'{context}/s7', s7)
    app.router.add_route('GET', f'{context}/s99', s99)
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
