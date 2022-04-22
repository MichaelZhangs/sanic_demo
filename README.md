 # sanic_pro

基于apscheduler的redis 与 mongo的定时功能任务框架
运行python3 main.py 启动
如果出现 如下错误，需要修改redis.py 源码
![image](https://user-images.githubusercontent.com/58901344/164680516-ca37020c-eadc-4d85-86e0-5058d04fd761.png)

找到"D:\python\lib\site-packages\apscheduler\jobstores\redis.py", 按如下修改。即注释掉原来的pipe.zadd 方式
![image](https://user-images.githubusercontent.com/58901344/164681233-5a994c77-bea4-4e68-9cdf-8ebd958642e4.png)

![image](https://user-images.githubusercontent.com/58901344/164684697-a8d28441-a187-48da-b56c-23b0c42d349f.png)
