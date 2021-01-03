"""
@version  0.1
@contant QQ597806630
@author zc
@desc 本项目淘宝抢购
@date 2020/12/04
说明：
classes: Mes()
function：
"""
import pyautogui
from datetime import datetime
import time
from selenium import webdriver
import sys
from PyQt5.QtCore import QThread,pyqtSignal,Qt
from PyQt5.QtWidgets import QApplication,QFileDialog, QMainWindow,QMessageBox,QCheckBox,QAbstractItemView,QTableView,QTableWidgetItem,QTableWidget
from taobaoui import Ui_mainWindow


MQTT_IP = "192.168.1.88"
MQTT_PORT = 1883
URL = "http://192.168.1.88:32888/api/workorder/pc"

class Mytaobao():
    def __init__(self):
        self.w = QMainWindow()
        self.myui = Ui_mainWindow()
        self.myui.setupUi(self.w)
        self.initmyui()

    def initmyui(self):
        self.myui.lineEdit.setText("D:/Program Files/Firefox/firefox.exe")
        self.myui.pushButton_2.clicked.connect(self.openFile)
        self.myui.pushButton.clicked.connect(self.login)
        self.myui.pushButton_3.clicked.connect(self.buy)

    def openFile(self):
        get_filename_path,ok = QFileDialog.getOpenFileName(None,"选取firefox.exe文件","C:\\","All Files (*)")
        if ok:
            self.myui.lineEdit.setText(str(get_filename_path))

    def login(self):
        path = self.myui.lineEdit.text()
        if not path.endswith("firefox.exe"):
            self.messageDialog("提示","找到火狐的浏览器都不会你还抢个蛋啊你！！！")
        else:
            option = webdriver.FirefoxOptions()
            self.browser = webdriver.Firefox(firefox_binary=path,options=option)
            self.browser.maximize_window()
            self.browser.get("https://www.taobao.com")
            while self.browser.find_element_by_link_text("亲，请登录"):
                self.browser.find_element_by_link_text("亲，请登录").click()
                time.sleep(3)
                qrcode = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[1]/i")
                if qrcode:
                    qrcode.click()
                while True:
                    try:
                        user = self.browser.find_element_by_class_name("site-nav-login-info-nick ").text
                        print(user)
                        self.myui.label_7.setText(user)
                        break
                    except:
                        time.sleep(1)
                break
        self.get_car()

    def get_car(self):
        self.browser.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)
        self.browser.find_element_by_id("J_SelectAll2").click()
        wods = self.browser.find_elements_by_class_name("item-content")
        wodlist = []
        for wod in wods:
            checkbox = wod.find_element_by_class_name("cart-checkbox ")
            name = wod.find_element_by_class_name("item-title").text
            print(name)
            price = wod.find_element_by_class_name("J_Price").text
            print(print())
            count = wod.find_element_by_class_name("text-amount").get_attribute("value")
            print(count)
            money = wod.find_element_by_class_name("J_ItemSum").text
            print(money)
            wodlist.append([checkbox,name,price,count,money])
        print(wodlist)
        self.myui.tableWidget.setRowCount(len(wodlist))
        # self.mesui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.myui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.myui.tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.myui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中
        # self.myui.tableWidget.horizontalHeader().resizeSection(0, 40)
        # self.myui.tableWidget.horizontalHeader().resizeSection(1, 100)
        # self.myui.tableWidget.horizontalHeader().resizeSection(2, 55)
        # self.myui.tableWidget.horizontalHeader().resizeSection(3, 65)
        self.myui.tableWidget.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大
        n = 0
        for i in wodlist:
            ck = QCheckBox()
            # ck.stateChanged.connect(lambda: i[0].click())
            ck.setStyleSheet("QCheckBox{margin:30px};")
            self.myui.tableWidget.setCellWidget(n, 0, ck)
            for j in range(len(i)):
                if j != 0:
                    taitem = QTableWidgetItem(str(i[j]))
                    taitem.setToolTip(i[j])
                    taitem.setTextAlignment(Qt.AlignCenter)
                    self.myui.tableWidget.setItem(n, j , taitem)
            n += 1

    def buy(self):
        if self.browser.find_element_by_link_text("结 算"):
            self.browser.find_element_by_link_text("结 算").click()
            self.order = Order(self.browser)
            self.order.mysignal.connect(lambda str:self.myui.statusbar.showMessage(str, 2000))
            self.order.start()

    def messageDialog(self, warn, msg):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, warn, msg)
        msg_box.exec_()

    def show(self):
        self.w.show()


class Order(QThread):
    mysignal = pyqtSignal(str)
    def __init__(self,browser):
        super(Order, self).__init__()
        self.browser = browser

    def run(self):
        while True:
            try:
                self.browser.find_element_by_link_text('提交订单').click()
                break
            except:
                self.browser.refresh()
                print("刷新")
                pyautogui.moveTo(1062, 481, duration=1)
                pyautogui.click()
                print("点击")
                self.mysignal.emit("提交订单失败我刷新失败再来!!!")
            # time.sleep()

if __name__=='__main__':
    app=QApplication(sys.argv)
    taobao = Mytaobao()
    taobao.show()
    sys.exit(app.exec_())

