from views.article import view_bp
from views.user import view_user
from utils.init_scheduler import InitScheduler
from utils.logger import _logger
from settings import app

"""
此路径下负责所有的初始化 及 监听
"""


@view_bp.listener("before_server_start")
async def setup_connection(app, loop):
    print("开始连接------")
    app.log = _logger
    print("id (app.log) ", id(app.log))

    app.log.info("服务开始启动......")
    # app.scheduler = InitScheduler().apscheduler_init_redis()
    app.scheduler = InitScheduler().apscheduler_init_mongo()
    app.log.info(f"app.scheduler 的 {id(app.scheduler)}")

app.blueprint(view_bp)
app.blueprint(view_user)