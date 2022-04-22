from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from config.configs import redis_port, redis_host
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class InitScheduler:

    def apscheduler_init(self):
        REDIS = {
            'host': redis_host,
            'port': str(redis_port),
            "db": 15,
            "password": ""

        }

        # 设置任务的存储位置为redis
        jobstores = {
            'redis': RedisJobStore(**REDIS)
        }

        # 设置定时任务运行的线程和进程，可选配置
        executors = {
            'default': ThreadPoolExecutor(10),  # 默认线程数
            'processpool': ProcessPoolExecutor(4)  # 默认进程
        }

        # 实例定时任务对象，用于定时任务的添加，修改，删除等等操作
        # scheduler = BackgroundScheduler(timezone="Asia/Shanghai", jobstores=jobstores, executors=executors)
        scheduler = AsyncIOScheduler(timezone="Asia/Shanghai", jobstores=jobstores, executors=executors)
        scheduler.start()
        return scheduler
