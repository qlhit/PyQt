﻿#!/usr/bin/env python3
import os
import platform
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import pca
from avaspec import *
import numpy as np
import time
import globals
import form11
import pyqtgraph as pg
import pandas as pd
import threading

class MainWindow(QMainWindow, form11.Ui_MainWindow):
    #signal definition
    newdata = pyqtSignal()
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)  # 初始化窗口
        self.p1, self.p2 = self.set_graph_ui_tab()  # 设置绘图窗口
        self.pc1,self.pc2,self.pc3,self.pc4,self.pc5,self.pc6= self.set_graph_ui_tab2()
        self.pt = self.set_graph_ui_tab3()
        self.StartMeasBtn.setEnabled(True)
        self.VersionBtn.setEnabled(False)
        self.data_time = []
        self.data_wavelength = []
        self.data_spectrInt = []
        self.data_colu_spectrInt = []
        self.label_down = pg.TextItem()
#       self.OpenCommBtn.clicked.connect(self.on_OpenCommBtn_clicked)
#       do not use explicit connect together with the on_ notation, or you will get
#       two signals instead of one!
        #绑定响应函数，draw
        self.newdata.connect(self.draw)
        #self.StartMeasBtn.clicked.connect(self.timer_start)
        self.scans = 0
        self.add_file()


    def set_graph_ui_tab3(self):
        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿
        win1 = pg.GraphicsLayoutWidget(show=True)  # 创建pg layout，可实现数据界面布局自动管理
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
        return pc1,pc2,pc3,pc4,pc5,pc6
    def set_graph_ui_tab(self):
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

    @pyqtSlot()
#   if you leave out the @pyqtSlot() line, you will also get an extra signal!
#   so you might even get three!
    def on_OpenCommBtn_clicked(self):
        print('open communication')
        ret = AVS_Init(0)
        # QMessageBox.information(self,"Info","AVS_Init returned:  {0:d}".format(ret))
        ret = AVS_GetNrOfDevices()
        # QMessageBox.information(self,"Info","AVS_GetNrOfDevices returned:  {0:d}".format(ret))
        mylist = AvsIdentityType()
        print('mylist1:',type(mylist))
        mylist = AVS_GetList(1)
        print('mylist2:',mylist)
        serienummer = str(mylist[0].SerialNumber.decode("utf-8"))
        QMessageBox.information(self,"Info","Found Serialnumber: " + serienummer)
        globals.dev_handle = AVS_Activate(mylist[0])
        # QMessageBox.information(self,"Info","AVS_Activate returned:  {0:d}".format(globals.dev_handle))
        devcon = DeviceConfigType()
        devcon = AVS_GetParameter(globals.dev_handle, 63484)
        globals.pixels = devcon.m_Detector_m_NrPixels
        print('type:',type(AVS_GetLambda(globals.dev_handle)))
        globals.wavelength = AVS_GetLambda(globals.dev_handle)
        self.data_wavelength = np.frombuffer(globals.wavelength)
        self.data_wavelength = self.data_wavelength[0:np.argwhere(self.data_wavelength <= 0)[0, 0]]

        # for index in range(len(self.data_wavelength)):
        #     box = QCheckBox(str(index))	# 实例化一个QCheckBox，吧文字传进去
        #     box.stateChanged.connect(self.getChoose)
        #     item = QListWidgetItem()  # 实例化一个Item，QListWidget，不能直接加入QCheckBox
        #     self.listWidget.addItem(item)	# 把QListWidgetItem加入QListWidget
        #     self.listWidget.setItemWidget(item, box)  # 再把QCheckBox加入QListWidgetItem
        self.StartMeasBtn.setEnabled(True)
        self.VersionBtn.setEnabled(True)
        return

    @pyqtSlot()
    def on_CloseCommBtn_clicked(self):
        print('close communication')
        # callbackclass.callback(self, 0, 0) # test
        return

    @pyqtSlot()
    def on_VersionBtn_clicked(self):
        print('version info')
        FPGAver = bytes(VERSION_LEN)
        FWver = bytes(VERSION_LEN)
        DLLver = bytes(VERSION_LEN)
        ret = AVS_GetVersionInfo(globals.dev_handle, FPGAver, FWver, DLLver)
        FPGAver = ret[0]
        FWver = ret[1]
        DLLver = ret[2]
        QMessageBox.information(self,"Info","FPGA version: {FPGA} \nFirmware version: {FW} \nDLL version: {DLL}" \
                               .format(FPGA=FPGAver.value.decode('utf-8'), 
                                       FW=FWver.value.decode('utf-8'),  
                                       DLL=DLLver.value.decode('utf-8')))
        return

    @pyqtSlot()
    def on_StartMeasBtn_clicked(self):
        print('start measurement')
        self.StartMeasBtn.setEnabled(False)
        ret = AVS_UseHighResAdc(globals.dev_handle, True)
        measconfig = MeasConfigType()
        measconfig.m_StartPixel = 0
        measconfig.m_StopPixel = globals.pixels - 1
        #IntegrationTime
        measconfig.m_IntegrationTime = float(self.IntTimeEdt.text())
        measconfig.m_IntegrationDelay = 0
        #number of averages in a single measurement
        measconfig.m_NrAverages = int(self.NumAvgEdt.text())
        measconfig.m_CorDynDark_m_Enable = 0  # nesting of types does NOT work!!
        measconfig.m_CorDynDark_m_ForgetPercentage = 0
        measconfig.m_Smoothing_m_SmoothPix = 0
        measconfig.m_Smoothing_m_SmoothModel = 0
        measconfig.m_SaturationDetection = 0
        measconfig.m_Trigger_m_Mode = 0
        measconfig.m_Trigger_m_Source = 0
        measconfig.m_Trigger_m_SourceType = 0
        measconfig.m_Control_m_StrobeControl = 0
        measconfig.m_Control_m_LaserDelay = 0
        measconfig.m_Control_m_LaserWidth = 0
        measconfig.m_Control_m_LaserWaveLength = 785.0
        measconfig.m_Control_m_StoreToRam = 0
        ret = AVS_PrepareMeasure(globals.dev_handle, measconfig)
        print('prepare for measure:',ret)

        nummeas = int(self.NumMeasEdt.text())

        # to use Windows messages, supply a window handle to send the messages to
        # ret = AVS_Measure(globals.dev_handle, int(self.winId()), nummeas)
        # single message sent from DLL, confirmed with Spy++
        # when using polling, just pass a 0 for the windows handle
        self.data_time = np.linspace(measconfig.m_IntegrationTime,nummeas * measconfig.m_IntegrationTime, num=nummeas, endpoint=True)

        globals.stopscanning = False
        while (globals.stopscanning == False):
            ret = AVS_Measure(globals.dev_handle, 0, 1)
            print('measure',ret)
            dataready = False
            while (dataready == False):
                dataready = (AVS_PollScan(globals.dev_handle) == True)
                print("dataready", dataready)
            if dataready == True:
                print('dataready', dataready)
                self.scans = self.scans + 1
                if (self.scans >= nummeas):
                    globals.stopscanning = True
                self.newdata.emit()
            time.sleep(0.01)
            self.repaint()
            qApp.processEvents() # allows clicking of the StopMeasBtn to be seen
        self.StartMeasBtn.setEnabled(True)
        return

    def getChoose(self):
        """
        得到备选统计项的字段
        :return: list[str]
        """
        count = self.listWidget.count()  # 得到QListWidget的总个数
        cb_list = [self.listWidget.itemWidget(self.listWidget.item(i))
                   for i in range(count)]  # 得到QListWidget里面所有QListWidgetItem中的QCheckBox
        # print(cb_list)
        chooses = []  # 存放被选择的数据
        for cb in cb_list:  # type:QCheckBox
            if cb.isChecked():
                chooses.append(cb.text())
        print(chooses)
        return chooses

    @pyqtSlot()
    def on_StopMeasBtn_clicked(self):
        print('stop measurement')
        ret = AVS_StopMeasure(globals.dev_handle)
        globals.stopscanning = True
        self.StartMeasBtn.setEnabled(True)
        self.repaint()
        return

    #def nativeEvent(self, eventType, message):
    #    msg = ctypes.wintypes.MSG.from_address(message.__int__())
    #    if eventType == "windows_generic_MSG":
    #        if msg.message == WM_MEAS_READY:
    #            # print("Message Received!")
    #            self.newdata.emit()
    #    return False, 0

    @pyqtSlot()
    def handle_newdata(self):
        timestamp = 0
        ret = AVS_GetScopeData(globals.dev_handle)
        timestamp = ret[0]
        print('timestamp',timestamp)
        globals.spectraldata = ret[1]
        # QMessageBox.information(self,"Info","Received data")
        print('数据', globals.spectraldata)
        #self.plot.update()
        time.sleep(2000)
        qApp.processEvents() # allows repaint to occur between scans
        return
    def draw_time_spect(self,X):
        for index_wavl in range(len(self.data_wavelength)):
            self.p1.plot(self.data_time,X[:,index_wavl],pen=(random.randint(0,200),random.randint(0,200),random.randint(0,200)))
            qApp.processEvents()
    def draw_wavel_spect(self,X):
        for index_time in range(len(self.data_time)):
            self.p2.plot(self.data_wavelength,X[index_time,],pen='red',clear=True)
            qApp.processEvents()
    # 启动定时器 时间间隔秒
    def timer_start(self):
        self.on_StartMeasBtn_clicked()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.draw)
        self.timer.start(500)

    @pyqtSlot()
    def on_select_all_clicked(self):
        #全选
        total_count = self.listWidget.count()
        print('全选',total_count)
        for i in range(total_count):
            self.listWidget.item(i).setSelected(True)

    @pyqtSlot()
    def on_cancel_all_clicked(self):
        selected_items = self.listWidget.selectedItems()
        if len(selected_items)<=0:
            return
        for item in selected_items:
            item.setSelected(False)

    @pyqtSlot()
    def on_commit_clicked(self):
        path_list = []
        file_name = []
        selected_items = self.listWidget.selectedItems()

        selected_items.sort(key=lambda x:int(x.text()[0:-9]))
        if len(selected_items)<=0:
            return
        for item in selected_items:
            file_name.append(item.text().split('.')[0])
            path_list.append(os.path.join(globals.file_dir,item.text()))

        print(file_name)
        print(path_list)
        sm = pca.process_control(file_name,path_list)
        print('得分：',sm)
        for i in range(1,1+len(sm)):
            self.pt.plot(sm,pen = 'red')


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
            #保存一轮数据
            temp = []
            temp = np.insert(self.data_colu_spectrInt,0,self.data_time,axis=1)
            self.data_wavelength = np.insert(self.data_wavelength,0,0)
            temp = np.insert(temp,0,self.data_wavelength,axis=0)
            pca.write_data(time.strftime('%Y_%m_%d_%H_%M_%S)'),temp)
            #更新listwidget
            self.listWidget.clear()
            self.add_file()
            for indexSI in range(len(self.data_wavelength)-1):
                self.p1.plot(self.data_time, self.data_colu_spectrInt[:, indexSI], pen=(random.randint(0,200),random.randint(0,200),random.randint(0,200)), name='wavelength VS SpectrIntes', clear=False)
                self.p1.set
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


    # 跟随鼠标移动，提取鼠标的横轴值，并自定义纵轴的值显示
    def mouseMoved(self,evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.p2.sceneBoundingRect().contains(pos):
            mousePoint = self.p2.vb.mapSceneToView(pos)
            print('location：', mousePoint)
            # 建议不用int，精度高时用float，这样可以显示横坐标的小数
            index = int(mousePoint.x())
            if index > 0 and index < len(self.data_wavelength):
                self.label_down.setHtml(
                    "<p style='color:black'>wavelength:<span style='color:green;'>{0}</span></p><p style='color:black'>spectromintesity<span style='color:green;'>{1}</span></p>".format(
                    mousePoint.x(), self.data_wavelength[index]))
                self.label_down.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())


    @pyqtSlot()
    def on_testButton1_clicked(self):
        print('绘图测试')
        #get source data
        X=np.array(pd.read_excel("D:\\File\\project_pca\\data_segmentation\\data-1_Primary_A.xlsx"))
        X=np.delete(X,0,1)
        self.data_time=np.array(np.delete(X[:,0],0,0),dtype=np.float64)
        X=np.delete(X,0,1)
        self.data_wavelength=np.array(X[0,:],dtype=np.float64)
        X=np.array(np.delete(X,0,0),dtype=np.float64)
        # for index_wavl in range(len(self.data_wavelength)):
        #     self.p1.plot(self.data_time,X[:,index_wavl],pen=(random.randint(0,200),random.randint(0,200),random.randint(0,200)))
        #     qApp.processEvents()
        # for index_time in range(len(self.data_time)):
        #     self.p2.plot(self.data_wavelength,X[index_time,],pen='red',clear=True)
        #     qApp.processEvents()
        #     time.sleep(0.1)
        thread1 = threading.Thread(target=self.draw_time_spect(X))
        thread2 = threading.Thread(target=self.draw_wavel_spect(X))
        thread2.start()
        thread1.start()
        # thread1.isAlive()

    def add_file(self):
        file_list = os.listdir(globals.file_dir)
        for f in file_list:
            self.listWidget.addItem(f)
    @pyqtSlot()
    def on_testButton2_clicked(self):
        #get source data
        pca.get_data('D:\\File\\data_oes\\data_6_10\\1_ALL.xlsx')
        sm_cur,lm_cur = pca.pca()
        sm_pre = pca.read_score_load(globals.pre_score)
        lm_pre = pca.read_score_load(globals.pre_load)
        self.pc1.plot(sm_cur[:,0],pen='red')
        self.pc1.plot(sm_pre[:,0],pen='blue')
        self.pc2.plot(sm_cur[:,1],pen='red')
        self.pc2.plot(sm_pre[:,1],pen='blue')
        self.pc3.plot(sm_cur[:,2],pen='red')
        self.pc3.plot(sm_pre[:,2],pen='blue')
        self.pc4.plot(lm_cur[0,],pen='red')
        self.pc4.plot(lm_pre[0,],pen='blue')
        self.pc5.plot(lm_cur[1,],pen='red')
        self.pc5.plot(lm_pre[1,],pen='blue')
        self.pc6.plot(lm_cur[2,],pen='red')
        self.pc6.plot(lm_pre[2,],pen='blue')

def main():
    app = QApplication(sys.argv)
    # app.lastWindowClosed.connect(app.quit)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
