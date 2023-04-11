from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt

#显示图片原始大小的窗口
class ViewImageWidget(QWidget):
  def __init__(self):
      super(QWidget, self).__init__()
      # 显示控件
      self.setWindowTitle("ROI原始图像")
      self.setWindowFlags(Qt.WindowCloseButtonHint |Qt.WindowStaysOnTopHint)
      self.show_label = QLabel(self)
      self.show_label.setAlignment(Qt.AlignCenter)
      self.show_label.setScaledContents(True)  #让label里的图片内容随着label大小自动缩放


      self.currentImgIdx = 0
      self.currentImg = None

      # 水平布局
      self.layout = QVBoxLayout(self)
      self.layout.addWidget(self.show_label)




if __name__=="__main__":
  import sys
  app = QApplication(sys.argv)

  # 显示控件
  main_widget = ViewImageWidget()
  main_widget.setWindowTitle("ImageViewer")
  main_widget.show()

  # 应用程序运行
  sys.exit(app.exec_())