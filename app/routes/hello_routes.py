from aiohttp import web
from log import log


class HelloRoute:
    @staticmethod
    async def select(request):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - Hello routes
        parameters: 
        - in: query
        name: var
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return "pong" text
            "405":
                description: invalid HTTP Method
        """
        res = {
            "res": "Hello, world",
        }
        log.debug("Something logged.")
        return web.json_response(res)
