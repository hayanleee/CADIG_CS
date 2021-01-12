# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateVer_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import requests

class Ui_PartSearchDialog(object):
    def setupUi(self, PartSearchDialog, svurl):
        PartSearchDialog.setObjectName("PartSearchDialog")
        PartSearchDialog.setFixedSize(990, 339)
        self.groupBox = QtWidgets.QGroupBox(PartSearchDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 318))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(18, 30, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(88, 28, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 241, 201, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchPart)
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton2.setGeometry(QtCore.QRect(10, 278, 201, 29))
        self.pushButton2.setObjectName("pushButton2")
        self.tableWidget = QtWidgets.QTableWidget(PartSearchDialog)
        self.tableWidget.setGeometry(QtCore.QRect(240, 17, 741, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.retranslateUi(PartSearchDialog)
        QtCore.QMetaObject.connectSlotsByName(PartSearchDialog)

        self.svurl = svurl
        self.setInitTableHeader()


    def retranslateUi(self, PartSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        PartSearchDialog.setWindowTitle(_translate("PartSearchDialog", "nyPLM CAD IG"))
        PartSearchDialog.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox.setTitle(_translate("PartSearchDialog", "[ 파트 검색 ]"))
        self.label.setText(_translate("PartSearchDialog", "파트 번호 :"))
        self.pushButton.setText(_translate("PartSearchDialog", "검       색"))
        self.pushButton2.setText(_translate("PartSearchDialog", "확       인"))


    # 테이블 초기 셋팅
    def setInitTableHeader(self):
        self.selectFlag_3 = True
        column_headers = ['제품구분', '차종정보', '파트번호', '파트이름', '파트개정', '등록자', '상태', 'oid']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setColumnHidden(7, True)


    def searchPart(self):
        if len(self.lineEdit.text()) == 0:
            self.qMessageBox("파트 번호를 입력하세요.")
            return 0

        try:
            URL = self.svurl + "/cad/draw/select/selectPartInfo.do"
            data = { 'pno': self.lineEdit.text() }
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            self.pnoInfo = []
            for val in res:
                self.pnoInfo.append(list(val.values()))

            if len(self.pnoInfo) == 0:
                self.qMessageBox("일치하는 파트 정보가 없습니다.")
                return 0
            else:
                self.draw_table()
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-RP0101 , " + str(e))
            return 0


    def draw_table(self):
        for i in range(len(self.pnoInfo)):
            self.tableWidget.setRowCount(i + 1)
            PRTTYPE = self.pnoInfo[i][0]
            CARNAME = self.pnoInfo[i][1]
            PNO = self.pnoInfo[i][2]
            PNAME = self.pnoInfo[i][3]
            PVERSION = self.pnoInfo[i][4]
            HUMNAME = self.pnoInfo[i][5]
            STAOID = self.pnoInfo[i][6]
            OID = self.pnoInfo[i][7]

            item1 = QtWidgets.QTableWidgetItem(PRTTYPE)
            item2 = QtWidgets.QTableWidgetItem(CARNAME)
            item3 = QtWidgets.QTableWidgetItem(PNO)
            item4 = QtWidgets.QTableWidgetItem(PNAME)
            item5 = QtWidgets.QTableWidgetItem(PVERSION)
            item6 = QtWidgets.QTableWidgetItem(HUMNAME)
            item7 = QtWidgets.QTableWidgetItem(STAOID)
            item8 = QtWidgets.QTableWidgetItem(OID)

            item1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item2.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item6.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item7.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item8.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
            self.tableWidget.setItem(i, 2, item3)
            self.tableWidget.setItem(i, 3, item4)
            self.tableWidget.setItem(i, 4, item5)
            self.tableWidget.setItem(i, 5, item6)
            self.tableWidget.setItem(i, 6, item7)
            self.tableWidget.setItem(i, 7, item8)

        self.tableWidget.setAlternatingRowColors(True)


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
        try:
            f = open('log/' + mkfile, 'a')
            f.write(realtime + msg + '\n')
            f.close()
        except:
            raise Exception


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PartSearchDialog = QtWidgets.QDialog()
    ui = Ui_PartSearchDialog()
    ui.setupUi(PartSearchDialog)
    PartSearchDialog.show()
    sys.exit(app.exec_())

