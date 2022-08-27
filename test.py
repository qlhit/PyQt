#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dell
import sys
import numpy as np
from PyQt5 import QtWidgets
import pyqtgraph as pg
from untitled import Ui_MainWindow
from PyQt5 import QtCore
import os
from avaspec import *

class MyGraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #signal definition
    newdata = pyqtSignal()
    def __init__(self):
        super(MyGraphWindow, self).__init__()
        self.setupUi(self)  # 初始化窗口
        self.p1, self.p2 = self.set_graph_ui()  # 设置绘图窗口
        self.set_graph_ui_tab2()
        self.pt = self.set_graph_ui_tab3()
        self.IntTimeEdt.setText("{:3.1f}".format(5.0))
        self.NumAvgEdt.setText("{0:d}".format(1))
        self.NumMeasEdt.setText("{0:d}".format(1))
        self.StartMeasBtn.setEnabled(True)
        self.VersionBtn.setEnabled(False)
        self.data_time = []
        self.data_wavelength = []
        self.data_spectrInt = []
        self.data_colu_spectrInt = []
        self.label_down = pg.TextItem()
        #绑定响应函数，draw
        self.newdata.connect(self.draw)
        #self.StartMeasBtn.clicked.connect(self.timer_start)
        self.scans = 0
        self.add_file()
    def set_graph_ui_tab3(self):
        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿
        win1 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        win1.setBackground('w')
        # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中
        self.gridLayout_6.addWidget(win1)
        pt = win1.addPlot(title="炉次 VS PCA得分",row=0, col=0)  # 添加第一个绘图窗口
        pt.setLabel('left', text='PCA得分', color='b')  # y轴设置函数
        pt.setLabel('bottom', text='炉次', units='ms', color='b')  # y轴设置函数
        pt.showGrid(x=True, y=True)  # 栅格设置函数
        return pt
    def set_graph_ui_tab2(self):
        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿
        win = pg.GraphicsLayoutWidget(show=True)  # 创建pg layout，可实现数据界面布局自动管理
        win.setBackground('w')
        # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中

        self.gridLayout_4.addWidget(win)
        pc1 = win.addPlot(title="score vs runtime PC1",row=1, col=1)  # 添加第一个绘图窗口
        pc1.setLabel('left', text='score', color='b')  # y轴设置函数
        pc1.setLabel('bottom', text='runtime', units='ms', color='b')  # y轴设置函数
        pc1.showGrid(x=True, y=True)  # 栅格设置函数

        win.nextColumn()
        pc2 = win.addPlot(title="score vs runtime PC2", row=1, col=2)
        pc2.showGrid(x=True, y=True)
        pc2.setLogMode(x=False, y=False)
        pc2.setLabel('left', text='score', color='b')  # y轴设置函数
        pc2.setLabel('bottom', text='runtime', color='b')  # x轴设置函数
        win.nextColumn()
        pc3 = win.addPlot(title="score vs runtime PC3", row=1, col=3)
        pc3.showGrid(x=True, y=True)
        pc3.setLogMode(x=False, y=False)
        pc3.setLabel('left', text='score', color='b')  # y轴设置函数
        pc3.setLabel('bottom', text='runtime', color='b')  # x轴设置函数

        win.nextRow()  # layout换行，采用垂直排列，不添加此行则默认水平排列
        pc4 = win.addPlot(title="intensity vs wavelength PC1", row=2, col=1)
        pc4.showGrid(x=True, y=True)
        pc4.setLogMode(x=False, y=False)
        pc4.setLabel('left', text='intensity', color='b')  # y轴设置函数
        pc4.setLabel('bottom', text='wavelength', color='b')  # x轴设置函数
        win.nextColumn()
        pc5 = win.addPlot(title="intensity vs wavelength PC2", row=2, col=2)
        pc5.showGrid(x=True, y=True)
        pc5.setLogMode(x=False, y=False)
        pc5.setLabel('left', text='intensity', color='b')  # y轴设置函数
        pc5.setLabel('bottom', text='wavelength', color='b')  # x轴设置函数
        win.nextColumn()
        pc6 = win.addPlot(title="intensity vs wavelength PC3", row=2, col=3)
        pc6.showGrid(x=True, y=True)
        pc6.setLogMode(x=False, y=False)
        pc6.setLabel('left', text='intensity', color='b')  # y轴设置函数
        pc6.setLabel('bottom', text='wavelength', color='b')  # x轴设置函数
    def set_graph_ui(self):
        # pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿
        # win = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        # win.setBackground('w')
        # # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中
        # self.gridLayout.addWidget(win)
        # p1 = win.addPlot(title="sin 函数")  # 添加第一个绘图窗口
        # p1.setLabel('left', text='meg', color='#ffffff')  # y轴设置函数
        # p1.showGrid(x=True, y=True)  # 栅格设置函数
        # p1.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
        # p1.setLabel('bottom', text='time', units='s')  # x轴设置函数
        # # p1.addLegend()  # 可选择是否添加legend
        # win.nextRow()  # layout换行，采用垂直排列，不添加此行则默认水平排列
        # p2 = win.addPlot(title="cos 函数")
        # p2.setLabel('left', text='meg', color='b')
        # p2.showGrid(x=True, y=True)
        # p2.setLogMode(x=False, y=False)
        # p2.setLabel('bottom', text='time', units='s')
        # # p2.addLegend()
        # return p1, p2
        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿
        win = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        win.setBackground('w')
        # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中
        self.gridLayout.addWidget(win)
        p1 = win.addPlot(title="Time VS SpectrIntes",row=1, col=0)  # 添加第一个绘图窗口
        p1.setLabel('left', text='SpectrIntes', color='b')  # y轴设置函数
        p1.setLabel('bottom', text='time', units='ms', color='b')  # y轴设置函数
        p1.showGrid(x=True, y=True)  # 栅格设置函数

        win.nextRow()  # layout换行，采用垂直排列，不添加此行则默认水平排列
        p2 = win.addPlot(title="Wavelength VS SpectrIntes", row=2, col=0)
        p2.showGrid(x=True, y=True)
        p2.setLabel('left', text='SpectrIntes', color='b')  # y轴设置函数
        p2.setLabel('bottom', text='wavelength', color='b')  # x轴设置函数
        return p1, p2

    # 启动定时器 时间间隔秒
    def timer_start(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.plot_sin_cos)
        self.timer.start(500)

    #绘图
    def plot_sin_cos(self):
        self.data_spectrInt.append(5)
        print(self.data_spectrInt)
        self.p1.plot(self.data_time[0:self.count], self.data_spectrInt, pen='g', name='Time VS SpectrIntes', clear=True,)
        self.p2.plot(self.data_wavelength[0:self.count],  self.data_spectrInt, pen='g', name='Time VS SpectrIntes', clear=True)
        self.count += 1
        print('count:',self.count)

    #绘图
    def draw(self):
        print('图像绘制开始')
        timestamp = 0
        ret = AVS_GetScopeData(globals.dev_handle)
        timestamp = ret[0]
        globals.spectraldata = ret[1]
        # QMessageBox.information(self,"Info","Received data")
        print('数据', globals.spectraldata)
        #self.plot.update()
        print('start measurement')
        self.StartMeasBtn.setEnabled(False)
        #光谱强度
        self.data_spectrInt = np.frombuffer(globals.spectraldata)
        self.data_spectrInt = self.data_spectrInt[0:np.argwhere(self.data_spectrInt <= 0 )[0,0]]

        self.data_colu_spectrInt = np.insert(self.data_colu_spectrInt, self.scans-1 if self.scans !=2 else len(self.data_colu_spectrInt), self.data_spectrInt,axis=0)
        print('325', self.data_colu_spectrInt.shape)
        if self.scans == 2:
            self.data_colu_spectrInt = np.resize(self.data_colu_spectrInt, (2, int(len(self.data_colu_spectrInt)/2)))
        #扫描结束
        if self.scans == len(self.data_time):
            for indexSI in range(len(self.data_wavelength)):
                self.p1.plot(self.data_time, self.data_colu_spectrInt[:, indexSI], pen=(random.randint(0,200),random.randint(0,200),random.randint(0,200)), name='wavelength VS SpectrIntes', clear=False)
                qApp.processEvents()
            self.p2.plot(self.data_wavelength, self.data_spectrInt, pen='r',name='wavelength VS SpectrIntes', clear=True)
            self.proxy = pg.SignalProxy(self.p2.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
            # 设置跟随鼠标移动的线
            #cross hair
            self.vLine = pg.InfiniteLine(angle=90, movable=False, pen='b')  # angle控制线相对x轴正向的相对夹角
            self.hLine = pg.InfiniteLine(angle=0, movable=False, pen='b')
            self.p2.addItem(self.vLine, ignoreBounds=True)
            self.p2.addItem(self.hLine, ignoreBounds=True)
            self.p2.addItem(self.label_down)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyGraphWindow()
    myWin.show()
    sys.exit(app.exec_())

