import os,datetime,shutil
from PyQt5.QtCore import QThread

#删除文件存储时间超过day天数的文件夹
class DelFileByDaysThread(QThread):
    def __init__(self, day):
        super().__init__()
        # self.month = day
        self.curPath='img'
        self.delta = datetime.timedelta(days=day)  # 3个月，按90天算。这里方便测试可以设置成0，也就是把这个文件夹下的所有文件都删除了
        self.now = datetime.datetime.now()

    def delFiles(self):
        dirLs=list(os.walk(self.curPath))  #os.walk遍历指定目录下所有的文件和子目录，返回三元组：(curPath,dirs,files)
        #list列表化后，dirLs[()]里就只有一个元素，这个元素就是三元组
        self.needDel=False
        for d in dirLs:
            if d[0]=='img': #img目录为图片存放根目录，不做操作
                continue
            if d[2]!=[]: #如果目录下有文件 相当于dirls[0][2]
                for file in d[2]:
                    fileName=os.path.join(d[0],file)
                    ctime = datetime.datetime.fromtimestamp(os.path.getctime(fileName))  # 获取文件创建时间
                    if ctime < (self.now - self.delta):  # 若创建于delta天前
                        # os.remove(file)  # 则删掉
                        self.needDel=True
                    else:
                        self.needDel=False

            if os.path.exists(d[0]) and self.needDel:
                print("del directorys:", d[0])
                shutil.rmtree(d[0])
        print("finished del")

    def run(self):
        print("starting del files....")
        self.delFiles()

if __name__=='__main__':
    del3M=DelFileByDaysThread(90)
    del3M.delFiles( )
    print("finished del")