# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cancle_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import requests
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_Dialog_Cancle(object):
    # def setupUi(self, Dialog_Cancle, uid, dbuser, dbpasswd, dbhost, dbport, dbname):
    def setupUi(self, Dialog_Cancle, uid, svurl):
        Dialog_Cancle.setObjectName("Dialog_Cancle")
        Dialog_Cancle.setFixedSize(543, 311)
        self.groupBox_60 = QtWidgets.QGroupBox(Dialog_Cancle)
        self.groupBox_60.setGeometry(QtCore.QRect(10, 10, 521, 291))
        self.groupBox_60.setObjectName("groupBox_60")
        self.treeWidget_60 = QtWidgets.QTreeWidget(self.groupBox_60)
        self.treeWidget_60.setGeometry(QtCore.QRect(10, 20, 194, 221))
        self.treeWidget_60.setObjectName("treeWidget_60")
        self.treeWidget_60.setHeaderLabels(["도면번호", "도면개정"])
        self.treeWidget_60.itemSelectionChanged.connect(self.clickedDno)
        self.pushButton_60 = QtWidgets.QPushButton(self.groupBox_60)
        self.pushButton_60.setGeometry(QtCore.QRect(400, 250, 111, 31))
        self.pushButton_60.setCheckable(False)
        self.pushButton_60.setObjectName("pushButton_60")
        self.treeWidget_61 = QtWidgets.QTreeWidget(self.groupBox_60)
        self.treeWidget_61.setGeometry(QtCore.QRect(210, 20, 301, 221))
        self.treeWidget_61.setObjectName("treeWidget_61")
        self.treeWidget_61.setHeaderLabels(["파일명"])

        self.retranslateUi(Dialog_Cancle)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Cancle)

        self.svurl = svurl
        # self.dbuser = dbuser
        # self.dbpasswd = dbpasswd
        # self.dbhost = dbhost
        # self.dbport = dbport
        # self.dbname = dbname

        # 초기셋팅
        self.getCheckOutDno(uid)

    def retranslateUi(self, Dialog_Cancle):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Cancle.setWindowTitle(_translate("Dialog_Cancle", "nyPLM CAD IG"))
        Dialog_Cancle.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_60.setTitle(_translate("Dialog_Cancle", "[ 도면확정 취소 ]"))
        self.pushButton_60.setText(_translate("Dialog_Cancle", "확인"))


    # 로그인 ID 도면확정 도면 가져오기
    def getCheckOutDno(self, userid):
        URL = self.svurl + "/cad/draw/insert/selectCancledraw.do"
        # URL = "http://192.168.1.35:8080/yPLM/cad/draw/insert/selectCancledraw.do"
        data = {
            'humid': userid
        }

        try:
            response = requests.post(url=URL,data=data)
            json_response = response.json()
            res = json_response['data']
            self.chkoutFileList = []
            for val in res:
                print(list(val.values()))
                self.chkoutFileList.append(list(val.values()))

        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-SR1428 , " + str(e))
            return 0

        self.chkout_Dno_Ver_Oid = []
        for i in range(len(self.chkoutFileList)):
            self.chkout_Dno_Ver_Oid.append([])
            self.chkout_Dno_Ver_Oid[i].append(self.chkoutFileList[i][0])
            self.chkout_Dno_Ver_Oid[i].append(self.chkoutFileList[i][1])
            self.chkout_Dno_Ver_Oid[i].append(self.chkoutFileList[i][3])
        self.chkout_Dno_Ver_Oid = list(set(tuple(item) for item in self.chkout_Dno_Ver_Oid))
        self.drawCheckOutInfo()


    def drawCheckOutInfo(self):
        self.getDnoVerItem = []
        for i in range(len(self.chkout_Dno_Ver_Oid)):
            headerItem = QtWidgets.QTreeWidgetItem([self.chkout_Dno_Ver_Oid[i][0], self.chkout_Dno_Ver_Oid[i][1]])
            headerItem.setCheckState(0, QtCore.Qt.Unchecked)
            self.getDnoVerItem.append(headerItem)
            self.treeWidget_60.addTopLevelItem(headerItem)
        self.treeWidget_60.setAlternatingRowColors(True)
        self.treeWidget_60.setColumnWidth(0, 120)
        self.treeWidget_60.setColumnWidth(1, 30)


    # 도면 선택시 파일 뷰 변경
    def clickedDno(self):
        self.treeWidget_61.clear()
        getSelected = self.treeWidget_60.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            self.getChkDno = baseNode.text(0)
            self.getChkVer = baseNode.text(1)
            for i in range(len(self.chkoutFileList)):
                if self.getChkDno == self.chkoutFileList[i][0] and self.getChkVer == self.chkoutFileList[i][1]:
                    chkFileItem = QtWidgets.QTreeWidgetItem([self.chkoutFileList[i][2]])
                    self.treeWidget_61.addTopLevelItem(chkFileItem)
        self.treeWidget_61.setAlternatingRowColors(True)


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
    Dialog_Cancle = QtWidgets.QDialog()
    ui = Ui_Dialog_Cancle()
    ui.setupUi(Dialog_Cancle)
    Dialog_Cancle.show()
    sys.exit(app.exec_())

