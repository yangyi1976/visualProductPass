import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

class InfoMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setStyleSheet("background-color: transparent;color:rgb(255,0,0);")
        self.setObjectName("info")
    def warn(self,str):
        return self.warning(self, "警告", str, QMessageBox.No | QMessageBox.Yes)

    def info(self, str):
        return self.information(self, "消息", str,  QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = InfoMessageBox()
    res=mainWin.warn("zhuyizhuyi")

    sys.exit(app.exec_())