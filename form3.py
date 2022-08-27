# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(936, 557)
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
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
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
        self.label.setGeometry(QtCore.QRect(10, 20, 311, 31))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenCommBtn.setText(_translate("MainWindow", "Open Communication"))
        self.CloseCommBtn.setText(_translate("MainWindow", "Close Communication"))
        self.VersionBtn.setText(_translate("MainWindow", "Show Version Info"))
        self.groupBox.setTitle(_translate("MainWindow", "Measurement Parameters"))
        self.label.setText(_translate("MainWindow", "Integration Time [ms]"))
        self.label_2.setText(_translate("MainWindow", "Number of Averages"))
        self.label_3.setText(_translate("MainWindow", "Number of Scans"))
        self.StartMeasBtn.setText(_translate("MainWindow", "Start Measurements"))
        self.StopMeasBtn.setText(_translate("MainWindow", "Stop Measurements"))
