import argparse
from aiohttp import web


async def hello(request):
    res = {
        "res": "Hello, world",
    }    
    return web.json_response(res)


app = web.Application()
app.add_routes([web.get("/", hello)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Set the IP address on which the aiohttp server will work.", type=str, default="0.0.0.0")
    parser.add_argument("--port", help="Set the port on which the aiohttp server will work.", type=int, default=8081)
    args = parser.parse_args()
    web.run_app(app, host=args.host, port=args.port)
