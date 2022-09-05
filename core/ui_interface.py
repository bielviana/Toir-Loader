# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceDOxjXN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(368, 238)
        MainWindow.setMinimumSize(QSize(368, 238))
        MainWindow.setMaximumSize(QSize(368, 238))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/images/toirOff.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#centralwidget #widget {\n"
"	background-color: #212121;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#centralwidget #shadowImg {\n"
"	background-image: url(:/images/images/shadow.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#loadBtn {\n"
"	background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"	border-radius: 5px;\n"
"	color: #212121;\n"
"}\n"
"#loadBtn:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"	border: 2px solid #d400ff;\n"
"	color: #d400ff;\n"
"}\n"
"#loadBtn:pressed {\n"
"	background-color: #212121;\n"
"	border: 2px solid #d400ff;\n"
"	color: #d400ff;\n"
"}\n"
"\n"
"#footer QPushButton {\n"
"	color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"	background-color: #212121;\n"
"	border-"
                        "radius: 18px;\n"
"}\n"
"#footer QPushButton:hover {\n"
"	color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"	background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"}\n"
"#footer QPushButton:pressed {\n"
"	color: #212121;\n"
"}\n"
"\n"
"#statusLabel {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#titleBar QPushButton {\n"
"	background-color: transparent;\n"
"	border: 0;\n"
"}\n"
"\n"
"#titleBar {\n"
"	background-color: #313131;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#closeBtn {\n"
"	image: url(:/purpleIcons/images/purpleIcons/x.svg);\n"
"}\n"
"#closeBtn:hover {\n"
"	image: url(:/whiteIcons/images/whiteIcons/x.svg);\n"
"}\n"
"\n"
"#minimizeBtn {\n"
"	image: url(:/purpleIcons/images/purpleIcons/minimize-2.svg);\n"
"}\n"
"#minimizeBtn:hover {\n"
"	image: url(:/whiteIcons/images/whiteIcons/minimize-2.svg);\n"
""
                        "}\n"
"\n"
"#configBtn {\n"
"	image: url(:/purpleIcons/images/purpleIcons/settings.svg);\n"
"}\n"
"#configBtn:hover {\n"
"	image: url(:/whiteIcons/images/whiteIcons/settings.svg);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.shadowImg = QFrame(self.centralwidget)
        self.shadowImg.setObjectName(u"shadowImg")
        self.shadowImg.setGeometry(QRect(0, 0, 368, 238))
        self.shadowImg.setFrameShape(QFrame.StyledPanel)
        self.shadowImg.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.shadowImg)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(19, 19, 330, 200))
        self.widget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.titleBar = QFrame(self.widget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 30))
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.label = QLabel(self.titleBar)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(20, 20))
        self.label.setPixmap(QPixmap(u":/images/images/toirOff.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.label)

        self.tileTitle = QLabel(self.titleBar)
        self.tileTitle.setObjectName(u"tileTitle")
        self.tileTitle.setEnabled(False)
        self.tileTitle.setMaximumSize(QSize(75, 16777215))
        self.tileTitle.setFont(font)
        self.tileTitle.setScaledContents(True)
        self.tileTitle.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.tileTitle)

        self.frame = QFrame(self.titleBar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.configBtn = QPushButton(self.frame)
        self.configBtn.setObjectName(u"configBtn")
        self.configBtn.setMinimumSize(QSize(0, 0))
        self.configBtn.setMaximumSize(QSize(18, 18))
        self.configBtn.setIconSize(QSize(24, 24))
        self.configBtn.setAutoDefault(False)
        self.configBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.configBtn)

        self.minimizeBtn = QPushButton(self.frame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(20, 20))
        self.minimizeBtn.setMaximumSize(QSize(20, 20))
        self.minimizeBtn.setIconSize(QSize(24, 24))
        self.minimizeBtn.setAutoDefault(False)
        self.minimizeBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.minimizeBtn)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(0, 20))
        self.closeBtn.setMaximumSize(QSize(200, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.closeBtn.setFont(font1)
        self.closeBtn.setIconSize(QSize(24, 24))
        self.closeBtn.setAutoDefault(False)
        self.closeBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.titleBar)

        self.header = QHBoxLayout()
        self.header.setSpacing(0)
        self.header.setObjectName(u"header")
        self.statusLabel = QLabel(self.widget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(0, 0))
        self.statusLabel.setMaximumSize(QSize(280, 30))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.statusLabel.setFont(font2)
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.header.addWidget(self.statusLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.header)

        self.body = QHBoxLayout()
        self.body.setSpacing(0)
        self.body.setObjectName(u"body")
        self.loadBtn = QPushButton(self.widget)
        self.loadBtn.setObjectName(u"loadBtn")
        self.loadBtn.setMinimumSize(QSize(170, 40))
        self.loadBtn.setMaximumSize(QSize(170, 40))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setWeight(75)
        self.loadBtn.setFont(font3)

        self.body.addWidget(self.loadBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.body)

        self.footer = QFrame(self.widget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.footer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.footerLinks = QHBoxLayout()
        self.footerLinks.setSpacing(0)
        self.footerLinks.setObjectName(u"footerLinks")
        self.discBtn = QPushButton(self.footer)
        self.discBtn.setObjectName(u"discBtn")
        self.discBtn.setMinimumSize(QSize(36, 36))
        self.discBtn.setMaximumSize(QSize(36, 36))
        font4 = QFont()
        font4.setFamily(u"Social Media Circled")
        font4.setPointSize(24)
        self.discBtn.setFont(font4)

        self.footerLinks.addWidget(self.discBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.ttBtn = QPushButton(self.footer)
        self.ttBtn.setObjectName(u"ttBtn")
        self.ttBtn.setMinimumSize(QSize(36, 36))
        self.ttBtn.setMaximumSize(QSize(36, 36))
        self.ttBtn.setFont(font4)

        self.footerLinks.addWidget(self.ttBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gitBtn = QPushButton(self.footer)
        self.gitBtn.setObjectName(u"gitBtn")
        self.gitBtn.setMinimumSize(QSize(36, 36))
        self.gitBtn.setMaximumSize(QSize(36, 36))
        self.gitBtn.setFont(font4)

        self.footerLinks.addWidget(self.gitBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.ppBtn = QPushButton(self.footer)
        self.ppBtn.setObjectName(u"ppBtn")
        self.ppBtn.setMinimumSize(QSize(36, 36))
        self.ppBtn.setMaximumSize(QSize(36, 36))
        self.ppBtn.setFont(font4)

        self.footerLinks.addWidget(self.ppBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.footerLinks)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.configBtn.setDefault(False)
        self.minimizeBtn.setDefault(False)
        self.closeBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Toir Loader", None))
        self.label.setText("")
        self.tileTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Toir Loader</span></p></body></html>", None))
        self.configBtn.setText("")
        self.minimizeBtn.setText("")
        self.closeBtn.setText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Toir Infinity is not open!", None))
        self.loadBtn.setText(QCoreApplication.translate("MainWindow", u"LOAD", None))
        self.discBtn.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.ttBtn.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.gitBtn.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.ppBtn.setText(QCoreApplication.translate("MainWindow", u"Z", None))
    # retranslateUi
