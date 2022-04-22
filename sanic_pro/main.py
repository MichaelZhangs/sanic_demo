from settings import app
from routers.routers_list import view_bp
from utils.init_scheduler import InitScheduler
from config.configs import redis_host, server_port


@view_bp.listener("before_server_start")
async def setup_connection(app, loop):
    print("开始连接------")
    app.scheduler = InitScheduler().apscheduler_init()


app.blueprint(view_bp)
if __name__ == '__main__':
    app.run(host=redis_host, port=server_port)