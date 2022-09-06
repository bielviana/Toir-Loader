# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configEGPsoN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources.res_rc

class Ui_ConfigWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 740)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(940, 740))
        MainWindow.setStyleSheet(u"#configShadow {\n"
"	background-image: url(:/images/images/configShadow.png);\n"
"}\n"
"\n"
"#centralwidget #widget {\n"
"	background-color: #212121;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#configBody {\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#sidebar {\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#sidebar QPushButton {\n"
"	color: #ffffff;\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"}\n"
"#sidebar QPushButton:hover {\n"
"	color: #ffffff;\n"
"	background-color: #313131;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"}\n"
"\n"
"#configFrame QLabel {\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#configFrame #tab1{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#searchConfigFrame {\n"
"	background-color: #ffffff;\n"
"	border: 2px solid #d400ff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchConfigBtn {\n"
"	image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
""
                        "	border: none;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 6px;\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"#searchConfigBtn:hover {\n"
"	image: url(:/whiteIcons/images/whiteIcons/search.svg);\n"
"	background-color: #d400ff;\n"
"	border: none;\n"
"}\n"
"#searchConfigBtn:pressed {\n"
"	image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"	background-color: #212121;\n"
"	border-left: 2px solid #d400ff;\n"
"	border-bottom: 4px solid #d400ff;\n"
"}\n"
"\n"
"#searchConfigInput {\n"
"	color: #212121;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchFileFrame {\n"
"	background-color: #ffffff;\n"
"	border: 2px solid #d400ff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchFileBtn {\n"
"	image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 6px;\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"#searchFileBtn:hover {\n"
"	image: url(:/whiteIcons/images/whiteIcons/search.s"
                        "vg);\n"
"	background-color: #d400ff;\n"
"	border: none;\n"
"}\n"
"#searchFileBtn:pressed {\n"
"	image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"	background-color: #212121;\n"
"	border-left: 2px solid #d400ff;\n"
"	border-bottom: 4px solid #d400ff;\n"
"}\n"
"\n"
"#searchFileInput {\n"
"	color: #212121;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchAS1Frame {\n"
"	background-color: #ffffff;\n"
"	border: 2px solid #d400ff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchAS1Btn {\n"
"	image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"	border: none;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 6px;\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"#searchAS1Btn:hover {\n"
"	image: url(:/whiteIcons/images/whiteIcons/search.svg);\n"
"	background-color: #d400ff;\n"
"	border: none;\n"
"}\n"
"#searchAS1Btn:pressed {\n"
"	image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"	background-color: #212121;\n"
"	border-left: 2px soli"
                        "d #d400ff;\n"
"	border-bottom: 4px solid #d400ff;\n"
"}\n"
"\n"
"#searchAS1Input {\n"
"	color: #212121;\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#configFrame #tab2 {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"#saveBtn {\n"
"	background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"	border-radius: 5px;\n"
"	color: #212121;\n"
"}\n"
"#saveBtn:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"	border: 2px solid #d400ff;\n"
"	color: #d400ff;\n"
"}\n"
"#saveBtn:pressed {\n"
"	background-color: #212121;\n"
"	border: 2px solid #d400ff;\n"
"	color: #d400ff;\n"
"}\n"
"\n"
"#cancelBtn {\n"
"	background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"	border-radius"
                        ": 5px;\n"
"	color: #212121;\n"
"}\n"
"#cancelBtn:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"	border: 2px solid #d400ff;\n"
"	color: #d400ff;\n"
"}\n"
"#cancelBtn:pressed {\n"
"	background-color: #212121;\n"
"	border: 2px solid #d400ff;\n"
"	color: #d400ff;\n"
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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 900, 700))
        self.widget.setMinimumSize(QSize(900, 700))
        self.widget.setMaximumSize(QSize(900, 700))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.label.setPixmap(QPixmap(u":/purpleIcons/images/purpleIcons/settings.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.label)

        self.tileTitle = QLabel(self.titleBar)
        self.tileTitle.setObjectName(u"tileTitle")
        self.tileTitle.setEnabled(False)
        self.tileTitle.setMaximumSize(QSize(90, 16777215))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
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

        self.body = QWidget(self.widget)
        self.body.setObjectName(u"body")
        self.horizontalLayout_3 = QHBoxLayout(self.body)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.sidebar = QFrame(self.body)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMaximumSize(QSize(200, 16777215))
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.generalBtn = QPushButton(self.sidebar)
        self.generalBtn.setObjectName(u"generalBtn")
        self.generalBtn.setMinimumSize(QSize(200, 50))
        self.generalBtn.setMaximumSize(QSize(200, 50))
        font2 = QFont()
        font2.setPointSize(14)
        self.generalBtn.setFont(font2)

        self.verticalLayout_2.addWidget(self.generalBtn)

        self.line = QFrame(self.sidebar)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: #313131;")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.profilesBtn = QPushButton(self.sidebar)
        self.profilesBtn.setObjectName(u"profilesBtn")
        self.profilesBtn.setMinimumSize(QSize(200, 50))
        self.profilesBtn.setMaximumSize(QSize(200, 50))
        self.profilesBtn.setFont(font2)

        self.verticalLayout_2.addWidget(self.profilesBtn)


        self.horizontalLayout_3.addWidget(self.sidebar, 0, Qt.AlignTop)

        self.separator = QFrame(self.body)
        self.separator.setObjectName(u"separator")
        self.separator.setStyleSheet(u"background-color: #313131;")
        self.separator.setFrameShadow(QFrame.Sunken)
        self.separator.setMidLineWidth(0)
        self.separator.setFrameShape(QFrame.VLine)

        self.horizontalLayout_3.addWidget(self.separator)

        self.configBody = QFrame(self.body)
        self.configBody.setObjectName(u"configBody")
        self.configBody.setFrameShape(QFrame.StyledPanel)
        self.configBody.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.configBody)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.configFrame = QFrame(self.configBody)
        self.configFrame.setObjectName(u"configFrame")
        self.configFrame.setMinimumSize(QSize(0, 600))
        self.configFrame.setMaximumSize(QSize(16777215, 600))
        self.configFrame.setFrameShape(QFrame.StyledPanel)
        self.configFrame.setFrameShadow(QFrame.Raised)
        self.configFrame.setLineWidth(0)
        self.tab1 = QFrame(self.configFrame)
        self.tab1.setObjectName(u"tab1")
        self.tab1.setGeometry(QRect(0, 0, 657, 600))
        self.tab1.setMinimumSize(QSize(657, 600))
        self.tab1.setMaximumSize(QSize(657, 600))
        self.tab1.setStyleSheet(u"")
        self.tab1.setFrameShape(QFrame.StyledPanel)
        self.tab1.setFrameShadow(QFrame.Raised)
        self.tab1.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.tab1)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.tab1_top_frame = QFrame(self.tab1)
        self.tab1_top_frame.setObjectName(u"tab1_top_frame")
        self.tab1_top_frame.setFrameShape(QFrame.StyledPanel)
        self.tab1_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.tab1_top_frame)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tab1_line1 = QWidget(self.tab1_top_frame)
        self.tab1_line1.setObjectName(u"tab1_line1")
        self.verticalLayout_8 = QVBoxLayout(self.tab1_line1)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.searchFileLabel = QLabel(self.tab1_line1)
        self.searchFileLabel.setObjectName(u"searchFileLabel")
        self.searchFileLabel.setFont(font2)

        self.verticalLayout_8.addWidget(self.searchFileLabel)

        self.searchFileFrame = QFrame(self.tab1_line1)
        self.searchFileFrame.setObjectName(u"searchFileFrame")
        self.searchFileFrame.setMinimumSize(QSize(0, 40))
        self.searchFileFrame.setMaximumSize(QSize(16777215, 40))
        self.searchFileFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFileFrame.setFrameShadow(QFrame.Raised)
        self.searchFileFrame.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFileFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.searchFileInput = QLineEdit(self.searchFileFrame)
        self.searchFileInput.setObjectName(u"searchFileInput")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.searchFileInput.sizePolicy().hasHeightForWidth())
        self.searchFileInput.setSizePolicy(sizePolicy)
        self.searchFileInput.setMinimumSize(QSize(0, 0))
        self.searchFileInput.setFont(font2)

        self.horizontalLayout_5.addWidget(self.searchFileInput)

        self.searchFileBtn = QPushButton(self.searchFileFrame)
        self.searchFileBtn.setObjectName(u"searchFileBtn")
        self.searchFileBtn.setMinimumSize(QSize(40, 40))
        self.searchFileBtn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.searchFileBtn)


        self.verticalLayout_8.addWidget(self.searchFileFrame)


        self.verticalLayout_7.addWidget(self.tab1_line1, 0, Qt.AlignTop)

        self.tab1_line4 = QWidget(self.tab1_top_frame)
        self.tab1_line4.setObjectName(u"tab1_line4")
        self.horizontalLayout_6 = QHBoxLayout(self.tab1_line4)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.customConfigLabel = QLabel(self.tab1_line4)
        self.customConfigLabel.setObjectName(u"customConfigLabel")
        self.customConfigLabel.setFont(font2)

        self.horizontalLayout_6.addWidget(self.customConfigLabel, 0, Qt.AlignLeft)

        self.customConfigCheckBox = QCheckBox(self.tab1_line4)
        self.customConfigCheckBox.setObjectName(u"customConfigCheckBox")
        self.customConfigCheckBox.setChecked(True)

        self.horizontalLayout_6.addWidget(self.customConfigCheckBox, 0, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.tab1_line4)

        self.tab1_line2 = QWidget(self.tab1_top_frame)
        self.tab1_line2.setObjectName(u"tab1_line2")
        self.verticalLayout_9 = QVBoxLayout(self.tab1_line2)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.searchConfigLabel = QLabel(self.tab1_line2)
        self.searchConfigLabel.setObjectName(u"searchConfigLabel")
        self.searchConfigLabel.setFont(font2)

        self.verticalLayout_9.addWidget(self.searchConfigLabel)

        self.searchConfigFrame = QFrame(self.tab1_line2)
        self.searchConfigFrame.setObjectName(u"searchConfigFrame")
        self.searchConfigFrame.setMinimumSize(QSize(0, 40))
        self.searchConfigFrame.setMaximumSize(QSize(16777215, 40))
        self.searchConfigFrame.setFrameShape(QFrame.StyledPanel)
        self.searchConfigFrame.setFrameShadow(QFrame.Raised)
        self.searchConfigFrame.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.searchConfigFrame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.searchConfigInput = QLineEdit(self.searchConfigFrame)
        self.searchConfigInput.setObjectName(u"searchConfigInput")
        sizePolicy.setHeightForWidth(self.searchConfigInput.sizePolicy().hasHeightForWidth())
        self.searchConfigInput.setSizePolicy(sizePolicy)
        self.searchConfigInput.setMinimumSize(QSize(0, 0))
        self.searchConfigInput.setFont(font2)

        self.horizontalLayout_8.addWidget(self.searchConfigInput)

        self.searchConfigBtn = QPushButton(self.searchConfigFrame)
        self.searchConfigBtn.setObjectName(u"searchConfigBtn")
        self.searchConfigBtn.setMinimumSize(QSize(40, 40))
        self.searchConfigBtn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.searchConfigBtn)


        self.verticalLayout_9.addWidget(self.searchConfigFrame)


        self.verticalLayout_7.addWidget(self.tab1_line2, 0, Qt.AlignTop)

        self.tab1_line3 = QWidget(self.tab1_top_frame)
        self.tab1_line3.setObjectName(u"tab1_line3")
        self.verticalLayout_11 = QVBoxLayout(self.tab1_line3)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.searchAS1Label = QLabel(self.tab1_line3)
        self.searchAS1Label.setObjectName(u"searchAS1Label")
        self.searchAS1Label.setFont(font2)

        self.verticalLayout_11.addWidget(self.searchAS1Label)

        self.searchAS1Frame = QFrame(self.tab1_line3)
        self.searchAS1Frame.setObjectName(u"searchAS1Frame")
        self.searchAS1Frame.setMinimumSize(QSize(0, 40))
        self.searchAS1Frame.setMaximumSize(QSize(16777215, 40))
        self.searchAS1Frame.setFrameShape(QFrame.StyledPanel)
        self.searchAS1Frame.setFrameShadow(QFrame.Raised)
        self.searchAS1Frame.setLineWidth(0)
        self.horizontalLayout_10 = QHBoxLayout(self.searchAS1Frame)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 0, 0)
        self.searchAS1Input = QLineEdit(self.searchAS1Frame)
        self.searchAS1Input.setObjectName(u"searchAS1Input")
        sizePolicy.setHeightForWidth(self.searchAS1Input.sizePolicy().hasHeightForWidth())
        self.searchAS1Input.setSizePolicy(sizePolicy)
        self.searchAS1Input.setMinimumSize(QSize(0, 0))
        self.searchAS1Input.setFont(font2)

        self.horizontalLayout_10.addWidget(self.searchAS1Input)

        self.searchAS1Btn = QPushButton(self.searchAS1Frame)
        self.searchAS1Btn.setObjectName(u"searchAS1Btn")
        self.searchAS1Btn.setMinimumSize(QSize(40, 40))
        self.searchAS1Btn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_10.addWidget(self.searchAS1Btn)


        self.verticalLayout_11.addWidget(self.searchAS1Frame)


        self.verticalLayout_7.addWidget(self.tab1_line3)


        self.verticalLayout_4.addWidget(self.tab1_top_frame, 0, Qt.AlignTop)

        self.tab1_bottom_frame = QFrame(self.tab1)
        self.tab1_bottom_frame.setObjectName(u"tab1_bottom_frame")
        self.tab1_bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.tab1_bottom_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.tab1_bottom_frame, 0, Qt.AlignBottom)

        self.tab2 = QFrame(self.configFrame)
        self.tab2.setObjectName(u"tab2")
        self.tab2.setGeometry(QRect(0, 0, 657, 600))
        self.tab2.setMinimumSize(QSize(657, 600))
        self.tab2.setMaximumSize(QSize(657, 600))
        self.tab2.setStyleSheet(u"")
        self.tab2.setFrameShape(QFrame.StyledPanel)
        self.tab2.setFrameShadow(QFrame.Raised)
        self.tab2.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.tab2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.label_2 = QLabel(self.tab2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignTop)

        self.tab2.raise_()
        self.tab1.raise_()

        self.verticalLayout_5.addWidget(self.configFrame)

        self.configBtns = QFrame(self.configBody)
        self.configBtns.setObjectName(u"configBtns")
        self.configBtns.setMinimumSize(QSize(0, 50))
        self.configBtns.setMaximumSize(QSize(16777215, 50))
        self.configBtns.setLayoutDirection(Qt.LeftToRight)
        self.configBtns.setFrameShape(QFrame.StyledPanel)
        self.configBtns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.configBtns)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.saveBtn = QPushButton(self.configBtns)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(100, 40))
        self.saveBtn.setMaximumSize(QSize(100, 40))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.saveBtn.setFont(font3)

        self.horizontalLayout_4.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(self.configBtns)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(100, 40))
        self.cancelBtn.setMaximumSize(QSize(100, 40))
        self.cancelBtn.setFont(font2)

        self.horizontalLayout_4.addWidget(self.cancelBtn)


        self.verticalLayout_5.addWidget(self.configBtns, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.configBody)


        self.verticalLayout.addWidget(self.body)

        self.configShadow = QFrame(self.centralwidget)
        self.configShadow.setObjectName(u"configShadow")
        self.configShadow.setGeometry(QRect(0, 0, 940, 740))
        self.configShadow.setFrameShape(QFrame.StyledPanel)
        self.configShadow.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.configShadow.raise_()
        self.widget.raise_()

        self.retranslateUi(MainWindow)

        self.configBtn.setDefault(False)
        self.minimizeBtn.setDefault(False)
        self.closeBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.label.setText("")
        self.tileTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Configuration</span></p></body></html>", None))
        self.configBtn.setText("")
        self.minimizeBtn.setText("")
        self.closeBtn.setText("")
        self.generalBtn.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.profilesBtn.setText(QCoreApplication.translate("MainWindow", u"Profiles", None))
        self.searchFileLabel.setText(QCoreApplication.translate("MainWindow", u"Toir Executable:", None))
        self.searchFileInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click on the search icon and select the Toir executable...", None))
        self.searchFileBtn.setText("")
        self.customConfigLabel.setText(QCoreApplication.translate("MainWindow", u"Use custom profile:", None))
        self.customConfigCheckBox.setText("")
        self.searchConfigLabel.setText(QCoreApplication.translate("MainWindow", u"Custom Config File:", None))
        self.searchConfigInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click on the search icon and select the custom config file...", None))
        self.searchConfigBtn.setText("")
        self.searchAS1Label.setText(QCoreApplication.translate("MainWindow", u"Toir config path (Example: C:\\Program Files\\AS1...config):", None))
        self.searchAS1Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click on the search icon and select the custom config file...", None))
        self.searchAS1Btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Coming soon...", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.cancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

