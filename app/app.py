from aiohttp import web


async def hello(request):
    res = {"res": "Hello, world"}
    return web.json_response(res)


app = web.Application()
app.add_routes([web.get("/", hello)])


if __name__ == "__main__":
    web.run_app(app, port=80)
