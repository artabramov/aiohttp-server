import argparse
from aiohttp import web
from aiohttp.web import middleware
from config import  get_config
from uuid import uuid4
import time
import os
from routes.hello_routes import HelloRoute
from context import ctx
from log import log
from aiohttp_swagger import setup_swagger

config = get_config()


@middleware
async def before_request(request, handler):
    ctx.trace_request_uuid = str(uuid4())
    ctx.pid = os.getpid()
    ctx.request_start_time = time.time()
    log.debug("Request received, method=%s, url=%s, headers=%s." % (
        request.method, str(request.url), str(request.headers)))
    return await handler(request)


@middleware
async def after_request(request, handler):
    response = await handler(request)
    request_elapsed_time = time.time() - ctx.request_start_time
    log.debug("Response sent, request_elapsed_time=%s, status=%s, headers=%s, body=%s." % (
        request_elapsed_time, response.status, str(response.headers), response.body.decode("utf-8")))
    return response


parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Set the aiohttp host.", type=str, default="0.0.0.0")
parser.add_argument("--port", help="Set the aiohttp port.", type=int, default=8081)

app = web.Application(middlewares=[before_request, after_request])
app.add_routes([web.get("/api/v1/", HelloRoute.select)])
setup_swagger(app, swagger_url="/apidocs")


if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app, host=args.host, port=args.port)
