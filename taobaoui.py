# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 469)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 241, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"font: 24pt \"Arial\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 100, 181, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 100, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 150, 101, 21))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 180, 91, 16))
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 150, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 150, 91, 16))
        self.label_8.setStyleSheet("color: rgb(255, 0, 127);")
        self.label_8.setObjectName("label_8")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(563, 150, 20, 271))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 170, 421, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(83)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 160, 121, 16))
        self.label_9.setObjectName("label_9")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(580, 180, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 230, 75, 71))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 130, 401, 16))
        self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 572, 68))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 180, 110, 14))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "淘宝抢购"))
        self.pushButton.setText(_translate("mainWindow", "点我登陆"))
        self.pushButton_2.setText(_translate("mainWindow", "点我设置firefox浏览器安装位置"))
        self.label_5.setText(_translate("mainWindow", "个人信息"))
        self.label_7.setText(_translate("mainWindow", "xxx"))
        self.label_8.setText(_translate("mainWindow", "  我的购物车"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "选择"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "商品名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "单价"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "数量"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "金额"))
        self.label_9.setText(_translate("mainWindow", "设置开始抢购时间"))
        self.pushButton_3.setText(_translate("mainWindow", "点我开抢"))
        self.label_10.setText(_translate("mainWindow", "不正确的浏览器路径会引起程序崩溃"))
        self.label.setText(_translate("mainWindow", "运行条件:"))
        self.label_2.setText(_translate("mainWindow", "1.安装firefox浏览器"))
        self.label_3.setText(_translate("mainWindow", "2.下载可以驱动firefox的工具geckodrive,下载地址:https://github.com/mozilla/geckodriver/releases/"))
        self.label_4.setText(_translate("mainWindow", "3.解压下载后的geckodriver 到此软件运行的同级目录"))
        self.label_6.setText(_translate("mainWindow", "会员名称"))
