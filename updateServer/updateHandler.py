import tornado.web #Web框架模块

# 创建请求处理器
# 当处理请求时会进行实例化并调用HTTP请求对应的方法
class UpdateHandler(tornado.web.RequestHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为version.json.
        filename = self.get_argument("filename", 'version.json')
        # write方法将字符串写入HTTP响应
        # self.write("welcome to start update server" )
        file_ext=filename.split(".")[-1]
        if file_ext=="json":
            self.set_header('Content-Type', 'application/json')
        else:
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        buf_size = 4096
        with open( filename, 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                self.write( data)
        self.finish()
