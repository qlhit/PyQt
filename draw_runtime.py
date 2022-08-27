import threading
import time

from PyQt5.QtCore import *
import random

from PyQt5.QtWidgets import qApp

class draw_runtime(QThread):
    finish = pyqtSignal()
    def __init__(self, target,data_time,data_wavelength,data_colu_spectrInt, parent=None):
        super().__init__(parent)
        self.flag = True
        self.temp = target
        self.data_time = data_time
        self.data_wavelength = data_wavelength
        self.data_colu_spectrInt = data_colu_spectrInt
    def run(self):
        self.temp.clear()
        len(self.data_wavelength)
        for indexSI in range(10):
            # QMessageBox.information(self,'Info','绘制time vs spectrInt')
            self.temp.plot(self.data_time, self.data_colu_spectrInt[:, indexSI], pen=(random.randint(0,200),random.randint(0,200),random.randint(0,200)), clear=False)
        self.finish.emit()
