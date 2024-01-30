from aiohttp import web
from log import log


class UserRoute:
    @staticmethod
    async def register(request):
        """
        ---
        description: This end-point allow to test that service is up.
        tags:
        - Users
        parameters: 
        - name: user_login
          type: string
          in: body
          required: true
          description: Created user object
        - name: first_name
          type: string
          in: body
          required: true
          description: Created user object
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
        log.debug("User registered.")
        return web.json_response(res)
