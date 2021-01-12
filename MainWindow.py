# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from ftplib import FTP_TLS
import ftplib
import requests
import os
os.environ['NLS_LANG'] = '.UTF8'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, userid, userpw, usrname):
    # def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(881, 674)
        # MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(10, 42, 861, 611))
        self.TabWidget.setObjectName("TabWidget")
        self.chg_lbtop_flag = False
        self.TabWidget.currentChanged.connect(self.tabChange)
        self.CheckOut = QtWidgets.QWidget()
        self.CheckOut.setObjectName("CheckOut")
        self.groupBox_2 = QtWidgets.QGroupBox(self.CheckOut)
        self.groupBox_2.setGeometry(QtCore.QRect(-10, -10, 871, 601))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 537, 71, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.checkOutBtn)
        self.pushButton_6.setStyleSheet(
            '''
            QPushButton{image:url(image/chkout.png); border:0px;}
            QPushButton:hover{image:url(image/chkout_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/chkout_click.png); border:0px;}
            ''')
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 112, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(447, 112, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(30, 531, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(137, 528, 631, 21))
        self.label_11.setObjectName("label_11")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(711, 537, 71, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.cancleCheckOut)
        self.pushButton_7.setStyleSheet(
            '''
            QPushButton{image:url(image/chkoutcancle.png); border:0px;}
            QPushButton:hover{image:url(image/chkoutcancle_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/chkoutcancle_click.png); border:0px;}
            ''')
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 834, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(14, 26, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(280, 52, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(514, 52, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(280, 26, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(514, 26, 61, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(75, 24, 131, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(341, 50, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(341, 24, 131, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(576, 24, 54, 20))
        self.lineEdit_8.setValidator(QtGui.QIntValidator(0, 99))
        self.lineEdit_8.setMaxLength(2)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(753, 22, 63, 42))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            '''
            QPushButton{image:url(image/search.png); border:0px;}
            QPushButton:hover{image:url(image/search_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/search_click.png); border:0px;}
            ''')
        self.pushButton_3.setToolTip("검색")
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_reset.setGeometry(QtCore.QRect(682, 22, 65, 41))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_reset.setStyleSheet(
            '''
            QPushButton{image:url(image/reset.png); border:0px;}
            QPushButton:hover{image:url(image/reset_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/reset_click.png); border:0px;}
            ''')
        self.pushButton_reset.setToolTip("초기화")
        self.pushButton_reset.clicked.connect(self.searchReset)

        # mod 버전이 pvsoid 같이.. R1 콤보박스일때
        # self.comboBox_pvs = QtWidgets.QComboBox(self.groupBox_3)
        # self.comboBox_pvs.setObjectName("comboBox_pvs")
        # self.comboBox_pvs.setGeometry(QtCore.QRect(576, 24, 54, 20))
        # self.comboBox_pvs.addItem("")
        # self.dic_pvs = {"R0": 'CCN10272', "R1": 'CCN10273', "R2": 'CCN10274', "R3": 'CCN10275', "R4": 'CCN10276',
        #               "R5": 'CCN10277', "R6": 'CCN10278', "R7": 'CCN10279', "R8": 'CCN10280', "R9": 'CCN10420',
        #               "R10": 'CCN10421', "R11": 'CCN10641', "R12": 'CCN10642', "R13": 'CCN10643', "R14": 'CCN10644',
        #               "R15": 'CCN10645', "R16": 'CCN10646', "R17": 'CCN10647', "R18": 'CCN10648', "R19": 'CCN10649',
        #               "R20": 'CCN10650', "W": 'CCN02119'}
        # for i in self.dic_pvs.keys():
        #     self.comboBox_pvs.addItem(i)
        # self.comboBox_pvs.currentIndexChanged.connect(self.changeData_pvs)

        # mod 버전이 숫자일때
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        # self.lineEdit_5.setGeometry(QtCore.QRect(576, 24, 54, 20))
        self.lineEdit_5.setGeometry(QtCore.QRect(576, 50, 54, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setValidator(QtGui.QIntValidator(0, 99))
        self.lineEdit_5.setMaxLength(2)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(75, 46, 54, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.hide()
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 23, 31, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(786, 537, 71, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet(
            '''
            QPushButton{image:url(image/drawcancle.png); border:0px;}
            QPushButton:hover{image:url(image/drawcancle_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/drawcancle_click.png); border:0px;}
            ''')
        self.pushButton_8.clicked.connect(self.cancleStaoid)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(365, 112, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.chkboxSelectAll)
        self.checkBox.setEnabled(False)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(205, 112, 91, 16))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.clicked.connect(self.radioBtnApproval)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(285, 112, 91, 16))
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.clicked.connect(self.radioBtnLatest)
        self.radioButton_4.setEnabled(False)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(569, 537, 71, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.autoOpenDownload)
        self.pushButton_5.setStyleSheet(
            '''
            QPushButton{image:url(image/opendraw.png); border:0px;}
            QPushButton:hover{image:url(image/opendraw_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/opendraw_click.png); border:0px;}
            ''')

        # self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        # self.pushButton_9.setGeometry(QtCore.QRect(718, 537, 71, 51))
        # self.pushButton_9.setObjectName("pushButton_9")
        # self.pushButton_9.setStyleSheet(
        #     '''
        #     QPushButton{image:url(image/chkin.png); border:0px;}
        #     QPushButton:hover{image:url(image/chkin_hover.png); border:0px;}
        #     QPushButton:pressed{image:url(image/chkin_click.png); border:0px;}
        #     ''')

        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setGeometry(QtCore.QRect(20, 130, 412, 391))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setHeaderLabels(["도면번호", "개정", "체크아웃", "상태", "ID"])
        self.treeWidget.header().setMinimumSectionSize(30)
        self.treeWidget.itemSelectionChanged.connect(self.clickedTreewidget)
        self.treeWidget.clicked.connect(self.isCheckBoxClick)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.history_action = QtWidgets.QAction("히스토리", self.treeWidget)
        self.treeWidget.addAction(self.history_action)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeWidget_2.setTabKeyNavigation(False)
        self.treeWidget_2.setGeometry(QtCore.QRect(438, 130, 415, 211))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.setHeaderLabels(["버전", "파일명", "체크아웃", "등록일"])
        self.treeWidget_2.header().setMinimumSectionSize(30)
        self.treeWidget_2.itemSelectionChanged.connect(self.fileSelectionChanged)
        self.treeWidget_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.down_action = QtWidgets.QAction("다운로드", self.treeWidget_2)
        self.treeWidget_2.addAction(self.down_action)
        self.down_action.triggered.connect(self.rightDownloadClick)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(438, 348, 415, 174))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setLineWidth(1)
        self.label_14.setObjectName("label_14")
        self.TabWidget.addTab(self.CheckOut, "")
        self.CheckIn = QtWidgets.QWidget()
        self.CheckIn.setObjectName("CheckIn")
        self.label_5 = QtWidgets.QLabel(self.CheckIn)
        self.label_5.setGeometry(QtCore.QRect(21, 21, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.CheckIn)
        self.lineEdit_2.setGeometry(QtCore.QRect(109, 20, 731, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.goDirPath2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.CheckIn)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 504, 411, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setGeometry(QtCore.QRect(32, 31, 90, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(225, 31, 90, 16))
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton_9 = QtWidgets.QPushButton(self.CheckIn)
        self.pushButton_9.setGeometry(QtCore.QRect(776, 524, 71, 51))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet(
            '''
            QPushButton{image:url(image/chkin.png); border:0px;}
            QPushButton:hover{image:url(image/chkin_hover.png); border:0px;}
            QPushButton:pressed{image:url(image/chkin_click.png); border:0px;}
            ''')

        self.splitter_3 = QtWidgets.QSplitter(self.CheckIn)
        self.splitter_3.setGeometry(QtCore.QRect(10, 50, 831, 441))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.treeView = QtWidgets.QTreeView(self.splitter_3)
        self.treeView.setObjectName("treeView")
        self.treeView.clicked.connect(self.changeFileList)
        self.listView = QtWidgets.QListView(self.splitter_3)
        self.listView.setObjectName("listView")
        self.listView.doubleClicked.connect(self.setRootFileCheckIn)
        self.label = QtWidgets.QLabel(self.CheckIn)
        self.label.setGeometry(QtCore.QRect(433, 510, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(self.CheckIn)
        self.label_12.setGeometry(QtCore.QRect(516, 510, 321, 16))
        self.label_12.setObjectName("label_12")
        self.TabWidget.addTab(self.CheckIn, "")
        self.NewRegistration = QtWidgets.QWidget()
        self.NewRegistration.setObjectName("NewRegistration")
        self.groupBox = QtWidgets.QGroupBox(self.NewRegistration)
        self.groupBox.setGeometry(QtCore.QRect(-10, -10, 871, 601))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(785, 530, 76, 56))
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet(
            '''
            QPushButton{image:url(image/regist.png); border:0px;}
            QPushButton:hover{image:url(image/regist_hover.png); border:0px;}
            ''')
        # self.pushButton_10.setToolTip("신규등록")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(119, 30, 731, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.goDirPath)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(31, 31, 81, 16))
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(20, 60, 831, 441))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeView_2 = QtWidgets.QTreeView(self.splitter)
        self.treeView_2.setObjectName("treeView_2")
        self.treeView_2.clicked.connect(self.changeFileList_2)
        self.listView_2 = QtWidgets.QListView(self.splitter)
        self.listView_2.setObjectName("listView_2")
        self.listView_2.doubleClicked.connect(self.setRootFileNewRegist)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(443, 520, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_icon1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_icon1.setGeometry(QtCore.QRect(529, 578, 350, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_icon1.setFont(font)
        self.label_icon1.setObjectName("label_icon1")
        self.label_icon5 = QtWidgets.QLabel(self.CheckIn)
        self.label_icon5.setGeometry(QtCore.QRect(801, 568, 61, 16))
        self.label_icon5.setFont(font)
        self.label_icon5.setObjectName("label_icon5")
        self.label_icon6 = QtWidgets.QLabel(self.groupBox)
        self.label_icon6.setGeometry(QtCore.QRect(808, 578, 61, 16))
        self.label_icon6.setFont(font)
        self.label_icon6.setObjectName("label_icon6")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(526, 512, 321, 32))
        self.label_13.setObjectName("label_13")
        self.label_13.setWordWrap(True)
        self.TabWidget.addTab(self.NewRegistration, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(748, 29, 121, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openHomepage)
        self.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap('image/plm.png')))
        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c.setGeometry(QtCore.QRect(707, 31, 38, 22))
        self.pushButton_c.setObjectName("pushButton_c")
        self.pushButton_c.setStyleSheet(
            '''
            QPushButton{image:url(image/config.png); border:0px;}
            QPushButton:hover{image:url(image/config.png); border:0px;}
            ''')
        self.pushButton_c.setToolTip("경로설정")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(
            '''
            QFrame{background-color: #3073ad;}
            '''
        )  # # rgb(48, 115, 173) || #3073ad
        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setGeometry(QtCore.QRect(14, 3, 281, 16))
        self.label_top.setObjectName("label_top")
        self.label_top.setStyleSheet(
            '''
            QLabel{color: #ffffff;}
            '''
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.userid = userid
        self.userpw = userpw
        self.usrname = usrname

        # 초기셋팅
        self.label_11.setText(self.cfg_pathdown)
        self.getFileName = ''
        self.search_staoid = ''
        self.treeWidget.setColumnWidth(0, 180)
        self.treeWidget.setColumnWidth(1, 40)
        self.treeWidget.setColumnWidth(2, 70)
        self.treeWidget.setColumnWidth(3, 50)
        self.treeWidget.setColumnWidth(4, 50)
        self.treeWidget_2.setColumnWidth(0, 50)
        self.treeWidget_2.setColumnWidth(1, 200)
        self.treeWidget_2.setColumnWidth(2, 75)
        self.treeWidget_2.setColumnWidth(3, 80)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget_2.setAlternatingRowColors(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "nyPLM CAD IG"))
        MainWindow.setWindowIcon(QtGui.QIcon('image/logo.png'))
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_7)
        self.label_3.setText(_translate("MainWindow", "[ EBOM 정보 ] "))
        self.label_4.setText(_translate("MainWindow", "[ 도면 파일 ] "))
        self.label_10.setText(_translate("MainWindow", "[ 다운로드 위치 ]"))
        self.label_11.setText(_translate("MainWindow", ""))
        self.groupBox_3.setTitle(_translate("MainWindow", "[ 검색 조건 ]"))
        self.label_7.setText(_translate("MainWindow", "차종정보 :"))
        self.label_8.setText(_translate("MainWindow", "도면번호 :"))
        self.label_9.setText(_translate("MainWindow", "도면개정 :"))
        self.label_15.setText(_translate("MainWindow", "파트번호 :"))
        self.label_16.setText(_translate("MainWindow", "파트개정 :"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.checkBox.setText(_translate("MainWindow", "전체선택"))
        self.radioButton_3.setText(_translate("MainWindow", "승인버전"))
        self.radioButton_4.setText(_translate("MainWindow", "최신버전"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.CheckOut), _translate("MainWindow", "체크아웃"))
        self.label_5.setText(_translate("MainWindow", "[ 파일 위치 ]"))
        self.groupBox_4.setTitle(_translate("MainWindow", " [ 유형 선택 ] "))
        self.radioButton.setText(_translate("MainWindow", "체크인"))
        self.radioButton_2.setText(_translate("MainWindow", "도면 확정"))
        self.label.setText(_translate("MainWindow", "최상위 파일: "))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.CheckIn), _translate("MainWindow", "체크인"))
        self.label_2.setText(_translate("MainWindow", "[ 파일 위치 ]"))
        self.label_6.setText(_translate("MainWindow", "최상위 파일: "))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.NewRegistration), _translate("MainWindow", "신규등록"))
        self.pushButton.setText(_translate("MainWindow", "nyPLM 홈페이지"))
        self.label_top.setText(_translate("MainWindow", "Check-Out"))
        # self.label_icon1.setText(_translate("MainWindow", "도면열기           체크아웃         체크아웃취소         체크인         도면확정취소"))
        # self.label_icon5.setText(_translate("MainWindow", "체크인"))


    ################################ ▽ [ C h e c k - O u t ] #################################


    # 탭 이동
    def tabChange(self, tabIndex):
        # if tabIndex == 0:
        #     self.lineEdit_7.setFocus()
        #     self.selectCheckMod = []
        #     if self.chg_lbtop_flag:
        #         self.label_top.setText("Check-In / Check-Out")
        # elif tabIndex == 1:
        #     self.colWidthFlag_2 = True
        #     self.newRegistPathInit()
        #     self.newRegInit()
        #     self.label_top.setText("New Registration")
        #     self.chg_lbtop_flag = True

        if tabIndex == 0:
            self.lineEdit_7.setFocus()
            self.selectCheckMod = []
            if self.chg_lbtop_flag:
                self.label_top.setText("Check-Out")
        elif tabIndex == 1:
            self.checkInFiles = []
            self.checkInFilesPath = []
            self.colWidthFlag = True
            self.checkInInit()
            self.label_top.setText("Check-In")
            self.chg_lbtop_flag = True
        elif tabIndex == 2:
            self.colWidthFlag_2 = True
            self.newRegistPathInit()
            self.newRegInit()
            self.label_top.setText("New Registration")
            self.chg_lbtop_flag = True


    # 검색 버튼
    def clickSearchModBtn(self):
        self.checkBox.setEnabled(True)
        self.treeWidget.clear()
        CAROID = self.lineEdit_6.text()  # 차종정보
        DNO = self.lineEdit_4.text()  # 도면번호
        MVERSION = self.lineEdit_5.text()  # 도면개정

        try:
            ############################################# 승인버전 검색 #############################################
            URL1 = self.cfg_svurl + "/cad/draw/insert/selectMainSearchParent.do"  # DrawMngDAO.selectEbomTreeList
            data1 = {
                'caroid': CAROID,
                'dno': DNO,
                'mversion': MVERSION
            }
            response1 = requests.post(url=URL1, data=data1)
            json_response1 = response1.json()
            res1 = json_response1['data']
            data = []
            for val in res1:
                data.append(list(val.values())[0])

            if len(data) == 0:
                self.qMessageBox("EBOM 정보를 조회할 수 없습니다.\n(도면 마스터파일 체크를 확인해주세요.)")
                return 0

            URL2 = self.cfg_svurl + "/cad/draw/insert/selectEBOMTreeChild.do"
            data2 = {
                'parentoid': data[0]
            }
            response2 = requests.post(url=URL2, data=data2)
            json_response2 = response2.json()
            res2 = json_response2['data']
            self.allmodlist = []
            maxLevelList = []
            for val in res2:
                if list(val.values())[8] == '0' and len(self.allmodlist) != 0:
                    break
                self.allmodlist.append(list(val.values()))
                data.append(list(val.values())[0])
                maxLevelList.append(list(val.values())[8])
            tu_data = tuple(data)
            self.maxLevel = int(max(maxLevelList))

            if len(tu_data) == 1:  # 단일 튜플은 뒤에 ('test',) 이렇게붙어서 쿼리에러나
                tu_data2 = tu_data + ('',)
            else:
                tu_data2 = tu_data
            URL3 = self.cfg_svurl + "/cad/draw/insert/selectMainSearchModfiles.do"
            data3 = {
                'tu_data': str(tu_data2)
            }
            response3 = requests.post(url=URL3, data=data3)
            json_response3 = response3.json()
            res3 = json_response3['data']
            self.allmodfiles = []
            for val in res3:
                self.allmodfiles.append(list(val.values()))

            URL4 = self.cfg_svurl + "/cad/draw/insert/selectMainSearchModfilehistory.do"
            data4 = {
                'tu_data': str(tu_data2)
            }
            response4 = requests.post(url=URL4, data=data4)
            json_response4 = response4.json()
            res4 = json_response4['data']
            self.allmodfilehistory = []
            for val in res4:
                self.allmodfilehistory.append(list(val.values()))

            ############################################# 최신버전 검색 #############################################
            self.rootStayName = self.search_staoid.replace(' ', '')
            if self.rootStayName == '승인':
                # 최상위파일 상태에 따라 radioBtn 사용여부 (승인: 활성 / 승인 외: 비활성)
                self.radioButton_3.setEnabled(True)
                self.radioButton_4.setEnabled(True)

                URL5 = self.cfg_svurl + "/cad/draw/select/selectLatestEbomParent.do"
                data5 = {
                    'dno': DNO
                }
                response5 = requests.post(url=URL5, data=data5)
                json_response5 = response5.json()
                res5 = json_response5['data']
                parentLastoid = []
                for val in res5:
                    parentLastoid = list(val.values())[0]
                    break

                if len(parentLastoid) == 0:
                    self.qMessageBox("최신버전 EBOM 정보를 조회할 수 없습니다.")
                    return 0

                URL6 = self.cfg_svurl + "/cad/draw/select/selectLatestEbomChild.do"
                data6 = {
                    'parentoid': parentLastoid
                }
                response6 = requests.post(url=URL6, data=data6)
                json_response6 = response6.json()
                res6 = json_response6['data']
                self.tmp_allmodlist = []
                tmp_maxLevelList = []
                cur_last_modoid = {}        # 현재 ebom을 최신으로 바꾸기위해 { cur_oid : last_oid } 만듬
                modlist = ""
                for val in res6:
                    if list(val.values())[8] == '0' and len(self.tmp_allmodlist) != 0:
                        break
                    self.tmp_allmodlist.append(list(val.values()))
                    tmp_maxLevelList.append(list(val.values())[8])
                    cur_last_modoid[list(val.values())[0]] = list(val.values())[13]
                    modlist += list(val.values())[13] + ","
                self.tmp_maxLevel = int(max(tmp_maxLevelList))
                self.tmp_allmodlist[0][13] = parentLastoid
                cur_last_modoid[self.tmp_allmodlist[0][0]] = parentLastoid
                modlist += parentLastoid + ","

                URL9 = self.cfg_svurl + "/cad/draw/select/selectLatestModInfo.do"
                data9 = { 'modlist': modlist }
                response9 = requests.post(url=URL9, data=data9)
                json_response9 = response9.json()
                res9 = json_response9['data']
                self.latest_modinfo = []
                for val in res9:
                    self.latest_modinfo.append(list(val.values()))

                for i in range(len(self.tmp_allmodlist)):           # allmodlist 정보 최신화
                    if self.tmp_allmodlist[i][0] in cur_last_modoid:
                        self.tmp_allmodlist[i][0] = cur_last_modoid[self.tmp_allmodlist[i][0]]      # modoid
                        for info in self.latest_modinfo:
                            if self.tmp_allmodlist[i][0] == info[0]:
                                self.tmp_allmodlist[i][1] = info[1]     # dno
                                self.tmp_allmodlist[i][2] = info[2]     # mversion
                                self.tmp_allmodlist[i][3] = info[3]     # prttypeoid
                                self.tmp_allmodlist[i][4] = info[4]     # caroid
                                self.tmp_allmodlist[i][5] = info[5]     # checkdate
                                self.tmp_allmodlist[i][6] = info[6]     # checkhumid
                                self.tmp_allmodlist[i][11] = info[7]    # staoid
                                self.tmp_allmodlist[i][12] = info[8]    # name
                                break
                    if self.tmp_allmodlist[i][7] in cur_last_modoid:
                        self.tmp_allmodlist[i][7] = cur_last_modoid[self.tmp_allmodlist[i][7]]

                URL7 = self.cfg_svurl + "/cad/draw/select/selectMainSearchModfiles2.do"
                data7 = { 'modlist': modlist }
                response7 = requests.post(url=URL7, data=data7)
                json_response7 = response7.json()
                res7 = json_response7['data']
                self.tmp_allmodfiles = []
                for val in res7:
                    self.tmp_allmodfiles.append(list(val.values()))

                URL8 = self.cfg_svurl + "/cad/draw/select/selectMainSearchModfilehistory2.do"
                data8 = { 'modlist': modlist }
                response8 = requests.post(url=URL8, data=data8)
                json_response8 = response8.json()
                res8 = json_response8['data']
                self.tmp_allmodfilehistory = []
                for val in res8:
                    self.tmp_allmodfilehistory.append(list(val.values()))

        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR1630 , " + str(e))
            return 0

        if len(self.allmodlist) == 0:
            self.qMessageBox("EBOM 데이터가 없습니다.")
            return 0

        self.makeEbomTree()


    def makeEbomTree(self):
        print(self.allmodlist)
        print(self.allmodfiles)

        self.treeWidget.clear()
        self.treeWidget_2.clear()
        self.label_14.clear()
        self.treeWidgetItem = []        # Alignment 위함.. 별거아님
        self.treeWidgetItemText = []    # 이건 별거임

        # parent tree
        if self.allmodlist[0][5] is None or len(self.allmodlist[0][5]) == 0:
            headerState = "-"
        else:
            headerState = "CheckOut"
        if self.allmodlist[0][12] is None or len(self.allmodlist[0][12]) == 0:
            headerID = "-"
        else:
            headerID = self.allmodlist[0][12]

        self.headerItem = QtWidgets.QTreeWidgetItem([self.allmodlist[0][1], self.allmodlist[0][2], headerState, self.ccn_dic17[self.allmodlist[0][11]], headerID])
        self.headerItem.setCheckState(0, QtCore.Qt.Unchecked)
        self.treeWidgetItem.append(self.headerItem)
        self.treeWidgetItemText.append(self.allmodlist[0][0] + "|" + self.allmodlist[0][1] + "|" + headerState + ":" + headerID)

        # child tree
        self.stock_Item = []
        self.stock_Item = [self.headerItem for i in range(self.maxLevel + 2)]
        self.preLevel = 0
        for k in range(1, len(self.allmodlist)):
            curLevel = int(self.allmodlist[k][8])
            if self.allmodlist[k][5] is None or len(self.allmodlist[k][5]) == 0:
                checkState = "-"
            else:
                checkState = "CheckOut"
            if self.allmodlist[k][12] is None or len(self.allmodlist[k][12]) == 0:
                checkID = "-"
            else:
                checkID = self.allmodlist[k][12]

            childItem = QtWidgets.QTreeWidgetItem([self.allmodlist[k][1], self.allmodlist[k][2], checkState, self.ccn_dic17[self.allmodlist[k][11]], checkID])
            childItem.setCheckState(0, QtCore.Qt.Unchecked)
            self.treeWidgetItem.append(childItem)
            self.treeWidgetItemText.append(
                self.allmodlist[k][0] + "|" + self.allmodlist[k][1] + "|" + checkState + ":" + checkID)
            self.stock_Item[curLevel + 1] = childItem
            self.stock_Item[curLevel].addChild(childItem)
            self.preLevel = curLevel

        self.treeWidget.addTopLevelItem(self.headerItem)
        self.treeWidget.expandAll()
        for item in self.treeWidgetItem:
            item.setTextAlignment(1, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item.setTextAlignment(2, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item.setTextAlignment(3, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item.setTextAlignment(4, QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.rowcount = 0
        iterator = QtWidgets.QTreeWidgetItemIterator(self.treeWidget)
        while iterator.value():
            # item = iterator.value()
            # print(item.text(0))
            self.rowcount += 1
            iterator += 1


    # EBOM 선택시 뷰 위젯 변경
    def clickedTreewidget(self):
        self.treeWidget_2.clear()
        getSelected = self.treeWidget.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            self.selDno = baseNode.text(0)
            thumbList = []
            for i in range(len(self.allmodfiles)):
                if self.selDno == self.allmodfiles[i][0]:
                    if self.allmodfiles[i][9] is None or len(self.allmodfiles[i][9]) == 0:
                        checkYesNo = "-"
                    else:
                        checkYesNo = "Check-Out"
                    date = self.allmodfiles[i][8]
                    # REGDATE = date.strftime('%Y/%m/%d')
                    REGDATE = date.replace('-', '/')[:10]
                    fileItem = QtWidgets.QTreeWidgetItem([self.allmodfiles[i][3], self.allmodfiles[i][7], checkYesNo, REGDATE])
                    self.treeWidget_2.addTopLevelItem(fileItem)

                    if '.jpg' in self.allmodfiles[i][6]:
                        if self.allmodfiles[i][5] is None or len(self.allmodfiles[i][5]) == 0:
                            fpath = "\\"
                        else:
                            fpath = self.allmodfiles[i][5]
                        thumbList.append(fpath)
                        thumbList.append(self.allmodfiles[i][6])
            self.thumbnailView(thumbList)


    # 썸네일 뷰어
    def thumbnailView(self, thumbList):
        import urllib.request
        import urllib.parse
        from PySide2.QtGui import QPixmap
        url = self.cfg_svurl + "/cad/draw/insert/getThumbImage.do"
        if len(thumbList) != 0:
            fpath = thumbList[0]
            fname = thumbList[1]
        else:
            self.label_14.clear()
            return 0

        data = urllib.parse.urlencode({'filepath': fpath[1:], 'filename': fname}).encode()
        try:
            image = urllib.request.urlopen(url, data).read()
        except urllib.request.URLError as e:
            self.errorLog("ERROR-MR17 , " + str(e))
            # print(e.reason)
            return 0
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(390, 170)
        self.label_14.setPixmap(pixmap)


    # 체크박스 전체선택
    def chkboxSelectAll(self):
        if self.checkBox.isChecked():
            for i in range(self.rowcount):
                self.treeWidgetItem[i].setCheckState(0, QtCore.Qt.Checked)
        else:
            for i in range(self.rowcount):
                self.treeWidgetItem[i].setCheckState(0, QtCore.Qt.Unchecked)
        self.isCheckBoxClick()


    # 승인버전 라디오버튼 선택
    def radioBtnApproval(self):
        print("승인")
        # selectCheckMod 선택 해제된지 확인해야함 (최종)
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)
        del self.selectCheckMod[:]

        save_allmodlist = []
        save_maxLevel = []
        save_allmodfiles = []
        save_allmodfilehistory = []
        save_allmodlist = self.allmodlist
        save_maxLevel = self.maxLevel
        save_allmodfiles = self.allmodfiles
        save_allmodfilehistory = self.allmodfilehistory
        self.allmodlist = self.tmp_allmodlist
        self.maxLevel = self.tmp_maxLevel
        self.allmodfiles = self.tmp_allmodfiles
        self.allmodfilehistory = self.tmp_allmodfilehistory
        self.tmp_allmodlist = save_allmodlist
        self.tmp_maxLevel = save_maxLevel
        self.tmp_allmodfiles = save_allmodfiles
        self.tmp_allmodfilehistory = save_allmodfilehistory

        self.makeEbomTree()


    # 최신버전 라디오버튼 선택
    def radioBtnLatest(self):
        print("최신")
        # selectCheckMod 선택 해제된지 확인해야함 (최종)
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)
        del self.selectCheckMod[:]

        save_allmodlist = []
        save_maxLevel = []
        save_allmodfiles = []
        save_allmodfilehistory = []
        save_allmodlist = self.allmodlist
        save_maxLevel = self.maxLevel
        save_allmodfiles = self.allmodfiles
        save_allmodfilehistory = self.allmodfilehistory
        self.allmodlist = self.tmp_allmodlist
        self.maxLevel = self.tmp_maxLevel
        self.allmodfiles = self.tmp_allmodfiles
        self.allmodfilehistory = self.tmp_allmodfilehistory
        self.tmp_allmodlist = save_allmodlist
        self.tmp_maxLevel = save_maxLevel
        self.tmp_allmodfiles = save_allmodfiles
        self.tmp_allmodfilehistory = save_allmodfilehistory

        self.makeEbomTree()


    # EBOM정보 체크박스 여부
    def isCheckBoxClick(self):
        del self.selectCheckMod[:]
        for i in range(self.rowcount):
            if self.treeWidgetItem[i].checkState(0) > 0:
                self.selectCheckMod.append(self.treeWidgetItemText[i])
        print(self.selectCheckMod)


    # 도면확정 취소버튼
    def cancleStaoid(self):
        if len(self.selectCheckMod) == 0:
            self.qMessageBox("도면을 선택해주세요.")
            return 0

        oids = ''
        for ele in self.selectCheckMod:
            oids += ele[:ele.find('|')] + ";"

        try:
            URL1 = self.cfg_svurl + "/cad/draw/update/updateCancleStaoid.do"
            data1 = {
                'oids': oids
            }
            response = requests.post(url=URL1, data=data1)
            json_response = response.json()
            res = json_response['resultMsg']
            if res == 'Success':
                self.qMessageBox("도면확정이 취소되었습니다.")
            else:
                print(res)
                print(res[:res.find("::")])
                print(res[res.find("::") + 2:])
                if res[:res.find("::")] == 'other':
                    self.qMessageBox("도면확정 상태가 아닙니다. ("+res[res.find("::")+2:]+")")
                else:
                    self.qMessageBox("취소 실패했습니다.")
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR1903 , " + str(e))
            self.qMessageBox("취소 실패했습니다.")
            return 0

        self.clickSearchModBtn()
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)


    # 도면열기 버튼
    def autoOpenDownload(self):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        if len(self.selectCheckMod) == 0:
            self.qMessageBox("도면을 선택해주세요.")
            return 0
        elif len(self.selectCheckMod) > 1:
            self.qMessageBox("도면을 하나만 선택해주세요.")
            return 0

        selCheck = self.selectCheckMod[0]
        selOid = selCheck[:selCheck.find('|')]
        selName = selCheck[selCheck.find('|')+1:selCheck.rfind('|')]
        open_draw_list = []
        for path in self.allmodlist:
            if selOid in path[9]:
                open_draw_list.append(path[0])
        open_draw_list = list(set(open_draw_list))

        # self.statusbar.showMessage("[도면열기] 다운로드 중..")

        localDirPath = self.label_11.text() + "\\_openDraw\\" + selName + nowTime
        if not (os.path.isdir(self.label_11.text() + "\\_openDraw")):
            os.makedirs(self.label_11.text() + "\\_openDraw")
        os.makedirs(localDirPath)

        rootflag = True
        for open_oid in open_draw_list:
            for i in range(len(self.allmodfiles)):
                if open_oid == self.allmodfiles[i][4]:
                # if open_oid == self.allmodfiles[i][4] and '.CATP' in self.allmodfiles[i][6]:
                    input_Directory = localDirPath + "\\" + self.allmodfiles[i][7]
                    if self.allmodfiles[i][5] is None or len(self.allmodfiles[i][5]) == 0:
                        output_Directory = "\\"
                    else:
                        output_Directory = self.allmodfiles[i][5]
                    try:
                        ftps = FTP_TLS(self.cfg_ftphost)
                        ftps.login(self.cfg_ftpid, self.cfg_ftppw)
                        ftps.encoding = 'utf-8'
                        ftps.prot_p()
                        ftps.cwd(output_Directory)
                        fd = open(input_Directory, 'wb')
                        ftps.retrbinary('RETR %s' % self.allmodfiles[i][6], fd.write)
                        ftps.quit()
                        fd.close()
                    except ftplib.all_errors as err:
                        self.errorLog("ERROR-MF18 , " + str(err))
                        return 0

                    if rootflag:
                        if self.allmodfiles[i][4] == selCheck[:selCheck.find('|')]:
                            rootfile = self.allmodfiles[i][7]
                            rootflag = False
                    # break

        # self.statusbar.showMessage("")
        self.qMessageBox("다운로드가 완료되었습니다.")
        self.autoOpenDraw(localDirPath + "\\", rootfile)


    # CATIA 버전
    # 도면 자동 열기
    def autoOpenDraw(self, getDir, rootfile):
        print(getDir)
        print(rootfile)
        import subprocess
        openFile_path = getDir + rootfile
        try:
            p = subprocess.Popen([openFile_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # output, err = p.communicate()
        # except subprocess.CalledProcessError as e:
        except:
            self.qMessageBox("[ERROR] CATIA 경로 및 옵션을 확인하세요.")
            return 0


    # # VIZDesign 버전
    # # 도면 자동 열기
    # def autoOpenDraw(self, getDir, rootfile):
    #     import subprocess
    #     VIZDesign_path = "C:\\Program Files\\Softhills\\VIZDesign\\V3.34.4\\VIZDesign.exe"
    #     openFile_path = getDir + rootfile
    #     try:
    #         p = subprocess.Popen([VIZDesign_path, openFile_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    #     except:
    #         self.qMessageBox("[ERROR] VIZDesign.exe 경로를 확인하세요.\n ( C:\\Program Files\\Softhills\\VIZDesign\\V3.34.4\\VIZDesign.exe )")
    #         return 0


    # # CREO 버전
    # # 도면 자동 열기
    # def autoOpenDraw(self, getDir, rootfile):
    #     import subprocess
    #     creo_path = "D:\\PTC\\Creo 3.0\\M120\\Parametric\\bin\\parametric.exe"
    #     openFile_path = getDir + rootfile
    #     try:
    #         p = subprocess.Popen([creo_path, openFile_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    #         # output, err = p.communicate()
    #     # except subprocess.CalledProcessError as e:
    #     except:
    #         self.qMessageBox("[ERROR] CREO 경로 및 옵션을 확인하세요.")
    #         return 0


    # 다운받을 파일 선택
    def fileSelectionChanged(self):
        getSelected = self.treeWidget_2.selectedItems()
        if getSelected:
            baseNode = getSelected[0]
            self.getFileName = baseNode.text(1)


    # 도면파일 우클릭 다운로드
    def rightDownloadClick(self):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        if len(self.getFileName) == 0:
            self.qMessageBox("파일을 선택해 주세요.")
            return 0

        localDirPath = self.label_11.text() + "\\_download_File\\" + nowTime
        if not (os.path.isdir(self.label_11.text() + "\\_download_File")):
            os.makedirs(self.label_11.text() + "\\_download_File")
        os.makedirs(localDirPath)
        for i in range(len(self.allmodfiles)):
            if (self.allmodfiles[i][0] == self.selDno) and (self.allmodfiles[i][7] == self.getFileName):
                input_Directory = localDirPath + "\\" + self.getFileName
                if self.allmodfiles[i][5] is None or len(self.allmodfiles[i][5]) == 0:
                    output_Directory = "\\"
                else:
                    output_Directory = self.allmodfiles[i][5]
                try:
                    ftps = FTP_TLS(self.cfg_ftphost)
                    ftps.login(self.cfg_ftpid, self.cfg_ftppw)
                    ftps.encoding = 'utf-8'
                    ftps.prot_p()
                    ftps.cwd(output_Directory)
                    fd = open(input_Directory, 'wb')
                    ftps.retrbinary('RETR %s' % self.allmodfiles[i][6], fd.write)
                    ftps.quit()
                    fd.close()
                except ftplib.all_errors as err:
                    self.errorLog("ERROR-MF19 , " + str(err))
                    # print(err)
                    return 0
        self.qMessageBox("다운로드가 완료되었습니다.")


    # 체크아웃 시 맥스버전 확인
    def checkMaxVersion(self):
        search_dno = self.lineEdit_4.text()
        search_mver = self.lineEdit_5.text()

        URL = self.cfg_svurl + "/cad/draw/select/checkMaxVersion.do"
        data = {
            'dno': search_dno
        }
        try:
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            print("------- resultMsg -------")
            print(json_response['resultMsg'])
            self.res_msg = json_response['resultMsg']
            res_yn = self.res_msg[:self.res_msg.find('::')]
            res_ver = self.res_msg[self.res_msg.find('::')+2:]
            if res_ver == search_mver:
                return res_yn
            else:
                return 'no'
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR326 , " + str(e))
            return 'no'


    # 체크아웃 상위 도면 체크박스 확인
    def parentoidChkBoxChecking(self):
        chkindex = list(i for i in range(self.rowcount) if self.treeWidgetItem[i].checkState(0) > 0)
        ebomseq = list(int(txt[8]) for txt in self.allmodlist)

        # 최상위도면 체크 확인
        if chkindex[0] != 0:
            return 'no'

        # chkindex 의 숫자에서 (왼쪽으로) 가장 가까운 -1 숫자의 자리idx가 chkindex에 포함되어있는지,
        for idx in chkindex[1:]:
            find_ele = ebomseq[idx] - 1
            for i, rot_ele in enumerate(ebomseq[idx-1::-1]):
                if find_ele == rot_ele:
                    if idx-i-1 in chkindex:
                        break
                    else:
                        return 'no'
        return 'Success'


    # 체크아웃 (개정시) 2222222
    def real_CheckOut_revision(self, put_oid, put_dno, put_num, put_step, put_prtpno, put_eono):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('%m%d_%H%M%S')

        # # file download
        localDirPath = self.label_11.text() + "\\_CheckOut\\" + nowTime + "_" + self.lineEdit_4.text().strip() + "_" + self.lineEdit_5.text()  # self.lineEdit_5.text().zfill(2)
        if not (os.path.isdir(self.label_11.text() + "\\_CheckOut")):
            os.makedirs(self.label_11.text() + "\\_CheckOut")
        os.makedirs(localDirPath)
        for k in range(len(self.allmodfiles)):
            input_Directory = localDirPath + "\\" + self.allmodfiles[k][7]
            if self.allmodfiles[k][5] is None or len(self.allmodfiles[k][5]) == 0:
                output_Directory = "\\"
            else:
                output_Directory = self.allmodfiles[k][5]
            try:
                ftps = FTP_TLS(self.cfg_ftphost)
                ftps.login(self.cfg_ftpid, self.cfg_ftppw)
                ftps.encoding = 'utf-8'
                ftps.prot_p()
                ftps.cwd(output_Directory)
                fd = open(input_Directory, 'wb')
                ftps.retrbinary('RETR %s' % self.allmodfiles[k][6], fd.write)
                ftps.quit()
                fd.close()
            except ftplib.all_errors as err:
                self.errorLog("ERROR-MF1925 , " + str(err))
                return 0

        # sql insert select & update
        try:
            URL1 = self.cfg_svurl + "/cad/draw/insert/checkoutRevision2.do"
            chkroot_oid = self.selectCheckMod[0][:self.selectCheckMod[0].find('|')]

            data1 = {
                'putoid': put_oid,
                'putdno': put_dno,
                'putnum': put_num,
                'putstep': put_step,
                'puteono': put_eono,
                'putprtpno': put_prtpno,
                'chkhumid': self.userid,
                'chkout_path': localDirPath,
                'root_oid': chkroot_oid
            }
            response = requests.post(url=URL1, data=data1)
            json_response = response.json()
            res1 = json_response['resultMsg']
            if res1 == 'Success':
                self.qMessageBox("체크아웃이 완료되었습니다.")
            else:
                self.qMessageBox("체크아웃에 실패했습니다.")
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR1905 , " + str(e))
            self.qMessageBox("체크아웃에 실패했습니다.")
            return 0

        # self.statusbar.showMessage("체크아웃 도면 여는중..")
        openFname = ''
        print(self.allmodfiles)
        for idx in range(len(self.allmodfiles)):
            if self.selectCheckMod[0][:self.selectCheckMod[0].find('|')] == self.allmodfiles[idx][4]:
                tmpName = self.allmodfiles[idx][7]
                idx2 = tmpName.rfind(".")
                if tmpName[idx2:idx2 + 5] == ".CATP":
                    openFname = tmpName

        if len(openFname) != 0:
            self.autoOpenDraw(localDirPath + "\\", openFname)
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)

        self.searchReset()


    # 체크아웃
    def real_CheckOut(self, cv_num, cv_step):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('%m%d_%H%M%S')
        check_date = now.strftime('%Y-%m-%d %H:%M:%S')

        # file download
        # self.statusbar.showMessage("[체크아웃] 다운로드 중..")
        localDirPath = self.label_11.text() + "\\_CheckOut\\" + nowTime + "_" + self.lineEdit_4.text().strip() + "_" + self.lineEdit_5.text()   # self.lineEdit_5.text().zfill(2)
        # localDirPath = self.label_11.text() + "\\_CheckOut\\" + self.lineEdit_4.text().strip() + "_" + self.comboBox_pvs.currentText() + nowTime
        if not (os.path.isdir(self.label_11.text() + "\\_CheckOut")):
            os.makedirs(self.label_11.text() + "\\_CheckOut")
        os.makedirs(localDirPath)
        for k in range(len(self.allmodfiles)):
            print(self.allmodfiles[k][7])
            input_Directory = localDirPath + "\\" + self.allmodfiles[k][7]
            if self.allmodfiles[k][5] is None or len(self.allmodfiles[k][5]) == 0:
                output_Directory = "\\"
            else:
                output_Directory = self.allmodfiles[k][5]
            try:
                ftps = FTP_TLS(self.cfg_ftphost)
                ftps.login(self.cfg_ftpid, self.cfg_ftppw)
                ftps.encoding = 'utf-8'
                ftps.prot_p()
                ftps.cwd(output_Directory)
                fd = open(input_Directory, 'wb')
                ftps.retrbinary('RETR %s' % self.allmodfiles[k][6], fd.write)
                ftps.quit()
                fd.close()
            except ftplib.all_errors as err:
                self.errorLog("ERROR-MF20 , " + str(err))
                # print(err)
                # self.statusbar.showMessage("")
                return 0

        oids_tmp = []
        for ele in self.selectCheckMod:
            oids_tmp.append(ele[:ele.find('|')])
        oids = tuple(oids_tmp)

        if len(oids) == 1:      # 하나만 체크아웃할때 단일튜플 ('test',) 이 에러나서 // 로컬에서 웹으로바꿔서그럼 안급할때 고치기
            oids = oids + ('',)

        # sql update
        self.data1 = {}
        if len(cv_num) != 0 and len(cv_step) != 0:          # STAOID : 승인
            self.data1 = {
                'cv_num': str(cv_num),
                'cv_step': str(cv_step),
                'check_date': str(check_date),
                'oids': str(oids)
            }
            self.URL1 = self.cfg_svurl + "/cad/draw/insert/updateModCheckOut.do"
        else:               # STAOID : 작업중
            self.data1 = {
                'check_date': str(check_date),
                'oids': str(oids)
            }
            self.URL1 = self.cfg_svurl + "/cad/draw/insert/updateModCheckOut2.do"

        try:
            response = requests.post(url=self.URL1, data=self.data1)
            json_response = response.json()
            res1 = json_response['resultMsg']
            URL2 = self.cfg_svurl + "/cad/draw/insert/updateModfilesCheckOut.do"
            chkroot_oid = self.selectCheckMod[0][:self.selectCheckMod[0].find('|')]
            data2 = {
                'oids': str(oids),
                'check_date': check_date,
                'hum_id': self.userid,
                'chkout_path': localDirPath,
                # 'root_oid': self.allmodlist[0][0]         ## 실수
                'root_oid': chkroot_oid
            }
            response2 = requests.post(url=URL2, data=data2)
            json_response2 = response2.json()
            res2 = json_response2['resultMsg']
            if res1 == 'Success' and res2 == 'Success':
                self.qMessageBox("체크아웃이 완료되었습니다.")
            else:
                self.qMessageBox("체크아웃에 실패했습니다.")
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR1842 , " + str(e))
            self.qMessageBox("체크아웃에 실패했습니다.")
            return 0

        # self.statusbar.showMessage("체크아웃 도면 여는중..")
        openFname = ''
        print(self.allmodfiles)
        for idx in range(len(self.allmodfiles)):
            if self.selectCheckMod[0][:self.selectCheckMod[0].find('|')] == self.allmodfiles[idx][4]:
                tmpName = self.allmodfiles[idx][7]
                idx2 = tmpName.rfind(".")
                if tmpName[idx2:idx2+5] == ".CATP":
                    openFname = tmpName
                # if '.CATP' in self.allmodfiles[idx][7]:
                #     openFname = self.allmodfiles[idx][7]
        if len(openFname) != 0:
            self.autoOpenDraw(localDirPath + "\\", openFname)
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)

        if len(cv_num) != 0:
            self.searchReset()
        else:
            self.clickSearchModBtn()        ### 새로고침


    # 체크아웃 취소버튼
    def cancleCheckOut(self):
        if len(self.selectCheckMod) == 0:
            self.qMessageBox("체크아웃 취소할 도면을 선택해주세요.")
            return 0

        for i in range(len(self.selectCheckMod)):
            if self.selectCheckMod[i][self.selectCheckMod[i].rfind(':')+1:] == '-':
                self.qMessageBox("체크아웃 상태가 아닙니다. (" + self.selectCheckMod[i][self.selectCheckMod[i].find('|')+1:self.selectCheckMod[i].rfind('|')] + ")")
                return 0

        for k in range(len(self.selectCheckMod)):
            if self.selectCheckMod[k][self.selectCheckMod[k].rfind(':')+1:] != self.usrname:
                self.qMessageBox("체크아웃 ID를 확인하세요. (" + self.selectCheckMod[k][self.selectCheckMod[k].find('|')+1:self.selectCheckMod[k].rfind('|')] + ")")
                return 0

        # self.statusbar.showMessage("[체크아웃] 해제 중..")
        oids_tmp = []
        for ele in self.selectCheckMod:
            oids_tmp.append(ele[:ele.find('|')])
        oids = ''
        for txt in oids_tmp:
            oids += txt + ";"

        try:
            URL1 = self.cfg_svurl + "/cad/draw/update/updateCancleCheckout.do"
            data1 = {
                'oids': oids
            }
            response = requests.post(url=URL1, data=data1)
            json_response = response.json()
            res1 = json_response['resultMsg']
            if res1 == 'Success':
                self.qMessageBox("해제되었습니다.")
            else:
                self.qMessageBox("해제 실패했습니다.")
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR1903 , " + str(e))
            self.qMessageBox("해제 실패했습니다.")
            return 0

        self.clickSearchModBtn()
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)


    # 검색 정보 초기화
    def searchReset(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.treeWidget.clear()
        self.treeWidget_2.clear()
        self.label_14.clear()
        self.checkBox.setCheckState(QtCore.Qt.Unchecked)
        self.checkBox.setEnabled(False)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)



    ################################# ▽ [ C h e c k - I n ] #################################

    # 체크인 초기 셋팅
    def checkInInit(self):
        self.dirModel = QtWidgets.QFileSystemModel()
        self.dirModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.dirModel.setRootPath("")
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        self.treeView.setModel(self.dirModel)
        self.listView.setModel(self.fileModel)
        tempPath = self.label_11.text() + "\\_CheckOut"
        if not (os.path.isdir(tempPath)):
            os.makedirs(tempPath)
        self.treeView.setRootIndex(self.dirModel.index(tempPath))
        self.lineEdit_2.setText(tempPath)
        self.changeFileList(self.dirModel.index(tempPath))


    # 디렉토리 이동시, 파일리스트 변경
    def changeFileList(self, index):
        filePathIdx = self.dirModel.fileInfo(index).absoluteFilePath()
        filePath = self.dirModel.filePath(index)
        self.listView.setRootIndex(self.fileModel.setRootPath(filePathIdx))
        self.lineEdit_2.setText(filePath)
        if self.colWidthFlag:
            self.treeView.setColumnWidth(0, 180)
            self.colWidthFlag = False
        else:
            self.treeView.resizeColumnToContents(0)
        self.treeView.resizeColumnToContents(1)
        self.treeView.resizeColumnToContents(2)
        self.treeView.resizeColumnToContents(3)
        self.label_12.setText('')


    # 파일위치 수동입력시 찾아가기
    def goDirPath2(self):
        getFilePath = self.lineEdit_2.text()
        getFolderPath = getFilePath[:getFilePath.rfind("\\")]
        self.treeView.setRootIndex(self.dirModel.index(getFolderPath))
        self.listView.setRootIndex(self.fileModel.setRootPath(getFilePath))


    # .wrl 파일 생성
    def CATPtoWrl(self):
        import subprocess
        try:
            for fname in self.checkout_files:
                idx = fname.rfind(".")
                ftype = fname[idx:]
                if ftype == ".CATPart" or ftype == ".CATProduct":
                    cmd = "CATPtoWrl.exe \"" + self.newPathdir + "\" \"" + fname + "\""
                    return_code = subprocess.call(cmd, shell=True)

                    # return_code = 0 is success
                    if not return_code:
                        print("- success : " + fname)
                        notype = fname[:fname.rfind('.')]
                        self.upload_wrl_pdf.append(notype + ".wrl")
                    else:
                        self.errorLog("ERROR-notAdd-CATPtoWrl() , cmd return_code is not 0 : " + fname)
                        continue
        except Exception as e:
            self.errorLog("ERROR-ME1610 , " + str(e))
            raise Exception('< Exception func > CATPtoWrl')


    # CATDrawing -> pdf 변환
    def drawing_to_pdf(self):
        import subprocess
        import fnmatch
        try:
            fn_noExtension = list(set(list([item[:item.rfind('.')] for item in self.checkout_files])))
            for fn in fn_noExtension:
                fname = fn + ".CATDrawing"
                if os.path.isfile(self.newPathdir + "\\" + fname):
                    print("-- 1 -- CATDrawing to pdf : " + fname)
                    # start : 체크인시 체크아웃된 pdf로 업로드되는 경우있음 (2020-12-08 수정)
                    if os.path.isfile(self.newPathdir + "\\" + fn + ".pdf"):
                        os.rename(self.newPathdir + "\\" + fn + ".pdf", self.newPathdir + "\\old_" + fn + ".pdf")
                        print("-- 2 -- rename pdffile")
                    # end

                    cmd = "CATDrawingToPdf.exe \"" + self.newPathdir + "\" \"" + fname + "\""
                    return_code = subprocess.call(cmd, shell=True)
                    self.upload_wrl_pdf.append(fname)
                    print("-- 3 -- cmd success")

                    # return_code = 0 is success
                    if not return_code:
                        print("- success : " + fn)
                    else:
                        self.errorLog("ERROR-IS3 , cmd return_code is not 0 : " + fname)
                        self.noConvertFile.append(fname)
                        continue

                    file_list = fnmatch.filter(os.listdir(self.newPathdir), fn + "*")
                    print("-- 4 -- fileList")
                    print(file_list)

                    pdf_dic = {}
                    for txt in file_list:
                        if '.pdf' in txt:
                            fsize = os.path.getsize(self.newPathdir + "\\" + txt)
                            pdf_dic[txt] = fsize
                    print("-- 5 -- pdf_dic")
                    print(pdf_dic)

                    if len(pdf_dic) > 0:
                        new_pdfName = max(pdf_dic.keys(), key=(lambda k: pdf_dic[k]))
                        print("-- 6 -- new_pdfName : " + new_pdfName)
                        if not os.path.isfile(self.newPathdir + "\\" + fn + ".pdf"):
                            os.rename(self.newPathdir + "\\" + new_pdfName, self.newPathdir + "\\" + fn + ".pdf")
                        self.upload_wrl_pdf.append(fn + ".pdf")
        except Exception as e:
            self.errorLog("ERROR-ME1613 , " + str(e))
            raise Exception('< Exception func > drawing_to_pdf')


    # 로컬→서버 파일 업로드
    def upload_notAddData(self):
        import datetime
        now = datetime.datetime.now()
        nowTime = now.strftime('_%m%d_%H%M%S')

        mkdirFlag = True
        self.mkdir_add = "\\viz\\ebom\\" + self.cfg_userid + nowTime
        alluploadFile = self.db_file_list + self.upload_wrl_pdf

        for upFile in alluploadFile:
            if os.path.isfile(self.newPathdir + "\\" + upFile):
                try:
                    Output_Directory = self.mkdir_add
                    ftps = FTP_TLS(self.cfg_ftphost)
                    ftps.login(self.cfg_ftpid, self.cfg_ftppw)
                    ftps.encoding = 'utf-8'
                    ftps.prot_p()
                    if mkdirFlag:
                        ftps.mkd(self.mkdir_add)
                        mkdirFlag = False
                    ftps.cwd(Output_Directory)
                    with open(self.newPathdir + "\\" + upFile, 'rb') as ftpup:
                        ftps.storbinary('STOR %s' % upFile, ftpup)
                    ftps.quit()
                    ftpup.close()
                except ftplib.all_errors as err:
                    self.errorLog("ERROR-MF413 , " + str(err))
                    raise Exception('< Exception func > upload_notAddData')


    # request to server
    def request_notAddData(self):
        print("------------- not add server start --------------")
        thumb_dir = self.cfg_svdraw + self.mkdir_add
        path_1 = self.cfg_svdraw + self.mkdir_add + "\\" + self.label_12.text()
        path_2 = self.cfg_svdraw + self.mkdir_add + "\\" + self.label_12.text() + "_result.xml"
        cmd_xml = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + path_2 + "\" -mode xml -fs t -att t -info t -path path -log 2"
        cmd_thumb = "VIZCoreTrans.exe -i \"" + path_1 + "\" -o \"" + thumb_dir + "\" -mode i -iw 400 -ih 300 -subimg t -info t -path path -log 2"
        URL = self.cfg_svurl + "/cad/draw/update/updateCheckInInfo.do"

        data = {
            'id': self.cfg_userid,
            'pwd': self.cfg_userpw,
            'cmd_xml': cmd_xml,
            'cmd_thumb': cmd_thumb,
            'path_2': path_2,
            'thumb_dir': thumb_dir,
            'chkout_path': self.newPathdir,
            'rootfile': self.label_12.text(),
            'put_staoid': self.put_radioBt
        }

        try:
            response = requests.post(url=URL, data=data)
            json_response = response.json()
            print("------- resultMsg -------")
            print(json_response['resultMsg'])
            self.resp_result = json_response['resultMsg']
        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-MR422 , " + str(e))
            raise Exception('< Exception func > request_notAddData')


    # 만들어진 서버 폴더 삭제
    def delete_mkdir(self):
        try:
            ftps = FTP_TLS(self.cfg_ftphost)
            ftps.login(self.cfg_ftpid, self.cfg_ftppw)
            ftps.encoding = 'utf-8'
            ftps.prot_p()
            ftps.cwd(self.mkdir_add)
            for something in ftps.nlst():
                ftps.delete(something)
            ftps.rmd(".." + self.mkdir_add[self.mkdir_add.rfind("\\"):])
            ftps.quit()
        except ftplib.all_errors as err:
            self.errorLog("ERROR-MF123 , " + str(err))
            raise Exception('< Exception func > delete_mkdir')
            # return 0


    # 최상위 파일 선택
    def setRootFileCheckIn(self, index):
        filePath = self.fileModel.filePath(index)
        filename = filePath[filePath.rfind("/") + 1:]
        self.label_12.setText(filename)


    ################################# ▽ [ N e w - R e g i s t e r ] #################################

    # 신규등록 현재 경로
    def newRegistPathInit(self):
        import configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        newpath = config.get('PATH_INFO', 'newpath')
        self.lineEdit.setText(newpath)


    # 신규등록 초기 셋팅
    def newRegInit(self):
        self.dirModel_2 = QtWidgets.QFileSystemModel()
        self.dirModel_2.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.dirModel_2.setRootPath("")
        self.fileModel_2 = QtWidgets.QFileSystemModel()
        self.fileModel_2.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        self.treeView_2.setModel(self.dirModel_2)
        self.listView_2.setModel(self.fileModel_2)
        newRegPath = self.lineEdit.text()
        self.treeView_2.setRootIndex(self.dirModel_2.index(newRegPath))
        self.lineEdit.setText(newRegPath)
        self.changeFileList_2(self.dirModel_2.index(newRegPath))


    # 디렉토리 이동시, 파일리스트 변경
    def changeFileList_2(self, index):
        filePathIdx = self.dirModel_2.fileInfo(index).absoluteFilePath()
        filePath = self.dirModel_2.filePath(index)
        self.listView_2.setRootIndex(self.fileModel_2.setRootPath(filePathIdx))
        self.lineEdit.setText(filePath)
        if self.colWidthFlag_2:
            self.treeView_2.setColumnWidth(0, 180)
            self.colWidthFlag_2 = False
        else:
            self.treeView_2.resizeColumnToContents(0)
        self.treeView_2.resizeColumnToContents(1)
        self.treeView_2.resizeColumnToContents(2)
        self.treeView_2.resizeColumnToContents(3)
        self.label_13.setText('')


    # 파일위치 수동입력시 찾아가기
    def goDirPath(self):
        getFilePath = self.lineEdit.text()
        getFolderPath = getFilePath[:getFilePath.rfind("\\")]
        self.treeView_2.setRootIndex(self.dirModel_2.index(getFolderPath))
        self.listView_2.setRootIndex(self.fileModel_2.setRootPath(getFilePath))


    # 최상위 파일 선택
    def setRootFileNewRegist(self, index):
        filePath = self.fileModel_2.filePath(index)
        filename = filePath[filePath.rfind("/") + 1:]
        self.label_13.setText(filename)


    ################################# ▽ [ e t c . ] #################################

    # PLM 홈페이지버튼
    def openHomepage(self):
        import webbrowser
        # url = "http://192.168.1.35:8080/yPLM/cad/yPLMLink.do?id="
        url = self.cfg_svurl + "/cad/yPLMLink.do?id="
        id = self.userid
        url += id
        webbrowser.open(url)


    # 메세지박스
    def qMessageBox(self, msg):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle('Message')
        msgbox.setWindowIcon(QtGui.QIcon('image/logo.png'))
        msgbox.setText(msg)
        msgbox.exec_()


    # 메세지박스 (선택)
    def qMessageBox_Select(self, msg):
        buttonReply = QtWidgets.QMessageBox.question(self, 'Message', msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            return 'yes'
        else:
            return 'no'


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


    # # ftp 경로 한글 체크
    # def checkKorean(self, text):
    #     import re
    #     KoreanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
    #     return KoreanCount


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

