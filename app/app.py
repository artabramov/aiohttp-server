import argparse
from aiohttp import web
from aiohttp.web import middleware
from config import set_config
from uuid import uuid4
from log import get_log


async def hello(request):
    res = {
        "res": "Hello, world",
        "trace_request_uuid": request["trace_request_uuid"],
    }
    tmp = request.app["LOG_FILENAME"]
    request["log"].debug("FUCK!")
    return web.json_response(res)


@middleware
async def middleware1(request, handler):
    # request["trace_request_uuid"] = str(uuid4())
    request["log"] = get_log(request)
    return await handler(request)


parser = argparse.ArgumentParser()
parser.add_argument("--host", help="Set the aiohttp host.", type=str, default="0.0.0.0")
parser.add_argument("--port", help="Set the aiohttp port.", type=int, default=8081)

app = web.Application(middlewares=[middleware1])
set_config(app)
# log = get_log(app)
app.add_routes([web.get("/", hello)])


if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app, host=args.host, port=args.port)
