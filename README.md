# sanic_python_scheduler_redis
基于apscheduler的redis定时功能任务框架
运行python3 main.py 启动
如果出现 如下错误，需要修改redis.py 源码
![image](https://user-images.githubusercontent.com/58901344/164680516-ca37020c-eadc-4d85-86e0-5058d04fd761.png)
  File "D:\python\lib\site-packages\apscheduler\jobstores\redis.py", line 88, in add_job
    {job.id: datetime_to_utc_timestamp(job.next_run_time)})
  File "D:\python\lib\site-packages\redis\client.py", line 2315, in zadd
    raise RedisError("ZADD requires an equal number of "
redis.exceptions.RedisError: ZADD requires an equal number of values and scores
找到大约86行, 按如下修改
            if job.next_run_time:
                # pipe.zadd(self.run_times_key,
                #           {job.id: datetime_to_utc_timestamp(job.next_run_time)})
                pipe.zadd(self.run_times_key, job.id, datetime_to_utc_timestamp(job.next_run_time))
