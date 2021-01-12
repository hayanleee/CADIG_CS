# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertAdd_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import ftplib
from ftplib import FTP_TLS
import requests
import hashlib
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_Dialog_InsertAdd(object):
    def setupUi(self, Dialog_InsertAdd, get_addfile, get_path, get_rootfile, get_radioBt, get_id, get_pw, get_chkout_files):
        Dialog_InsertAdd.setObjectName("Dialog_InsertAdd")
        Dialog_InsertAdd.setFixedSize(1032, 602)
        # Dialog_InsertAdd.setFixedSize(1032, 625)
        self.groupBox_50 = QtWidgets.QGroupBox(Dialog_InsertAdd)
        self.groupBox_50.setGeometry(QtCore.QRect(10, 10, 231, 581))
        self.groupBox_50.setObjectName("groupBox_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.groupBox_50)
        self.pushButton_51.setGeometry(QtCore.QRect(10, 500, 211, 31))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.clicked.connect(self.tableDataClear)
        self.pushButton_52 = QtWidgets.QPushButton(self.groupBox_50)
        self.pushButton_52.setGeometry(QtCore.QRect(10, 540, 211, 31))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_50 = QtWidgets.QPushButton(self.groupBox_50)
        self.pushButton_50.setGeometry(QtCore.QRect(10, 460, 211, 31))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_50.clicked.connect(self.copyTableCell)
        self.lineEdit_50 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_50.setGeometry(QtCore.QRect(80, 32, 111, 20))
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.lineEdit_50.textChanged.connect(self.changeData)
        self.lineEdit_50.setEnabled(False)
        self.label_50 = QtWidgets.QLabel(self.groupBox_50)
        self.label_50.setGeometry(QtCore.QRect(13, 33, 57, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_50)
        self.label_51.setGeometry(QtCore.QRect(13, 64, 57, 16))
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.groupBox_50)
        self.label_52.setGeometry(QtCore.QRect(13, 95, 57, 16))
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_50)
        self.label_53.setGeometry(QtCore.QRect(13, 126, 57, 16))
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_50)
        self.label_54.setGeometry(QtCore.QRect(13, 157, 57, 16))
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_50)
        self.label_55.setGeometry(QtCore.QRect(13, 188, 57, 16))
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_50)
        self.label_56.setGeometry(QtCore.QRect(13, 219, 57, 16))
        # self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.groupBox_50)
        self.label_57.setGeometry(QtCore.QRect(13, 250, 57, 16))
        # self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_50)
        self.label_58.setGeometry(QtCore.QRect(13, 281, 57, 16))
        # self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_50)
        self.label_59.setGeometry(QtCore.QRect(13, 312, 57, 16))
        # self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.label_501 = QtWidgets.QLabel(self.groupBox_50)
        self.label_501.setGeometry(QtCore.QRect(13, 343, 57, 16))
        self.label_501.setFont(font)
        self.label_501.setObjectName("label_501")
        self.label_502 = QtWidgets.QLabel(self.groupBox_50)
        self.label_502.setGeometry(QtCore.QRect(13, 374, 57, 16))
        self.label_502.setFont(font)
        self.label_502.setObjectName("label_502")
        self.comboBox_50 = QtWidgets.QComboBox(self.groupBox_50)
        self.comboBox_50.setObjectName("comboBox_50")
        self.comboBox_50.setGeometry(QtCore.QRect(81, 63, 139, 20))
        self.lineEdit_51 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_51.setGeometry(QtCore.QRect(81, 94, 139, 20))
        self.lineEdit_51.setObjectName("lineEdit_51")
        ##### 테이블 컬럼 순서 변경
        self.lineEdit_51.setEnabled(False)
        self.lineEdit_51.textChanged.connect(self.changeData_2)
        self.lineEdit_52 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_52.setGeometry(QtCore.QRect(81, 125, 139, 20))
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_52.textChanged.connect(self.changeData_3)
        self.lineEdit_52.setValidator(QtGui.QIntValidator(0, 99))
        self.lineEdit_52.setMaxLength(2)
        self.lineEdit_52.setEnabled(False)
        self.comboBox_51 = QtWidgets.QComboBox(self.groupBox_50)
        self.comboBox_51.setGeometry(QtCore.QRect(81, 156, 139, 20))
        self.comboBox_51.setObjectName("comboBox_51")
        self.comboBox_52 = QtWidgets.QComboBox(self.groupBox_50)
        self.comboBox_52.setGeometry(QtCore.QRect(81, 187, 139, 20))
        self.comboBox_52.setObjectName("comboBox_52")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_53.setGeometry(QtCore.QRect(81, 218, 139, 20))
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_53.textChanged.connect(self.changeData_4)
        self.comboBox_53 = QtWidgets.QComboBox(self.groupBox_50)
        self.comboBox_53.setGeometry(QtCore.QRect(81, 249, 139, 20))
        self.comboBox_53.setObjectName("comboBox_53")
        self.comboBox_54 = QtWidgets.QComboBox(self.groupBox_50)
        self.comboBox_54.setGeometry(QtCore.QRect(81, 280, 139, 20))
        self.comboBox_54.setObjectName("comboBox_54")
        self.comboBox_55 = QtWidgets.QComboBox(self.groupBox_50)
        self.comboBox_55.setGeometry(QtCore.QRect(81, 311, 139, 20))
        self.comboBox_55.setObjectName("comboBox_55")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_55.setGeometry(QtCore.QRect(81, 342, 139, 20))
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.lineEdit_55.textChanged.connect(self.changeData_12)
        self.lineEdit_56 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_56.setGeometry(QtCore.QRect(81, 373, 139, 20))
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.lineEdit_56.textChanged.connect(self.changeData_13)
        self.pushButton_53 = QtWidgets.QPushButton(self.groupBox_50)
        self.pushButton_53.setGeometry(QtCore.QRect(194, 31, 27, 22))
        self.pushButton_53.setObjectName("pushButton_53")
        self.tableWidget_50 = QtWidgets.QTableWidget(Dialog_InsertAdd)
        self.tableWidget_50.setGeometry(QtCore.QRect(250, 16, 771, 574))
        self.tableWidget_50.setObjectName("tableWidget_50")
        self.tableWidget_50.setColumnCount(14)
        self.tableWidget_50.setRowCount(len(get_addfile))
        self.tableWidget_50.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_50.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_50.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_50.clicked.connect(self.selectRowData)
        self.lineEdit_54 = QtWidgets.QLineEdit(self.groupBox_50)
        self.lineEdit_54.setGeometry(QtCore.QRect(80, 380, 111, 20))
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_54.textChanged.connect(self.changeData_11)
        self.lineEdit_54.hide()

        # self.progressBar_2 = QtWidgets.QProgressBar(Dialog_InsertAdd)
        # self.progressBar_2.setGeometry(QtCore.QRect(10, 599, 1011, 19))
        # self.progressBar_2.setObjectName("progressBar_2")
        # self.progressBar_2.setRange(0, 100)
        # self.progressBar_2.setStyleSheet(
        #     '''
        #     QProgressBar {
        #         text-align: center;
        #         height: 10px;
        #     }
        #     QProgressBar:chunk{
        #         background-color: #3073ad;
        #         width: 10px;
        #         margin: 1px;
        #     }
        #     '''
        # )

        self.comboBox_50.addItem("")
        # self.dic1 = {"완제품": "CCN11671", "반제품": "CCN11672", "부품": "CCN11683"}
        for i in self.dic1.keys():
            self.comboBox_50.addItem(i)
        self.comboBox_51.addItem("")
        # self.dic2 = {"일반도면": "CCN00056", "프로젝트": "CCN00057"}
        for i in self.dic2.keys():
            self.comboBox_51.addItem(i)
        self.comboBox_52.addItem("")
        # self.dic3 = {"견적도 [DT01]": "CCN00059", "요구사양도 [DT02]": "CCN00060", "승인요청도 [DT03]": "CCN00061",
        #              "승인도 [DT04]": "CCN00062",
        #              "부품도 [DT05]": "CCN11715", "임시도 [DT06]": "CCN11716", "휴면도 [DT07]": "CCN11717",
        #              "참고도 [DT08]": "CCN11718",
        #              "외래도 [DT09]": "CCN11719", "JIG도면 [DT10]": "CCN11720", "FIXTURE도면 [DT11]": "CCN11721"}
        for i in self.dic3.keys():
            self.comboBox_52.addItem(i)
        self.comboBox_53.addItem("")
        # self.dic4 = {"현대자동차 [DF01]": "CCN00077", "기아자동차 [DF02]": "CCN00078", "위아 [DF03]": "CCN00079",
        #              "지엠대우 [DF04]": "CCN00080",
        #              "르노삼성 [DF05]": "CCN00179", "쌍용자동차 [DF06]": "CCN11708", "남양공업 [DF07]": "CCN11709",
        #              "현대모비스 [DF08]": "CCN11710",
        #              "TRW [DF21]": "CCN11711", "BMW [DF22]": "CCN11712", "VW [DF23]": "CCN11713",
        #              "협력사 [DF09]": "CCN11714"}
        for i in self.dic4.keys():
            self.comboBox_53.addItem(i)
        self.comboBox_54.addItem("")
        # self.dic5 = {"A0": "CCN00068", "A1": "CCN00069", "A2": "CCN00070", "A3": "CCN00071", "A4": "CCN00072",
        #              "B4": "CCN00073",
        #              "B5": "CCN00074", "기타": "CCN00075"}
        for i in self.dic5.keys():
            self.comboBox_54.addItem(i)
        self.comboBox_55.addItem("")
        # self.dic6 = {"선행": "CCN11960", "T-CAR": "CCN11961", "PROTO": "CCN11678", "PILOT1": "CCN11679",
        #              "PILOT2": "CCN1180", "M": "CCN11962", "SOP": "CCN11681"}
        for i in self.dic6.keys():
            self.comboBox_55.addItem(i)

        self.retranslateUi(Dialog_InsertAdd)
        QtCore.QMetaObject.connectSlotsByName(Dialog_InsertAdd)

        self.col = self.tableWidget_50.columnCount()
        self.row = self.tableWidget_50.rowCount()
        self.get_radio = get_radioBt
        self.regid = get_id
        self.regpw = get_pw
        self.add_drawfile = get_addfile
        self.fpath = get_path
        self.rootFile = get_rootfile
        self.chkout_files = get_chkout_files

        idx = self.comboBox_51.findText('일반도면', QtCore.Qt.MatchFixedString)
        self.comboBox_51.setCurrentIndex(idx)

        self.setInitTableWidget()
        self.comboBox_50.currentIndexChanged.connect(self.changeData_5)
        self.comboBox_51.currentIndexChanged.connect(self.changeData_6)
        self.comboBox_52.currentIndexChanged.connect(self.changeData_7)
        self.comboBox_53.currentIndexChanged.connect(self.changeData_8)
        self.comboBox_54.currentIndexChanged.connect(self.changeData_9)
        self.comboBox_55.currentIndexChanged.connect(self.changeData_10)


    def retranslateUi(self, Dialog_InsertAdd):
        _translate = QtCore.QCoreApplication.translate
        Dialog_InsertAdd.setWindowTitle(_translate("Dialog_InsertAdd", "nyPLM CAD IG"))
        Dialog_InsertAdd.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.groupBox_50.setTitle(_translate("Dialog_InsertAdd", "[ 추가 등록 ]"))
        self.pushButton_51.setText(_translate("Dialog_InsertAdd", "초  기  화"))
        self.pushButton_52.setText(_translate("Dialog_InsertAdd", "등       록"))
        self.pushButton_50.setText(_translate("Dialog_InsertAdd", "공통 적용"))
        self.label_50.setText(_translate("Dialog_InsertAdd", "차종정보:"))
        self.label_51.setText(_translate("Dialog_InsertAdd", "제품구분:"))
        self.label_52.setText(_translate("Dialog_InsertAdd", "도면번호:"))
        self.label_53.setText(_translate("Dialog_InsertAdd", "도면개정:"))
        self.label_54.setText(_translate("Dialog_InsertAdd", "도면구분:"))
        self.label_55.setText(_translate("Dialog_InsertAdd", "도면종류:"))
        self.label_56.setText(_translate("Dialog_InsertAdd", "EONO:"))
        self.label_57.setText(_translate("Dialog_InsertAdd", "도면출처:"))
        self.label_58.setText(_translate("Dialog_InsertAdd", "도면크기:"))
        self.label_59.setText(_translate("Dialog_InsertAdd", "개발단계:"))
        self.label_501.setText(_translate("Dialog_InsertNew", "파트번호:"))
        self.label_502.setText(_translate("Dialog_InsertNew", "도면명:"))
        self.pushButton_53.setText(_translate("Dialog_InsertAdd", "..."))


    # 테이블 초기 셋팅
    def setInitTableWidget(self):
        self.selectFlag = True
        ##### 테이블 컬럼 순서 변경
        # column_headers = ['파일명', '차종정보', '제품구분', '도면번호', '도면개정', '도면구분', '도면종류', 'EONO', '도면출처', '도면크기', '개발단계', '파트번호', '차종넘버']
        column_headers = ['파일명', '파트번호', '도면번호', '차종정보', '제품구분', '도면개정', '도면구분', '도면종류', 'EONO', '도면출처', '도면크기', '개발단계', '차종넘버', '도면명']
        self.tableWidget_50.setHorizontalHeaderLabels(column_headers)
        for i in range(self.row):
            self.tableWidget_50.setItem(i, 0, QtWidgets.QTableWidgetItem(self.add_drawfile[i]))
        self.tableWidget_50.setAlternatingRowColors(True)
        self.pushButton_51.setEnabled(False)
        self.pushButton_52.setEnabled(False)
        self.autoExistInfo()


    # 기존 정보 채우기
    def autoExistInfo(self):
        try:
            URL = self.svurl + "/cad/draw/select/autoFillModInfo.do"
            data = {
                "path" : self.fpath,
                "rfile": self.rootFile
            }
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            exInfo = []
            for val in res:
                exInfo.append(list(val.values()))
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR1302 , " + str(e))
            return 0

        self.lineEdit_50.setText(exInfo[0][0])                   # 차종정보
        self.lineEdit_53.setText(exInfo[0][4])                   # 고객EONO
        # for name, oid in self.dic1.items():
        #     if oid == exInfo[0][1]:
        #         index = self.comboBox_50.findText(name)
        #         self.comboBox_50.setCurrentIndex(index)          # 제품구분
        for name2, oid2 in self.dic2.items():
            if oid2 == exInfo[0][2]:
                index = self.comboBox_51.findText(name2)
                self.comboBox_51.setCurrentIndex(index)          # 도면구분
        for name3, oid3 in self.dic3.items():
            if oid3 == exInfo[0][3]:
                index = self.comboBox_52.findText(name3)
                self.comboBox_52.setCurrentIndex(index)          # 도면종류
        for name4, oid4 in self.dic4.items():
            if oid4 == exInfo[0][5]:
                index = self.comboBox_53.findText(name4)
                self.comboBox_53.setCurrentIndex(index)          # 도면출처
        for name5, oid5 in self.dic5.items():
            if oid5 == exInfo[0][6]:
                index = self.comboBox_54.findText(name5)
                self.comboBox_54.setCurrentIndex(index)          # 도면크기
        for name6, oid6 in self.dic6.items():
            if oid6 == exInfo[0][7]:
                index = self.comboBox_55.findText(name6)
                self.comboBox_55.setCurrentIndex(index)          # 개발단계
        self.lineEdit_54.setText(exInfo[0][8])                   # 차종넘버
        self.lineEdit_52.setText("0")               # 도면개정


    # 공통 적용
    def copyTableCell(self):
        self.pushButton_51.setEnabled(True)
        self.pushButton_52.setEnabled(True)
        letext_1 = self.lineEdit_50.text()              # 차종정보
        # letext_2 = self.lineEdit_51.text()              # 도면번호
        letext_3 = self.lineEdit_52.text().zfill(1)     # 도면개정
        # letext_3 = self.lineEdit_52.setText("0")     # 도면개정
        letext_4 = self.lineEdit_53.text()              # 고객EONO
        # cbtext_1 = self.comboBox_50.currentText()       # 제품구분
        cbtext_2 = self.comboBox_51.currentText()       # 도면구분
        cbtext_3 = self.comboBox_52.currentText()       # 도면종류
        cbtext_4 = self.comboBox_53.currentText()       # 도면출처
        cbtext_5 = self.comboBox_54.currentText()       # 도면크기
        cbtext_6 = self.comboBox_55.currentText()       # 개발단계
        letext_6 = self.lineEdit_55.text()              # 파트번호
        letext_5 = self.lineEdit_54.text()              # 차종넘버
        letext_7 = self.lineEdit_56.text()              # 도면명

        try:
            # 채번 가져오기 - 도면번호
            URL1 = self.svurl + "/cad/draw/select/selectComtecopseq2.do"
            data1 = {
                'id': 'CAV_ID',
                'seq': self.row
            }
            response1 = requests.post(url=URL1, data=data1)
            json_response1 = response1.json()
            res1 = json_response1['data']
            self.dno_seq = []
            for val in res1:
                self.dno_seq.append(list(val.values()))
        except requests.exceptions.RequestException as e:
            self.qMessageBox("도면번호 채번을 가져오지 못했습니다.")
            self.errorLog("ERROR-IR2123 , " + str(e))
            return 0

        for i in range(self.row):
            fname = self.tableWidget_50.item(i, 0).text()
            ind = 0
            if '.CATProduct' in fname:
                if fname != self.rootFile:
                    ind = self.comboBox_50.findText('반제품', QtCore.Qt.MatchFixedString)
                else:
                    ind = self.comboBox_50.findText('완제품', QtCore.Qt.MatchFixedString)
            elif '.CATPart' in fname:
                ind = self.comboBox_50.findText('부품', QtCore.Qt.MatchFixedString)
            self.comboBox_50.setCurrentIndex(ind)
            cbtext_1 = self.comboBox_50.currentText()

            seq = int(self.dno_seq[0][1]) + i
            dno = 'CAV' + str(seq).zfill(6)
            self.tableWidget_50.setItem(i, 3, QtWidgets.QTableWidgetItem(letext_1))
            self.tableWidget_50.setItem(i, 4, QtWidgets.QTableWidgetItem(cbtext_1))
            self.tableWidget_50.setItem(i, 2, QtWidgets.QTableWidgetItem(dno))
            self.tableWidget_50.setItem(i, 5, QtWidgets.QTableWidgetItem(letext_3))
            self.tableWidget_50.setItem(i, 6, QtWidgets.QTableWidgetItem(cbtext_2))
            self.tableWidget_50.setItem(i, 7, QtWidgets.QTableWidgetItem(cbtext_3))
            self.tableWidget_50.setItem(i, 8, QtWidgets.QTableWidgetItem(letext_4))
            self.tableWidget_50.setItem(i, 9, QtWidgets.QTableWidgetItem(cbtext_4))
            self.tableWidget_50.setItem(i, 10, QtWidgets.QTableWidgetItem(cbtext_5))
            self.tableWidget_50.setItem(i, 11, QtWidgets.QTableWidgetItem(cbtext_6))
            self.tableWidget_50.setItem(i, 1, QtWidgets.QTableWidgetItem(letext_6.upper()))
            self.tableWidget_50.setItem(i, 12, QtWidgets.QTableWidgetItem(letext_5))
            self.tableWidget_50.setItem(i, 13, QtWidgets.QTableWidgetItem(fname))


    # 테이블 row 단위 선택
    def selectRowData(self, item):
        self.selectFlag = False

        self.clickRow = item.row()
        txt = []
        for i in range(self.col):
            tmp = self.tableWidget_50.item(self.clickRow, i)
            if tmp is None:
                return 0
            txt.append(tmp.text())

        self.lineEdit_50.setText(txt[3])  # 차종정보
        self.lineEdit_51.setText(txt[2])  # 도면번호
        self.lineEdit_52.setText(txt[5])  # 도면개정
        self.lineEdit_53.setText(txt[8])  # 고객EONO
        self.lineEdit_55.setText(txt[1])  # 파트번호
        self.lineEdit_54.setText(txt[12])  # 차종넘버
        self.lineEdit_56.setText(txt[13])  # 도면명

        index_1 = self.comboBox_50.findText(txt[4], QtCore.Qt.MatchFixedString)
        index_2 = self.comboBox_51.findText(txt[6], QtCore.Qt.MatchFixedString)
        index_3 = self.comboBox_52.findText(txt[7], QtCore.Qt.MatchFixedString)
        index_4 = self.comboBox_53.findText(txt[9], QtCore.Qt.MatchFixedString)
        index_5 = self.comboBox_54.findText(txt[10], QtCore.Qt.MatchFixedString)
        index_6 = self.comboBox_55.findText(txt[11], QtCore.Qt.MatchFixedString)

        self.comboBox_50.setCurrentIndex(index_1)  # 제품구분
        self.comboBox_51.setCurrentIndex(index_2)  # 도면구분
        self.comboBox_52.setCurrentIndex(index_3)  # 도면종류
        self.comboBox_53.setCurrentIndex(index_4)  # 도면출처
        self.comboBox_54.setCurrentIndex(index_5)  # 도면크기
        self.comboBox_55.setCurrentIndex(index_6)  # 개발단계


    # 추가등록 에러잡기
    def registAdd_CatchError(self):
        for row in range(self.row):
            for col in range(self.col):
                # EONO, 도면출처, 도면크기, 개발단계는 필수값 제외함 - 2020.12.03
                if col == 8 or col == 9 or col == 10 or col == 11:
                    continue

                cell = self.tableWidget_50.item(row, col)
                if len(cell.text()) == 0:
                    self.qMessageBox("비어있는칸이 있습니다.")
                    return 'no'

        tmp_pno = []
        for tmprow in range(self.row):
            temp = self.tableWidget_50.item(tmprow, 1)
            tmp_pno.append(temp.text())
        if len(tmp_pno) != len(set(tmp_pno)):
            self.qMessageBox("중복된 파트번호를 작성했습니다. 중복을 제거해주세요.")
            return 'no'

        put_pno = ''
        for i in range(self.row):
            pno = self.tableWidget_50.item(i, 1).text()
            put_pno += pno + ";"

        try:
            URL = self.svurl + "/cad/draw/select/selectRegCatchError3.do"
            data = {
                'put_pno': put_pno
            }
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            res = json_response['data']
            self.prtInfo = []
            db_pno = []
            for val in res:
                self.prtInfo.append(list(val.values()))
                db_pno.append(list(val.values())[1])
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR1335 , " + str(e))
            return 'no'

        noPrt = list(set(tmp_pno) - set(db_pno))
        if len(noPrt) != 0:
            self.qMessageBox("일치하는 파트번호 정보가 없습니다. \n (" + str(noPrt[0]) + ")")
            return 'no'

        for idx in range(len(self.prtInfo)):
            if self.prtInfo[idx][2] == "CCN00196":
                self.qMessageBox("승인 상태인 파트번호입니다. \n (" + self.prtInfo[idx][1] + ")")
                return 'no'


    # .wrl 파일 생성
    def add_CATPtoWrl(self):
        import subprocess
        try:
            self.add_CATPtoWrl = []
            # 체크아웃 CATP* 와 추가등록 CATP* 만 변환
            tmp_all = self.chkout_files + self.add_drawfile
            for fname in tmp_all:
                idx = fname.rfind(".")
                ftype = fname[idx:]
                if ftype == ".CATPart" or ftype == ".CATProduct":
                    cmd = "CATPtoWrl.exe \"" + self.fpath + "\" \"" + fname + "\""
                    return_code = subprocess.call(cmd, shell=True)

                    # return_code = 0 is success
                    if not return_code:
                        print("- success : " + fname)
                        notype = fname[:fname.rfind('.')]
                        self.add_CATPtoWrl.append(notype + ".wrl")
                    else:
                        self.errorLog("ERROR-add-CATPtoWrl() , cmd return_code is not 0 : " + fname)
                        continue
        except Exception as e:
            self.errorLog("ERROR-IR1601 , " + str(e))
            raise Exception('< Exception func > add_CATPtoWrl')


    # CATDrawing -> pdf 변환
    def drawing_to_pdf(self):
        import subprocess
        import os, fnmatch

        try:
            # 체크아웃 drawing 과 추가등록 drawing 만 변환
            tmp_all = self.chkout_files + self.add_drawfile
            fn_noExtension = list(set(list([item[:item.rfind('.')] for item in tmp_all])))

            for fn in fn_noExtension:
                fname = fn + ".CATDrawing"
                if os.path.isfile(self.fpath + "\\" + fname):
                    # start : 체크인시 체크아웃된 pdf로 업로드되는 경우있음 (2020-12-08 수정)
                    if os.path.isfile(self.fpath + "\\" + fn + ".pdf"):
                        os.rename(self.fpath + "\\" + fn + ".pdf", self.fpath + "\\old_" + fn + ".pdf")
                    # end

                    cmd = "CATDrawingToPdf.exe \"" + self.fpath + "\" \"" + fname + "\""
                    return_code = subprocess.call(cmd, shell=True)

                    # return_code = 0 is success
                    if not return_code:
                        print("- success : " + fn)
                    else:
                        self.errorLog("ERROR-IS2 , cmd return_code is not 0 : " + fname)
                        self.noConvertFile.append(fname)
                        continue

                    file_list = fnmatch.filter(os.listdir(self.fpath), fn + "*")
                    pdf_dic = {}
                    for tmpfname in file_list:
                        if '.pdf' in tmpfname:
                            fsize = os.path.getsize(self.fpath + "\\" + tmpfname)
                            pdf_dic[tmpfname] = fsize

                    if len(pdf_dic) > 0:
                        new_pdfName = max(pdf_dic.keys(), key=(lambda k: pdf_dic[k]))
                        if not os.path.isfile(self.fpath + "\\" + fn + ".pdf"):
                            os.rename(self.fpath + "\\" + new_pdfName, self.fpath + "\\" + fn + ".pdf")
        except Exception as e:
            self.errorLog("ERROR-IR1602 , " + str(e))
            raise Exception('< Exception func > add_drawing_to_pdf')


    # 파일 업로드
    def uploadAddData(self):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        mkdirFlag = True
        self.makedir = "\\viz\\ebom\\" + self.regid + nowTime

        # local all file list
        all_file_list = os.listdir(self.fpath)

        for upFile in all_file_list:
            if os.path.isfile(self.fpath + "\\" + upFile):
                try:
                    Output_Directory = self.makedir
                    ftps = FTP_TLS(self.ftphost)
                    ftps.login(self.ftpid, self.ftppw)
                    ftps.encoding = 'utf-8'
                    ftps.prot_p()
                    if mkdirFlag:
                        ftps.mkd(self.makedir)
                        mkdirFlag = False
                    ftps.cwd(Output_Directory)
                    with open(self.fpath + "\\" + upFile, 'rb') as ftpup:
                        ftps.storbinary('STOR %s' % upFile, ftpup)
                    ftps.quit()
                    ftpup.close()
                except ftplib.all_errors as err:
                    self.errorLog("ERROR-IF314 , " + str(err))
                    raise Exception('< Exception func > uploadAddData')


    # DB data 만들기
    def addRegMakeData(self):
        try:
            self.add_ModData = ""
            for i in range(self.row):
                filename = self.tableWidget_50.item(i, 0).text()
                caroid = self.tableWidget_50.item(i, 12).text()
                prttypeoid = self.dic1[self.tableWidget_50.item(i, 4).text()]
                dno = self.tableWidget_50.item(i, 2).text()
                mversion = self.tableWidget_50.item(i, 5).text()
                moduletype = self.dic2[self.tableWidget_50.item(i, 6).text()]
                modtypeoid = self.dic3[self.tableWidget_50.item(i, 7).text()]
                eono = ''
                if len(self.tableWidget_50.item(i, 8).text()) == 0:
                    eono = '-'
                else:
                    eono = self.tableWidget_50.item(i, 8).text()
                dscoid = ''
                if len(self.tableWidget_50.item(i, 9).text()) == 0:
                    dscoid = '-'
                else:
                    dscoid = self.dic4[self.tableWidget_50.item(i, 9).text()]
                modsizeoid = ''
                if len(self.tableWidget_50.item(i, 10).text()) == 0:
                    modsizeoid = '-'
                else:
                    modsizeoid = self.dic5[self.tableWidget_50.item(i, 10).text()]
                devstep = ''
                if len(self.tableWidget_50.item(i, 11).text()) == 0:
                    devstep = '-'
                else:
                    devstep = self.dic6[self.tableWidget_50.item(i, 11).text()]
                pno = self.tableWidget_50.item(i, 1).text()
                dnam = self.tableWidget_50.item(i, 13).text()

                self.add_ModData += filename + ";"
                self.add_ModData += caroid + ";"
                self.add_ModData += prttypeoid + ";"
                self.add_ModData += dno + ";"
                self.add_ModData += mversion + ";"
                self.add_ModData += moduletype + ";"
                self.add_ModData += modtypeoid + ";"
                self.add_ModData += eono + ";"
                self.add_ModData += dscoid + ";"
                self.add_ModData += modsizeoid + ";"
                self.add_ModData += devstep + ";"
                self.add_ModData += pno + ";"
                self.add_ModData += dnam + "|"
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR8875 , " + str(e))
            raise Exception('< Exception func > addRegMakeData')


    # request to server
    def requestAddData(self):
        print("------------- add server start --------------")
        thumb_dir = self.svdraw + self.makedir
        path_1 = self.svdraw + self.makedir + "\\" + self.rootFile
        path_2 = self.svdraw + self.makedir + "\\" + self.rootFile + "_result.xml"
        cmd_xml = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + path_2 + "\" -mode xml -fs t -att t -info t -path path -log 2"
        cmd_thumb = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + thumb_dir + "\" -mode i -iw 400 -ih 300 -subimg t -info t -path path -log 2"
        URL = self.svurl + "/cad/draw/update/updateCheckInAddEbom.do"

        data = {
            'id': self.regid,
            'pwd': self.regpw,
            'thumb_dir': thumb_dir,
            'path_1': path_1,
            'path_2': path_2,
            'cmd_xml': cmd_xml,
            'cmd_thumb': cmd_thumb,
            'put_staoid': self.get_radio,
            'chkout_path': self.fpath,
            'moddata': self.add_ModData
        }

        try:
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            print("------- resultMsg -------")
            print(json_response['resultMsg'])
            self.resp_result = json_response['resultMsg']
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-IR589 , " + str(e))
            raise Exception('< Exception func > requestAddData')


    # 만들어진 서버 폴더 삭제
    def delete_mkdir(self):
        try:
            ftps = FTP_TLS(self.ftphost)
            ftps.login(self.ftpid, self.ftppw)
            ftps.encoding = 'utf-8'
            ftps.prot_p()
            ftps.cwd(self.makedir)
            for something in ftps.nlst():
                ftps.delete(something)
            ftps.rmd(".." + self.makedir[self.makedir.rfind("\\"):])
            ftps.quit()
        except ftplib.all_errors as err:
            self.errorLog("ERROR-IF123 , " + str(err))
            raise Exception('< Exception func > delete_mkdir')


    # 데이터 실시간 변경
    def changeData(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 3, QtWidgets.QTableWidgetItem(text))

    def changeData_2(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 2, QtWidgets.QTableWidgetItem(text))

    def changeData_3(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 5, QtWidgets.QTableWidgetItem(text))

    def changeData_4(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 8, QtWidgets.QTableWidgetItem(text))

    def changeData_5(self):
        if self.selectFlag:
            return 0
        text = self.comboBox_50.currentText()
        self.tableWidget_50.setItem(self.clickRow, 4, QtWidgets.QTableWidgetItem(text))

    def changeData_6(self):
        if self.selectFlag:
            return 0
        text = self.comboBox_51.currentText()
        self.tableWidget_50.setItem(self.clickRow, 6, QtWidgets.QTableWidgetItem(text))

    def changeData_7(self):
        if self.selectFlag:
            return 0
        text = self.comboBox_52.currentText()
        self.tableWidget_50.setItem(self.clickRow, 7, QtWidgets.QTableWidgetItem(text))

    def changeData_8(self):
        if self.selectFlag:
            return 0
        text = self.comboBox_53.currentText()
        self.tableWidget_50.setItem(self.clickRow, 9, QtWidgets.QTableWidgetItem(text))

    def changeData_9(self):
        if self.selectFlag:
            return 0
        text = self.comboBox_54.currentText()
        self.tableWidget_50.setItem(self.clickRow, 10, QtWidgets.QTableWidgetItem(text))

    def changeData_10(self):
        if self.selectFlag:
            return 0
        text = self.comboBox_55.currentText()
        self.tableWidget_50.setItem(self.clickRow, 11, QtWidgets.QTableWidgetItem(text))

    def changeData_11(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 12, QtWidgets.QTableWidgetItem(text))

    def changeData_12(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 1, QtWidgets.QTableWidgetItem(text.upper()))

    def changeData_13(self, text):
        if self.selectFlag:
            return 0
        self.tableWidget_50.setItem(self.clickRow, 13, QtWidgets.QTableWidgetItem(text.upper()))


    # 초기화
    def tableDataClear(self):
        self.tableWidget_50.clear()
        self.setInitTableWidget()


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
    Dialog_InsertAdd = QtWidgets.QDialog()
    ui = Ui_Dialog_InsertAdd()
    ui.setupUi(Dialog_InsertAdd)
    Dialog_InsertAdd.show()
    sys.exit(app.exec_())

