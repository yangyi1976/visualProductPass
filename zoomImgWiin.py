import sys

from PyQt5.QtWidgets import QWidget, QApplication

from ui_zoomImgWin import Ui_zoomImgWin


class ZoomImgwin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_zoomImgWin()
        self.ui.setupUi(self)
        self.ui.lbZoomImg.setScaledContents(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ZoomImgwin()
    mainWin.show()

    sys.exit(app.exec_())