# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectCar_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import requests
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_Dialog_SelectCar(object):
    # def setupUi(self, Dialog_SelectCar, dbuser, dbpasswd, dbhost, dbport, dbname):
    def setupUi(self, Dialog_SelectCar, svurl):
        Dialog_SelectCar.setObjectName("Dialog_SelectCar")
        Dialog_SelectCar.setFixedSize(312, 551)
        self.groupBox_car = QtWidgets.QGroupBox(Dialog_SelectCar)
        self.groupBox_car.setGeometry(QtCore.QRect(10, 10, 291, 531))
        self.groupBox_car.setObjectName("groupBox_car")
        self.treeWidget_car = QtWidgets.QTreeWidget(self.groupBox_car)
        self.treeWidget_car.setGeometry(QtCore.QRect(10, 20, 271, 461))
        self.treeWidget_car.setObjectName("treeWidget_car")
        self.treeWidget_car.setHeaderLabels(["차종명"])
        self.pushButton_car = QtWidgets.QPushButton(self.groupBox_car)
        self.pushButton_car.setGeometry(QtCore.QRect(10, 490, 271, 31))
        self.pushButton_car.setObjectName("pushButton_car")

        self.retranslateUi(Dialog_SelectCar)
        QtCore.QMetaObject.connectSlotsByName(Dialog_SelectCar)

        self.svurl = svurl
        # self.dbuser = dbuser
        # self.dbpasswd = dbpasswd
        # self.dbhost = dbhost
        # self.dbport = dbport
        # self.dbname = dbname

        self.init_engctgView()

    def retranslateUi(self, Dialog_SelectCar):
        _translate = QtCore.QCoreApplication.translate
        Dialog_SelectCar.setWindowTitle(_translate("Dialog_SelectCar", "nyPLM CAD IG"))
        Dialog_SelectCar.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_car.setTitle(_translate("Dialog_SelectCar", "[ 차종 ]"))
        self.pushButton_car.setText(_translate("Dialog_SelectCar", "선택"))


    def init_engctgView(self):
        URL = self.svurl + "/cad/draw/insert/selectCar.do"
        # URL = "http://192.168.1.35:8080/yPLM/cad/draw/insert/selectCar.do"
        try:
            response = requests.post(url=URL)
            json_response = response.json()
            res = json_response['data']
            self.engctgView_list = []
            for val in res:
                self.engctgView_list.append(list(val.values()))
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-SR1428 , " + str(e))
            return 0

        self.drawTreeWidget()


    def drawTreeWidget(self):
        stock_parent_oid = []
        stock_Item = []
        self.all_Items = []
        self.all_Text = []
        for i in range(len(self.engctgView_list)):
            if self.engctgView_list[i][2] == 'CCN00131':
                stock_parent_oid.append(self.engctgView_list[i][1])
                self.parentItem = QtWidgets.QTreeWidgetItem([self.engctgView_list[i][0]])
                stock_Item.append(self.parentItem)
                self.all_Items.append(self.parentItem)
                self.all_Text.append(self.engctgView_list[i][0] + ":" + self.engctgView_list[i][1])

        while len(stock_parent_oid):
            for k in range(len(self.engctgView_list)):
                if self.engctgView_list[k][2] == stock_parent_oid[0]:
                    stock_parent_oid.append(self.engctgView_list[k][1])
                    childItem = QtWidgets.QTreeWidgetItem([self.engctgView_list[k][0]])
                    childItem.setCheckState(0, QtCore.Qt.Unchecked)
                    stock_Item.append(childItem)
                    stock_Item[0].addChild(childItem)
                    self.all_Items.append(childItem)
                    self.all_Text.append(self.engctgView_list[k][0] + ":" + self.engctgView_list[k][1])
            del stock_parent_oid[0]
            del stock_Item[0]

        self.treeWidget_car.addTopLevelItem(self.parentItem)
        self.treeWidget_car.expandToDepth(0)


    # 메세지박스
    def qMessageBox(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle('Message')
        msgbox.setWindowIcon(QtGui.QIcon('image/logo.png'))
        msgbox.setText(msg)
        msgbox.exec_()


    # 에러메세지 txt 파일에 떨구기
    def errorLog(self, msg):
        import datetime
        now = datetime.datetime.now()
        today = now.strftime('%Y%m%d')
        realtime = now.strftime('[%Y-%m-%d %H:%M:%S] ')
        mkfile = 'message_' + today + '.txt'
        f = open('log/' + mkfile, 'a')
        f.write(realtime + msg + '\n')
        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_SelectCar = QtWidgets.QDialog()
    ui = Ui_Dialog_SelectCar()
    ui.setupUi(Dialog_SelectCar)
    Dialog_SelectCar.show()
    sys.exit(app.exec_())

