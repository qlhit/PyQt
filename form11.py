# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form11.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.select_all = QtWidgets.QPushButton(self.groupBox_2)
        self.select_all.setObjectName("select_all")
        self.verticalLayout_4.addWidget(self.select_all)
        self.cancel_all = QtWidgets.QPushButton(self.groupBox_2)
        self.cancel_all.setObjectName("cancel_all")
        self.verticalLayout_4.addWidget(self.cancel_all)
        self.commit = QtWidgets.QPushButton(self.groupBox_2)
        self.commit.setObjectName("commit")
        self.verticalLayout_4.addWidget(self.commit)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenCommBtn = QtWidgets.QPushButton(self.groupBox)
        self.OpenCommBtn.setObjectName("OpenCommBtn")
        self.verticalLayout.addWidget(self.OpenCommBtn)
        self.CloseCommBtn = QtWidgets.QPushButton(self.groupBox)
        self.CloseCommBtn.setObjectName("CloseCommBtn")
        self.verticalLayout.addWidget(self.CloseCommBtn)
        self.VersionBtn = QtWidgets.QPushButton(self.groupBox)
        self.VersionBtn.setObjectName("VersionBtn")
        self.verticalLayout.addWidget(self.VersionBtn)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.IntTimeEdt = QtWidgets.QLineEdit(self.groupBox_3)
        self.IntTimeEdt.setObjectName("IntTimeEdt")
        self.verticalLayout_2.addWidget(self.IntTimeEdt)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.NumAvgEdt = QtWidgets.QLineEdit(self.groupBox_3)
        self.NumAvgEdt.setObjectName("NumAvgEdt")
        self.verticalLayout_2.addWidget(self.NumAvgEdt)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.NumMeasEdt = QtWidgets.QLineEdit(self.groupBox_3)
        self.NumMeasEdt.setObjectName("NumMeasEdt")
        self.verticalLayout_2.addWidget(self.NumMeasEdt)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.StartMeasBtn = QtWidgets.QPushButton(self.groupBox)
        self.StartMeasBtn.setObjectName("StartMeasBtn")
        self.verticalLayout.addWidget(self.StartMeasBtn)
        self.StopMeasBtn = QtWidgets.QPushButton(self.groupBox)
        self.StopMeasBtn.setObjectName("StopMeasBtn")
        self.verticalLayout.addWidget(self.StopMeasBtn)
        self.testButton1 = QtWidgets.QPushButton(self.groupBox)
        self.testButton1.setObjectName("testButton1")
        self.verticalLayout.addWidget(self.testButton1)
        self.testButton2 = QtWidgets.QPushButton(self.groupBox)
        self.testButton2.setObjectName("testButton2")
        self.verticalLayout.addWidget(self.testButton2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 22))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menu_O = QtWidgets.QMenu(self.menubar)
        self.menu_O.setObjectName("menu_O")
        self.menu_V = QtWidgets.QMenu(self.menubar)
        self.menu_V.setObjectName("menu_V")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_W = QtWidgets.QMenu(self.menubar)
        self.menu_W.setObjectName("menu_W")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_F.addSeparator()
        self.menuEdit.addSeparator()
        self.menu_O.addSeparator()
        self.menu_V.addSeparator()
        self.menu_S.addSeparator()
        self.menu_W.addSeparator()
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu_O.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_W.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "原始光谱"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "主成分"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "炉次得分变化"))
        self.groupBox_2.setTitle(_translate("MainWindow", "文件列表"))
        self.listWidget.setSortingEnabled(True)
        self.select_all.setText(_translate("MainWindow", "全选"))
        self.cancel_all.setText(_translate("MainWindow", "取消全选"))
        self.commit.setText(_translate("MainWindow", "提交"))
        self.groupBox.setTitle(_translate("MainWindow", "配置"))
        self.OpenCommBtn.setText(_translate("MainWindow", "Open Communication"))
        self.CloseCommBtn.setText(_translate("MainWindow", "Close Communication"))
        self.VersionBtn.setText(_translate("MainWindow", "Show Version Info"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Measurement Parameters"))
        self.label_4.setText(_translate("MainWindow", "Integration Time [ms]"))
        self.IntTimeEdt.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "Number of Averages"))
        self.NumAvgEdt.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Number of Scans"))
        self.NumMeasEdt.setText(_translate("MainWindow", "1"))
        self.StartMeasBtn.setText(_translate("MainWindow", "Start Measurements"))
        self.StopMeasBtn.setText(_translate("MainWindow", "Stop Measurements"))
        self.testButton1.setText(_translate("MainWindow", "test1"))
        self.testButton2.setText(_translate("MainWindow", "test2"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(F)"))
        self.menuEdit.setTitle(_translate("MainWindow", "编辑(E)"))
        self.menu_O.setTitle(_translate("MainWindow", "窗体(O)"))
        self.menu_V.setTitle(_translate("MainWindow", "视图(V)"))
        self.menu_S.setTitle(_translate("MainWindow", "设置(S)"))
        self.menu_W.setTitle(_translate("MainWindow", "窗口(W)"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(H)"))
