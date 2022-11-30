import resources.res_rc

from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 238)
        MainWindow.setMinimumSize(QtCore.QSize(368, 238))
        MainWindow.setMaximumSize(QtCore.QSize(368, 238))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget #widget {\n"
"    background-color: #212121;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#centralwidget #shadowImg {\n"
"    background-image: url(:/images/images/shadow.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"#loadBtn {\n"
"    background-color: #212121;\n"
"    color: #d400ff;\n"
"    border: 2px solid #d400ff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#loadBtn:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"    color: #ffffff;\n"
"    border: 2px solid #ffffff;\n"
"}\n"
"\n"
"#loadBtn:pressed {\n"
"    background-color: #212121;\n"
"    color: #313131;\n"
"    border: 2px solid #313131;\n"
"}\n"
"\n"
"#footer QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"    color: #212121;\n"
"    border-radius: 18px;\n"
"}\n"
"#footer QPushButton:hover {\n"
"    color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"    background-color: #ffffff;\n"
"}\n"
"#footer QPushButton:pressed {\n"
"    background-color: #313131;\n"
"    color: #212121;\n"
"}\n"
"\n"
"#statusLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#titleBar QPushButton {\n"
"    background-color: transparent;\n"
"    border: 0;\n"
"}\n"
"\n"
"#titleBar {\n"
"    background-color: #313131;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#closeBtn {\n"
"    image: url(:/purpleIcons/images/purpleIcons/x.svg);\n"
"}\n"
"#closeBtn:hover {\n"
"    image: url(:/whiteIcons/images/whiteIcons/x.svg);\n"
"}\n"
"\n"
"#minimizeBtn {\n"
"    image: url(:/purpleIcons/images/purpleIcons/minimize-2.svg);\n"
"}\n"
"#minimizeBtn:hover {\n"
"    image: url(:/whiteIcons/images/whiteIcons/minimize-2.svg);\n"
"}\n"
"\n"
"#configBtn {\n"
"    image: url(:/purpleIcons/images/purpleIcons/settings.svg);\n"
"}\n"
"#configBtn:hover {\n"
"    image: url(:/whiteIcons/images/whiteIcons/settings.svg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.shadowImg = QtWidgets.QFrame(self.centralwidget)
        self.shadowImg.setGeometry(QtCore.QRect(0, 0, 368, 238))
        self.shadowImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shadowImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shadowImg.setObjectName("shadowImg")
        self.widget = QtWidgets.QWidget(self.shadowImg)
        self.widget.setGeometry(QtCore.QRect(19, 19, 330, 200))
        self.widget.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QFrame(self.widget)
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleBar)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.titleBar)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/images/icon.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tileTitle = QtWidgets.QLabel(self.titleBar)
        self.tileTitle.setEnabled(False)
        self.tileTitle.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tileTitle.setFont(font)
        self.tileTitle.setScaledContents(True)
        self.tileTitle.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.tileTitle.setObjectName("tileTitle")
        self.horizontalLayout.addWidget(self.tileTitle)
        self.frame = QtWidgets.QFrame(self.titleBar)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.configBtn = QtWidgets.QPushButton(self.frame)
        self.configBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.configBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.configBtn.setText("")
        self.configBtn.setIconSize(QtCore.QSize(24, 24))
        self.configBtn.setAutoDefault(False)
        self.configBtn.setDefault(False)
        self.configBtn.setFlat(False)
        self.configBtn.setObjectName("configBtn")
        self.horizontalLayout_2.addWidget(self.configBtn)
        self.minimizeBtn = QtWidgets.QPushButton(self.frame)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.minimizeBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.minimizeBtn.setText("")
        self.minimizeBtn.setIconSize(QtCore.QSize(24, 24))
        self.minimizeBtn.setAutoDefault(False)
        self.minimizeBtn.setDefault(False)
        self.minimizeBtn.setFlat(False)
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_2.addWidget(self.minimizeBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame)
        self.closeBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.closeBtn.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.closeBtn.setFont(font)
        self.closeBtn.setText("")
        self.closeBtn.setIconSize(QtCore.QSize(24, 24))
        self.closeBtn.setAutoDefault(False)
        self.closeBtn.setDefault(False)
        self.closeBtn.setFlat(False)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.titleBar)
        self.header = QtWidgets.QHBoxLayout()
        self.header.setSpacing(0)
        self.header.setObjectName("header")
        self.statusLabel = QtWidgets.QLabel(self.widget)
        self.statusLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.statusLabel.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.statusLabel.setObjectName("statusLabel")
        self.header.addWidget(self.statusLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.header)
        self.body = QtWidgets.QHBoxLayout()
        self.body.setSpacing(0)
        self.body.setObjectName("body")
        self.loadBtn = QtWidgets.QPushButton(self.widget)
        self.loadBtn.setMinimumSize(QtCore.QSize(170, 40))
        self.loadBtn.setMaximumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.loadBtn.setFont(font)
        self.loadBtn.setObjectName("loadBtn")
        self.body.addWidget(self.loadBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.body)
        self.footer = QtWidgets.QFrame(self.widget)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.footerLinks = QtWidgets.QHBoxLayout()
        self.footerLinks.setSpacing(0)
        self.footerLinks.setObjectName("footerLinks")
        self.discBtn = QtWidgets.QPushButton(self.footer)
        self.discBtn.setMinimumSize(QtCore.QSize(36, 36))
        self.discBtn.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.discBtn.setFont(font)
        self.discBtn.setObjectName("discBtn")
        self.footerLinks.addWidget(self.discBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ttBtn = QtWidgets.QPushButton(self.footer)
        self.ttBtn.setMinimumSize(QtCore.QSize(36, 36))
        self.ttBtn.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.ttBtn.setFont(font)
        self.ttBtn.setObjectName("ttBtn")
        self.footerLinks.addWidget(self.ttBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gitBtn = QtWidgets.QPushButton(self.footer)
        self.gitBtn.setMinimumSize(QtCore.QSize(36, 36))
        self.gitBtn.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.gitBtn.setFont(font)
        self.gitBtn.setObjectName("gitBtn")
        self.footerLinks.addWidget(self.gitBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ppBtn = QtWidgets.QPushButton(self.footer)
        self.ppBtn.setMinimumSize(QtCore.QSize(36, 36))
        self.ppBtn.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.ppBtn.setFont(font)
        self.ppBtn.setObjectName("ppBtn")
        self.footerLinks.addWidget(self.ppBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addLayout(self.footerLinks)
        self.verticalLayout.addWidget(self.footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Toir Loader"))
        self.tileTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Toir Loader</span></p></body></html>"))
        self.statusLabel.setText(_translate("MainWindow", "Toir is not open!"))
        self.loadBtn.setText(_translate("MainWindow", "LOAD"))
        self.discBtn.setText(_translate("MainWindow", "Y"))
        self.ttBtn.setText(_translate("MainWindow", "D"))
        self.gitBtn.setText(_translate("MainWindow", ")"))
        self.ppBtn.setText(_translate("MainWindow", "Z"))
