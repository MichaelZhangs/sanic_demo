 # sanic_pro

运行python3 main.py 启动
因看到自己工作中项目 main.py 异常多函数， 自己写了个测试， 分离各类函数。使得main 函数简单。
同样，通过与绑定， 在函数启动 前 把 loger 和 scheduler 函数绑定到app上，实现app.logger, app.scheduler 含有logger, scheduler 的功能，
且全局唯一 ， 为单列模式，避免自己创建单列。
如果出现 如下错误，需要修改redis.py 源码
![image](https://user-images.githubusercontent.com/58901344/164680516-ca37020c-eadc-4d85-86e0-5058d04fd761.png)

找到"D:\python\lib\site-packages\apscheduler\jobstores\redis.py", 按如下修改。即注释掉原来的pipe.zadd 方式
![image](https://user-images.githubusercontent.com/58901344/164681233-5a994c77-bea4-4e68-9cdf-8ebd958642e4.png)

![image](https://user-images.githubusercontent.com/58901344/164684697-a8d28441-a187-48da-b56c-23b0c42d349f.png)
