import time

from PyQt5.QtCore import *
import random
class draw_wavel(QThread):
    finish = pyqtSignal()
    def __init__(self,target,data_time,data_wavelength,data_colu_spectrInt,parent=None):

        super().__init__(parent)
        self.flag = True
        self.temp = target
        self.data_time = data_time
        self.data_wavelength = data_wavelength
        self.data_colu_spectrInt = data_colu_spectrInt
    def run(self):
        for indexWa in range(len(self.data_time)):
            # QMessageBox.information(self,'Info','wavlength vs spectrInt')
            self.temp.plot(self.data_wavelength, self.data_colu_spectrInt[indexWa,], pen='r',clear=True)
            time.sleep(0.5)
        self.finish.emit()
