from sanic.views import HTTPMethodView
from sanic.response import json
from settings import app


class GetUser(HTTPMethodView):

    async def get(self, request):

        app.log.info("查询所有用户")
        return json({"status": 200})