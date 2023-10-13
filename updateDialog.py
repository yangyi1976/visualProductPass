import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui_updateWindow import  Ui_updateDlg


class UpdateDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui=Ui_updateDlg()
        self.ui.setupUi(self)
        self.setWindowTitle("废票信息可视化传递系统升级")
        QApplication.processEvents()


if __name__=="__main__":
    app=QApplication(sys.argv)
    updateDlg=UpdateDlg()
    updateDlg.show()
    sys.exit(app.exec_())