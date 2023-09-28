#! /usr/bin/python
# encoding:utf-8

# 导入Tornado模块
import tornado.ioloop #核心IO循环模块
import tornado.httpserver #异步非阻塞HTTP服务器模块
import tornado.web #Web框架模块
import tornado.options #解析终端参数模块

#从终端模块中导出define模块用于读取参数，导出options模块用于设置默认参数
from tornado.options import define, options
from updateHandler import UpdateHandler
from get_host_ip import host_ip
# 定义端口用于指定HTTP服务监听的端口
define("port", type=int, default=8090, help="run on the given port")

# 创建路由表
urls = [(r"/version.json", UpdateHandler),]

# 定义服务器
def serv_main():
    # 解析命令行参数
    tornado.options.parse_command_line()
    # 创建应用实例
    app = tornado.web.Application(urls)
    # 监听端口
    app.listen(options.port)

    print('server is running:%s:%s' %(host_ip(),options.port))
    # 创建IOLoop实例并启动
    tornado.ioloop.IOLoop.current().start()

# 应用运行入口，解析命令行参数
if __name__ == "__main__":
    # 启动服务器
    serv_main()
