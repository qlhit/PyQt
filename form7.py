# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form7.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(936, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(936, 557))
        MainWindow.setBaseSize(QtCore.QSize(936, 557))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_10.addWidget(self.listWidget, 0, 0, 1, 1)
        self.cancel_all = QtWidgets.QPushButton(self.groupBox_2)
        self.cancel_all.setObjectName("cancel_all")
        self.gridLayout_10.addWidget(self.cancel_all, 2, 0, 1, 1)
        self.select_all = QtWidgets.QPushButton(self.groupBox_2)
        self.select_all.setObjectName("select_all")
        self.gridLayout_10.addWidget(self.select_all, 1, 0, 1, 1)
        self.commit = QtWidgets.QPushButton(self.groupBox_2)
        self.commit.setObjectName("commit")
        self.gridLayout_10.addWidget(self.commit, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenCommBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OpenCommBtn.setObjectName("OpenCommBtn")
        self.verticalLayout.addWidget(self.OpenCommBtn)
        self.CloseCommBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CloseCommBtn.setObjectName("CloseCommBtn")
        self.verticalLayout.addWidget(self.CloseCommBtn)
        self.VersionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.VersionBtn.setObjectName("VersionBtn")
        self.verticalLayout.addWidget(self.VersionBtn)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox.setObjectName("groupBox")
        self.IntTimeEdt = QtWidgets.QLineEdit(self.groupBox)
        self.IntTimeEdt.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.IntTimeEdt.setObjectName("IntTimeEdt")
        self.NumAvgEdt = QtWidgets.QLineEdit(self.groupBox)
        self.NumAvgEdt.setGeometry(QtCore.QRect(10, 120, 51, 20))
        self.NumAvgEdt.setObjectName("NumAvgEdt")
        self.NumMeasEdt = QtWidgets.QLineEdit(self.groupBox)
        self.NumMeasEdt.setGeometry(QtCore.QRect(10, 180, 51, 20))
        self.NumMeasEdt.setObjectName("NumMeasEdt")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 85, 311, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 145, 311, 21))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.groupBox)
        self.StartMeasBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StartMeasBtn.setObjectName("StartMeasBtn")
        self.verticalLayout.addWidget(self.StartMeasBtn)
        self.StopMeasBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StopMeasBtn.setObjectName("StopMeasBtn")
        self.verticalLayout.addWidget(self.StopMeasBtn)
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setObjectName("testButton")
        self.verticalLayout.addWidget(self.testButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "原始光谱"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PCA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "炉次变化"))
        self.groupBox_2.setTitle(_translate("MainWindow", "文件列表"))
        self.cancel_all.setText(_translate("MainWindow", "取消全选"))
        self.select_all.setText(_translate("MainWindow", "全选"))
        self.commit.setText(_translate("MainWindow", "提交"))
        self.OpenCommBtn.setText(_translate("MainWindow", "Open Communication"))
        self.CloseCommBtn.setText(_translate("MainWindow", "Close Communication"))
        self.VersionBtn.setText(_translate("MainWindow", "Show Version Info"))
        self.groupBox.setTitle(_translate("MainWindow", "Measurement Parameters"))
        self.label.setText(_translate("MainWindow", "Integration Time [ms]"))
        self.label_2.setText(_translate("MainWindow", "Number of Averages"))
        self.label_3.setText(_translate("MainWindow", "Number of Scans"))
        self.StartMeasBtn.setText(_translate("MainWindow", "Start Measurements"))
        self.StopMeasBtn.setText(_translate("MainWindow", "Stop Measurements"))
        self.testButton.setText(_translate("MainWindow", "test"))
