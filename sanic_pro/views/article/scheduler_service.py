from settings import app
from sanic.views import HTTPMethodView
from sanic.response import json
import threading
import datetime

class Book(HTTPMethodView):

    def send_hello(self, *args):
        app.log.info(f"{args[0]}: welcome you ....")
        print(f"{args[0]}: welcome you ....")


    async def post(self, request):
        data = request.json
        user_id = data.get("user_id")
        t = datetime.datetime.now()
        exe_time = t + datetime.timedelta(seconds=10)
        # print(exe_time)
        # exe_time = datetime.datetime.strptime(str(exe_time).split(".")[0], "%Y-%m-%d %H:%M:%S")
        app.log.debug("post 函数-----")
        app.log.debug(f"地址值。。。。 {id(app.log)}")
        app.log.info(f"app.scheduler 的 {id(app.scheduler)}")
        app.scheduler.add_job(self.send_hello, trigger="date",  next_run_time=exe_time , args=(user_id,), id=user_id, replace_existing=True )

        return json({"ok": 1})

    async def get(self, request):

        data = request.args
        user_id = data.get("user_id")
        t = datetime.datetime.now()
        exe_time = t + datetime.timedelta(seconds=10)
        print("---> ", id(app.log))
        app.log.error(f"开始任务")
        # print(exe_time)
        # exe_time = datetime.datetime.strptime(str(exe_time).split(".")[0], "%Y-%m-%d %H:%M:%S")
        # 基于mongo
        app.log.info(f"app.scheduler 的 {id(app.scheduler)}")
        app.scheduler.add_job(self.send_hello, trigger="date", jobstore="mongo", next_run_time=exe_time,id=user_id, args=(user_id,), replace_existing=True )
        # 基于redis
        # app.scheduler.add_job(self.send_hello, trigger="date", jobstore="redis", next_run_time=exe_time,id=user_id, args=(user_id,), replace_existing=True )

        return json({"status": 200})


