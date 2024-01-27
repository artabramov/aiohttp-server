import argparse
from aiohttp import web
from aiohttp.web import middleware
from config import  get_config
from uuid import uuid4
from context import set_context_var, get_context_var
from log import get_log
import time
import os


async def hello(request):
    res = {
        "res": "Hello, world",
    }
    log.debug("Something logged.")
    return web.json_response(res)


@middleware
async def before_request(request, handler):
    set_context_var("trace_request_uuid", str(uuid4()))
    set_context_var("pid", os.getpid())
    set_context_var("request_start_time", time.time())
    log.debug("Request received, method=%s, url=%s, headers=%s." % (
        request.method, str(request.url), str(request.headers)))
    return await handler(request)


@middleware
async def after_request(request, handler):
    response = await handler(request)
    request_elapsed_time = time.time() - get_context_var("request_start_time")
    log.debug("Response sent, request_elapsed_time=%s, status=%s, headers=%s, body=%s." % (
        request_elapsed_time, response.status, str(response.headers), response.body.decode("utf-8")))
    return response


parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Set the aiohttp host.", type=str, default="0.0.0.0")
parser.add_argument("--port", help="Set the aiohttp port.", type=int, default=8081)

config = get_config()
log = get_log()
app = web.Application(middlewares=[before_request, after_request])
app.add_routes([web.get("/", hello)])


if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app, host=args.host, port=args.port)
