# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biliDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 676)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/images/bilidownloader.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"    font: 14px \"Microsoft YaHei\";\n"
"}\n"
"/* 主体颜色\n"
".QWidget#centralwidget{\n"
"    background-color: rgb(156, 156, 156);\n"
"    border-radius:20px;\n"
"} */\n"
".QWidget#mainwidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"/* 编辑框样式 */\n"
"QLineEdit{\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    padding-left: 5px;\n"
"    padding-right: 27px;\n"
"}\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 238, 238);\n"
"}\n"
"\n"
"/* 按钮样式 */\n"
"QPushButton[flat=\"false\"]{\n"
"    background-color: rgb(255, 153, 153);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    font: 15px \"Microsoft YaHei\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"QPushButton#btnclose{\n"
"    background-color: rgb(255, 102, 102);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#btnclose:pressed{\n"
"    background-color: rgb(200, 80, 80);\n"
"}\n"
"QPushButton#btnmax{\n"
"    background-color: rgb(255, 255, 102);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#btnmax:pressed{\n"
"    background-color: rgb(195, 195, 78);\n"
"}\n"
"QPushButton#btnmin{\n"
"    background-color: rgb(153, 204, 102);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#btnmin:pressed{\n"
"    background-color: rgb(126, 168, 83);\n"
"}\n"
"\n"
"/* 进度条样式 */\n"
"QProgressBar{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    height: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 16px \"Microsoft YaHei\";\n"
"    border-radius:6px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(255, 204, 153);\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"/* 选择表样式 */\n"
"QListWidget{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    border-radius:15px;\n"
"    padding: 5px;\n"
"}\n"
"QListWidget::item{\n"
"    border: 1px dashed rgb(255, 204, 153);\n"
"    border-radius: 5px\n"
"}\n"
"QListWidget::item:hover{\n"
"    background-color: rgb(255, 204, 153);\n"
"}\n"
"QListWidget::item:focus{\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* 选择框样式 */\n"
"QComboBox{\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"    background: rgb(255, 238, 238)\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    selection-background-color: rgb(255, 204, 153)\n"
"}\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position :  top  left;\n"
"     width :  28px ;\n"
"     border: none;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(:/combo/images/dd.png);\n"
"}\n"
"QComboBox::down-arrow:hover{\n"
"    image: url(:/combo/images/dd1.png);\n"
"}\n"
"QComboBox::down-arrow:pressed{\n"
"    image: url(:/combo/images/dd2.png);\n"
"}\n"
"\n"
"/* 文本框样式 */\n"
"QPlainTextEdit{\n"
"    border-radius: 15px;\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Title Frame样式 */\n"
"QFrame#title{\n"
"    background-image: url(:/title/images/title.png);\n"
"}\n"
"\n"
"/* 分组框样式 */\n"
"QGroupBox{\n"
"    border: 2px solid rgb(255, 153, 153);\n"
"    border-radius: 15px;\n"
"    margin-top: 2ex;\n"
"}\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 3px;\n"
"}\n"
"\n"
"/* 组合框样式 */\n"
"/*QCheckBox{}*/\n"
"QFrame#title{\n"
"    border: none\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainwidget = QtWidgets.QWidget(self.centralwidget)
        self.mainwidget.setGeometry(QtCore.QRect(20, 20, 881, 631))
        self.mainwidget.setObjectName("mainwidget")
        self.source_search = QtWidgets.QLineEdit(self.mainwidget)
        self.source_search.setGeometry(QtCore.QRect(40, 100, 691, 31))
        self.source_search.setText("")
        self.source_search.setObjectName("source_search")
        self.progressBar = QtWidgets.QProgressBar(self.mainwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 580, 801, 31))
        self.progressBar.setMaximum(1000000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.btn_search = QtWidgets.QPushButton(self.mainwidget)
        self.btn_search.setEnabled(True)
        self.btn_search.setGeometry(QtCore.QRect(700, 100, 141, 31))
        self.btn_search.setObjectName("btn_search")
        self.btnclose = QtWidgets.QPushButton(self.mainwidget)
        self.btnclose.setGeometry(QtCore.QRect(840, 20, 16, 16))
        self.btnclose.setText("")
        self.btnclose.setFlat(True)
        self.btnclose.setObjectName("btnclose")
        self.btnmax = QtWidgets.QPushButton(self.mainwidget)
        self.btnmax.setGeometry(QtCore.QRect(810, 20, 16, 16))
        self.btnmax.setText("")
        self.btnmax.setFlat(True)
        self.btnmax.setObjectName("btnmax")
        self.btnmin = QtWidgets.QPushButton(self.mainwidget)
        self.btnmin.setGeometry(QtCore.QRect(780, 20, 16, 16))
        self.btnmin.setText("")
        self.btnmin.setFlat(True)
        self.btnmin.setObjectName("btnmin")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.mainwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 380, 801, 191))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox = QtWidgets.QGroupBox(self.mainwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(40, 140, 801, 231))
        self.groupBox.setObjectName("groupBox")
        self.btn_download = QtWidgets.QPushButton(self.groupBox)
        self.btn_download.setGeometry(QtCore.QRect(20, 180, 131, 31))
        self.btn_download.setObjectName("btn_download")
        self.checkBox_sym = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_sym.setGeometry(QtCore.QRect(300, 30, 131, 31))
        self.checkBox_sym.setObjectName("checkBox_sym")
        self.combo_vq = QtWidgets.QComboBox(self.groupBox)
        self.combo_vq.setGeometry(QtCore.QRect(110, 30, 151, 31))
        self.combo_vq.setCurrentText("")
        self.combo_vq.setObjectName("combo_vq")
        self.combo_aq = QtWidgets.QComboBox(self.groupBox)
        self.combo_aq.setGeometry(QtCore.QRect(110, 80, 151, 31))
        self.combo_aq.setCurrentText("")
        self.combo_aq.setObjectName("combo_aq")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 51, 31))
        self.label.setObjectName("label")
        self.media_list = QtWidgets.QListWidget(self.groupBox)
        self.media_list.setGeometry(QtCore.QRect(460, 61, 321, 151))
        self.media_list.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.media_list.setTabKeyNavigation(False)
        self.media_list.setDragEnabled(False)
        self.media_list.setMovement(QtWidgets.QListView.Static)
        self.media_list.setViewMode(QtWidgets.QListView.ListMode)
        self.media_list.setSelectionRectVisible(False)
        self.media_list.setObjectName("media_list")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(470, 20, 111, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_dir.setGeometry(QtCore.QRect(110, 130, 281, 31))
        self.lineEdit_dir.setText("")
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.label_4.setObjectName("label_4")
        self.btn_dir = QtWidgets.QPushButton(self.groupBox)
        self.btn_dir.setGeometry(QtCore.QRect(360, 130, 71, 31))
        self.btn_dir.setObjectName("btn_dir")
        self.btn_pause = QtWidgets.QPushButton(self.groupBox)
        self.btn_pause.setGeometry(QtCore.QRect(160, 180, 131, 31))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_stop = QtWidgets.QPushButton(self.groupBox)
        self.btn_stop.setGeometry(QtCore.QRect(300, 180, 131, 31))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_selectALL = QtWidgets.QPushButton(self.groupBox)
        self.btn_selectALL.setGeometry(QtCore.QRect(710, 20, 71, 31))
        self.btn_selectALL.setObjectName("btn_selectALL")
        self.checkBox_usecookie = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_usecookie.setGeometry(QtCore.QRect(300, 60, 141, 31))
        self.checkBox_usecookie.setObjectName("checkBox_usecookie")
        self.btn_changecookie = QtWidgets.QPushButton(self.groupBox)
        self.btn_changecookie.setGeometry(QtCore.QRect(300, 90, 131, 31))
        self.btn_changecookie.setObjectName("btn_changecookie")
        self.title = QtWidgets.QFrame(self.mainwidget)
        self.title.setGeometry(QtCore.QRect(40, 20, 371, 61))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.btn_about = QtWidgets.QPushButton(self.mainwidget)
        self.btn_about.setGeometry(QtCore.QRect(700, 60, 61, 31))
        self.btn_about.setObjectName("btn_about")
        self.btn_help = QtWidgets.QPushButton(self.mainwidget)
        self.btn_help.setGeometry(QtCore.QRect(780, 60, 61, 31))
        self.btn_help.setObjectName("btn_help")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnclose.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bili Downloader"))
        self.source_search.setPlaceholderText(_translate("MainWindow", "请填入视频页面HTTP/HTTPS地址"))
        self.btn_search.setText(_translate("MainWindow", "资源探查"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "欢迎使用Bili Downloader V1.3.20211016\n"
"Release at 2021/10/16 ......"))
        self.groupBox.setTitle(_translate("MainWindow", "操作框"))
        self.btn_download.setText(_translate("MainWindow", "下载资源"))
        self.checkBox_sym.setText(_translate("MainWindow", "FFMPEG合成"))
        self.label.setText(_translate("MainWindow", "清晰度"))
        self.media_list.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "音频清晰度"))
        self.label_3.setText(_translate("MainWindow", "媒体下载选择"))
        self.label_4.setText(_translate("MainWindow", "下载目录"))
        self.btn_dir.setText(_translate("MainWindow", "浏览"))
        self.btn_pause.setText(_translate("MainWindow", "暂停下载"))
        self.btn_stop.setText(_translate("MainWindow", "停止下载"))
        self.btn_selectALL.setText(_translate("MainWindow", "全选"))
        self.checkBox_usecookie.setText(_translate("MainWindow", "使用VIP Cookie"))
        self.btn_changecookie.setText(_translate("MainWindow", "修改Cookie"))
        self.btn_about.setText(_translate("MainWindow", "关于"))
        self.btn_help.setText(_translate("MainWindow", "帮助"))
import images_dl_rc
