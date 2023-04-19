
import os,datetime
from PyQt5.QtCore import QThread


class Del3MFileThread(QThread):



    def __init__(self, t):
        super().__init__()
        self.month = t
        self.curPath='img'
        self.delta = datetime.timedelta(days=1)  # 3个月，按90天算。这里方便测试可以设置成0，也就是把这个文件夹下的所有文件都删除了
        self.now = datetime.datetime.now()


    def delFiles(self):
        dirLs=list(os.walk(self.curPath))  #os.walk便利指定目录下所有的文件和子目录，返回三元组：(curPath,dirs,files)
        for d in dirLs:
            os.chdir(d[0]) #进入子目录
            if d[2]!=[]: #如果目录下有文件 相当于dirls[0][2]
                for file in d[2]:
                    ctime = datetime.datetime.fromtimestamp(os.path.getctime(file))  # 获取文件创建时间
                    # print(ctime)
                    if ctime < (self.now - self.delta):  # 若创建于delta天前
                        os.remove(file)  # 则删掉



