import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from ui_pramaSetup import Ui_winParamSetup

class ParamSetupWin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_winParamSetup()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint |Qt.WindowStaysOnTopHint)
        self.setAutoFillBackground(True)





if __name__ == "__main__":


    app = QApplication(sys.argv)
    mainWin = ParamSetupWin()
    mainWin.show()

    sys.exit(app.exec_())