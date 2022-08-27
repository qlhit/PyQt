import time

from PyQt5.QtCore import *
class update_time(QThread):
    usig = pyqtSignal(int)
    def __init__(self, data_time, parent=None):
        super().__init__(parent)
        self.data_time = data_time
    def run(self):
        for i in range(0,self.data_time):
            self.usig.emit(i)
            time.sleep(1)

