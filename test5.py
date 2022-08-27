import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self,):
        super(QWidget,self).__init__()
        self.number = 0
        w = QWidget(self)
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(250, 1000)
        for filename in range(20):
            self.MapButton = QPushButton(self.topFiller)
            self.MapButton.setText(str(filename))
            self.MapButton.move(10,filename*40)
        ##创建一个滚动条
        self.scroll = QScrollArea(self)
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)

        self.resize(300, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
