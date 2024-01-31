from aiohttp import web
from log import log
from session import get_session
from models.user_models import User, UserMeta


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
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return "pong" text
            "405":
                description: invalid HTTP Method
        """
        session = get_session()
        res = {
            "res": "User registered",
        }
        log.debug("User registered.")
        return web.json_response(res)
