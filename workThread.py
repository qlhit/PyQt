from PyQt5.QtCore import *
class workThread(QThread):

    def __init__(self, target, parent=None):
        super().__init__(parent)
        self.temp = target
    def run(self):
        self.temp.clear()

