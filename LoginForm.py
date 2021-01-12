# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginForm_v0.1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from Crypto.Cipher import AES
import configparser
import base64
import hashlib
import requests
BS = 16
pad = (lambda s: s + (BS - len(s) % BS) * bytes([BS - len(s) % BS]))
unpad = (lambda s: s[:-s[-1]])

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setFixedSize(243, 158)
        self.lb = QtWidgets.QLabel(Login)
        self.lb.setGeometry(QtCore.QRect(30, 30, 56, 12))
        self.lb.setObjectName("lb")
        self.lb2 = QtWidgets.QLabel(Login)
        self.lb2.setGeometry(QtCore.QRect(30, 60, 56, 12))
        self.lb2.setObjectName("lb2")
        self.le_ID = QtWidgets.QLineEdit(Login)
        self.le_ID.setGeometry(QtCore.QRect(100, 26, 113, 20))
        self.le_ID.setMaxLength(20)
        self.le_ID.setObjectName("le_ID")
        self.le_PW= QtWidgets.QLineEdit(Login)
        self.le_PW.setGeometry(QtCore.QRect(100, 57, 113, 20))
        self.le_PW.setMaxLength(20)
        self.le_PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_PW.setObjectName("le_PW")
        self.pb_OK = QtWidgets.QPushButton(Login)
        self.pb_OK.setGeometry(QtCore.QRect(29, 110, 75, 23))
        self.pb_OK.setObjectName("pb_OK")
        self.pb_quit= QtWidgets.QPushButton(Login)
        self.pb_quit.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.pb_quit.setObjectName("pb_quit")
        self.pb_quit.clicked.connect(self.endProgram)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        # 코드 실행시간 테스트
        # import timeit
        # start = timeit.default_timer()
        # self.initInfo()       # ini 파일 읽어오기
        # stop = timeit.default_timer()
        # self.errorLog("initInfo code time : " + str(stop - start))
        #
        # start2 = timeit.default_timer()
        # self.delLogfile()     # 로그파일 삭제
        # stop2 = timeit.default_timer()
        # self.errorLog("delLogfile code time : " + str(stop2 - start2))
        #
        # start3 = timeit.default_timer()
        # self.getCCNcode()     # 공통코드 셋팅
        # stop3 = timeit.default_timer()
        # self.errorLog("getCCNcode code time : " + str(stop3 - start3))

        self.initInfo()         # ini 파일 읽어오기
        self.delLogfile()       # 로그파일 삭제
        self.getCCNcode()       # 공통코드 셋팅


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "nyPLM CAD IG"))
        Login.setWindowIcon(QtGui.QIcon('image/logo.png'))
        self.lb.setText(_translate("Login", "아이디    :"))
        self.lb2.setText(_translate("Login", "비밀번호 :"))
        self.pb_OK.setText(_translate("Login", "확  인"))
        self.pb_quit.setText(_translate("Login", "종  료"))


    # 초기 셋팅
    def initInfo(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            cfg_login_id = config.get('LOGIN', 'id')
            self.le_ID.setText(cfg_login_id)

            if len(self.le_ID.text()) != 0:
                self.le_PW.setFocus()

            self.__class__.cfg_oracle_user = config.get('ORACLE', 'user')
            tmp_passwd = config.get('ORACLE', 'passwd')
            key = "(비공개)"
            aes = AESCipher(key)
            decrypt = aes.decrypt(tmp_passwd)
            self.__class__.cfg_oracle_passwd = decrypt
            self.__class__.cfg_oracle_host = config.get('ORACLE', 'host')
            self.__class__.cfg_oracle_port = config.get('ORACLE', 'port')
            self.__class__.cfg_oracle_dbname = config.get('ORACLE', 'sid')

            self.__class__.cfg_ftp_id = config.get('FTP', 'id')
            tmp_pw = config.get('FTP', 'pw')
            key2 = "(비공개)"
            aes2 = AESCipher(key2)
            decrypt2 = aes2.decrypt(tmp_pw)
            self.__class__.cfg_ftp_pw = decrypt2
            self.__class__.cfg_ftp_host = config.get('FTP', 'host')
            self.__class__.cfg_ftp_port = config.get('FTP', 'port')

            self.__class__.cfg_path_down = config.get('PATH_INFO', 'downpath')
            self.__class__.cfg_path_new = config.get('PATH_INFO', 'newpath')
            ### add [path_info]
            ### ; catiapath = [B25 | B26 | TESTPC]
            ### catiapath = TESTPC
            # self.__class__.cfg_path_catia = config.get('PATH_INFO', 'catiapath')
            self.__class__.cfg_server_url = config.get('SERVER', 'url')
            self.__class__.cfg_server_draw = config.get('SERVER', 'drawdir')
        except Exception as e:
            self.errorLog("ERROR-INI , " + str(e))
            return 0


    # 로그파일 일주일전꺼 삭제
    def delLogfile(self):
        import os
        from datetime import datetime, timedelta
        now = datetime.now()
        tmpDeltaTime = now + timedelta(days=-7)
        deltaTime = tmpDeltaTime.strftime('%Y%m%d')

        path_dir = 'log'
        file_list = os.listdir(path_dir)
        int_list = []
        del_list = []
        for fname in file_list:
            int_list.append(int(fname[fname.find('_') + 1:16]))

        for fdate in int_list:
            td = fdate - int(deltaTime)
            if td < 0:
                filename = 'message_' + str(fdate) + '.txt'
                del_list.append(filename)

        for fname2 in del_list:
            try:
                os.remove(path_dir + '\\' + fname2)
            except OSError as e:
                self.errorLog("ERROR-LW36 , " + str(e.filename) + " - " + str(e.strerror))
                # self.errorLog("ERROR-LW36 , %s - %s." % (e.filename, e.strerror))


    # 공통코드 셋팅
    def getCCNcode(self):
        try:
            URL1 = self.cfg_server_url + "/cad/draw/insert/selectCCN.do"
            # 제품구분
            ccnPtype = 'CCN11670'
            data1 = {'parentoid': str(ccnPtype)}
            response1 = requests.post(url=URL1, data=data1)
            json_response1 = response1.json()
            res1 = json_response1['data']
            self.__class__.dic11 = {}
            for i in range(len(res1)):
                self.__class__.dic11[res1[i]['name']] = res1[i]['oid']

            # 도면구분
            ccnDtype = 'CCN00134'
            data2 = {'parentoid': str(ccnDtype)}
            response2 = requests.post(url=URL1, data=data2)
            json_response2 = response2.json()
            res2 = json_response2['data']
            self.__class__.dic12 = {}
            for i in range(len(res2)):
                self.__class__.dic12[res2[i]['name']] = res2[i]['oid']

            # 도면종류
            ccnDvariety = 'CCN00058'
            data3 = {'parentoid': str(ccnDvariety)}
            response3 = requests.post(url=URL1, data=data3)
            json_response3 = response3.json()
            res3 = json_response3['data']
            self.__class__.dic13 = {}
            for i in range(len(res3)):
                self.__class__.dic13[res3[i]['name']] = res3[i]['oid']

            # 도면출처
            ccnDsource = 'CCN00076'
            data4 = {'parentoid': str(ccnDsource)}
            response4 = requests.post(url=URL1, data=data4)
            json_response4 = response4.json()
            res4 = json_response4['data']
            self.__class__.dic14 = {}
            for i in range(len(res4)):
                self.__class__.dic14[res4[i]['name']] = res4[i]['oid']

            # 도면크기
            ccnDsize = 'CCN00067'
            data5 = {'parentoid': str(ccnDsize)}
            response5 = requests.post(url=URL1, data=data5)
            json_response5 = response5.json()
            res5 = json_response5['data']
            self.__class__.dic15 = {}
            for i in range(len(res5)):
                self.__class__.dic15[res5[i]['name']] = res5[i]['oid']

            # 개발단계
            ccnDsource = 'CCN11677'
            data6 = {'parentoid': str(ccnDsource)}
            response6 = requests.post(url=URL1, data=data6)
            json_response6 = response6.json()
            res6 = json_response6['data']
            self.__class__.dic16 = {}
            for i in range(len(res6)):
                self.__class__.dic16[res6[i]['name']] = res6[i]['oid']

            # 도면상태
            ccnDsource = 'CCN00190'
            data7 = {'parentoid': str(ccnDsource)}
            response7 = requests.post(url=URL1, data=data7)
            json_response7 = response7.json()
            res7 = json_response7['data']
            self.__class__.dic17 = {}
            for i in range(len(res7)):
                self.__class__.dic17[res7[i]['oid']] = res7[i]['name'].replace(' ','')

        except requests.exceptions.RequestException as e:
            self.errorLog("ERROR-getCCNcode() , " + str(e))


    # SHA256 비밀번호 인코딩
    def hashSHA(self, userip):
        import hashlib, base64
        hashSHA = hashlib.sha256()
        hashSHA.update(userip.encode())
        sha = hashSHA.digest()
        bs = base64.b64encode(sha)
        userpw_hash = bs.decode('utf-8')
        return userpw_hash


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


    # 종료버튼 클릭시
    def endProgram(self):
        import sys
        sys.exit(0)


# 복호화 클래스
class AESCipher(object):
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.__iv().encode('utf-8'))
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')

    def __iv(self):
        return chr(0) * 16


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())