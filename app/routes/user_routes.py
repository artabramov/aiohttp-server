from aiohttp import web
from log import get_log

log = get_log()


class HelloRoute:
    @staticmethod
    async def select(request):
        res = {
            "res": "Hello, world",
        }
        log.debug("Something logged.")
        return web.json_response(res)
