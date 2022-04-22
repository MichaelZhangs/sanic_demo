# sanic_python_scheduler_redis
基于apscheduler的redis定时功能任务框架
运行python3 main.py 启动
如果出现 如下错误，需要修改redis.py 源码
![image](https://user-images.githubusercontent.com/58901344/164680516-ca37020c-eadc-4d85-86e0-5058d04fd761.png)

找到"D:\python\lib\site-packages\apscheduler\jobstores\redis.py", 按如下修改
if job.next_run_time:
  # pipe.zadd(self.run_times_key,
  #           {job.id: datetime_to_utc_timestamp(job.next_run_time)})
  pipe.zadd(self.run_times_key, job.id, datetime_to_utc_timestamp(job.next_run_time))
