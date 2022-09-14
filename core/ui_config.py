import resources.res_rc

from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import *

class Ui_ConfigWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 740)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(940, 740))
        MainWindow.setStyleSheet("#configShadow {\n"
"    background-image: url(:/images/images/configShadow.png);\n"
"}\n"
"\n"
"#centralwidget #widget {\n"
"    background-color: #212121;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#configBody {\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#sidebar {\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#sidebar QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"#sidebar QPushButton:hover {\n"
"    color: #ffffff;\n"
"    background-color: #313131;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"#configFrame QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#configFrame #tab1{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"#searchConfigFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"    border: 2px solid #d400ff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#searchConfigBtn {\n"
"    image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 6px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"#searchConfigBtn:hover {\n"
"    image: url(:/whiteIcons/images/whiteIcons/search.svg);\n"
"    background-color: #d400ff;\n"
"    border: none;\n"
"}\n"
"#searchConfigBtn:pressed {\n"
"    image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"    background-color: #212121;\n"
"    border-left: 2px solid #d400ff;\n"
"    border-bottom: 4px solid #d400ff;\n"
"}\n"
"\n"
"#searchConfigInput {\n"
"    color: #212121;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#searchFileFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"    border: 2px solid #d400ff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#searchFileBtn {\n"
"    image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 6px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"#searchFileBtn:hover {\n"
"    image: url(:/whiteIcons/images/whiteIcons/search.svg);\n"
"    background-color: #d400ff;\n"
"    border: none;\n"
"}\n"
"#searchFileBtn:pressed {\n"
"    image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"    background-color: #212121;\n"
"    border-left: 2px solid #d400ff;\n"
"    border-bottom: 4px solid #d400ff;\n"
"}\n"
"\n"
"#searchFileInput {\n"
"    color: #212121;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#searchAS1Frame {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(212, 212, 212, 255));\n"
"    border: 2px solid #d400ff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#searchAS1Btn {\n"
"    image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"    border: none;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 6px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"#searchAS1Btn:hover {\n"
"    image: url(:/whiteIcons/images/whiteIcons/search.svg);\n"
"    background-color: #d400ff;\n"
"    border: none;\n"
"}\n"
"#searchAS1Btn:pressed {\n"
"    image: url(:/purpleIcons/images/purpleIcons/search.svg);\n"
"    background-color: #212121;\n"
"    border-left: 2px solid #d400ff;\n"
"    border-bottom: 4px solid #d400ff;\n"
"}\n"
"\n"
"#searchAS1Input {\n"
"    color: #212121;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#useCCBtn {\n"
"    background-color: #212121;\n"
"    color: #d400ff;\n"
"    border: 2px solid #d400ff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#useCCBtn:hover {\n"
"    background-color: #313131;\n"
"}\n"
"\n"
"#useCCBtn:pressed {\n"
"    background-color: #212121;\n"
"    color: #313131;\n"
"    border: 2px solid #313131;\n"
"}\n"
"\n"
"#configFrame #tab2 {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"#configBtns QPushButton {\n"
"    background-color: #212121;\n"
"    color: #d400ff;\n"
"    border: 2px solid #d400ff;\n"
"    border-radius: 5px;\n"
"}\n"
"#configBtns QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489, y1:0, x2:0.511, y2:1, stop:0 rgba(212, 0, 255, 255), stop:1 rgba(155, 0, 194, 255));\n"
"    color: #ffffff;\n"
"    border: 2px solid #ffffff;\n"
"}\n"
"#configBtns QPushButton:pressed {\n"
"    background-color: #212121;\n"
"    color: #313131;\n"
"    border: 2px solid #313131;\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 900, 700))
        self.widget.setMinimumSize(QtCore.QSize(900, 700))
        self.widget.setMaximumSize(QtCore.QSize(900, 700))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.label.setPixmap(QtGui.QPixmap(":/purpleIcons/images/purpleIcons/settings.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.tileTitle = QtWidgets.QLabel(self.titleBar)
        self.tileTitle.setEnabled(False)
        self.tileTitle.setMaximumSize(QtCore.QSize(90, 16777215))
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
        self.body = QtWidgets.QWidget(self.widget)
        self.body.setObjectName("body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sidebar = QtWidgets.QFrame(self.body)
        self.sidebar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.generalBtn = QtWidgets.QPushButton(self.sidebar)
        self.generalBtn.setMinimumSize(QtCore.QSize(200, 50))
        self.generalBtn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generalBtn.setFont(font)
        self.generalBtn.setObjectName("generalBtn")
        self.verticalLayout_2.addWidget(self.generalBtn)
        self.line = QtWidgets.QFrame(self.sidebar)
        self.line.setStyleSheet("background-color: #313131;")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.profilesBtn = QtWidgets.QPushButton(self.sidebar)
        self.profilesBtn.setMinimumSize(QtCore.QSize(200, 50))
        self.profilesBtn.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.profilesBtn.setFont(font)
        self.profilesBtn.setObjectName("profilesBtn")
        self.verticalLayout_2.addWidget(self.profilesBtn)
        self.horizontalLayout_3.addWidget(self.sidebar, 0, QtCore.Qt.AlignTop)
        self.separator = QtWidgets.QFrame(self.body)
        self.separator.setStyleSheet("background-color: #313131;")
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setMidLineWidth(0)
        self.separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator.setObjectName("separator")
        self.horizontalLayout_3.addWidget(self.separator)
        self.configBody = QtWidgets.QFrame(self.body)
        self.configBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configBody.setObjectName("configBody")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.configBody)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.configFrame = QtWidgets.QFrame(self.configBody)
        self.configFrame.setMinimumSize(QtCore.QSize(0, 600))
        self.configFrame.setMaximumSize(QtCore.QSize(16777215, 600))
        self.configFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configFrame.setLineWidth(0)
        self.configFrame.setObjectName("configFrame")
        self.tab1 = QtWidgets.QFrame(self.configFrame)
        self.tab1.setGeometry(QtCore.QRect(0, 0, 657, 600))
        self.tab1.setMinimumSize(QtCore.QSize(657, 600))
        self.tab1.setMaximumSize(QtCore.QSize(657, 600))
        self.tab1.setStyleSheet("")
        self.tab1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab1.setLineWidth(0)
        self.tab1.setObjectName("tab1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab1_top_frame = QtWidgets.QFrame(self.tab1)
        self.tab1_top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab1_top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab1_top_frame.setObjectName("tab1_top_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab1_top_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tab1_line1 = QtWidgets.QWidget(self.tab1_top_frame)
        self.tab1_line1.setObjectName("tab1_line1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab1_line1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.searchFileLabel = QtWidgets.QLabel(self.tab1_line1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchFileLabel.setFont(font)
        self.searchFileLabel.setObjectName("searchFileLabel")
        self.verticalLayout_8.addWidget(self.searchFileLabel)
        self.searchFileFrame = QtWidgets.QFrame(self.tab1_line1)
        self.searchFileFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.searchFileFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.searchFileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFileFrame.setLineWidth(0)
        self.searchFileFrame.setObjectName("searchFileFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.searchFileFrame)
        self.horizontalLayout_5.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchFileInput = QtWidgets.QLineEdit(self.searchFileFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.searchFileInput.sizePolicy().hasHeightForWidth())
        self.searchFileInput.setSizePolicy(sizePolicy)
        self.searchFileInput.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchFileInput.setFont(font)
        self.searchFileInput.setObjectName("searchFileInput")
        self.horizontalLayout_5.addWidget(self.searchFileInput)
        self.searchFileBtn = QtWidgets.QPushButton(self.searchFileFrame)
        self.searchFileBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.searchFileBtn.setMaximumSize(QtCore.QSize(40, 40))
        self.searchFileBtn.setText("")
        self.searchFileBtn.setObjectName("searchFileBtn")
        self.horizontalLayout_5.addWidget(self.searchFileBtn)
        self.verticalLayout_8.addWidget(self.searchFileFrame)
        self.verticalLayout_7.addWidget(self.tab1_line1, 0, QtCore.Qt.AlignTop)
        self.tab1_line4 = QtWidgets.QWidget(self.tab1_top_frame)
        self.tab1_line4.setObjectName("tab1_line4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab1_line4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.useCCBtn = QtWidgets.QPushButton(self.tab1_line4)
        self.useCCBtn.setMinimumSize(QtCore.QSize(220, 40))
        self.useCCBtn.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.useCCBtn.setFont(font)
        self.useCCBtn.setObjectName("useCCBtn")
        self.horizontalLayout_6.addWidget(self.useCCBtn)
        self.verticalLayout_7.addWidget(self.tab1_line4, 0, QtCore.Qt.AlignLeft)
        self.tab1_line2 = QtWidgets.QWidget(self.tab1_top_frame)
        self.tab1_line2.setObjectName("tab1_line2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab1_line2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.searchConfigLabel = QtWidgets.QLabel(self.tab1_line2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchConfigLabel.setFont(font)
        self.searchConfigLabel.setObjectName("searchConfigLabel")
        self.verticalLayout_9.addWidget(self.searchConfigLabel)
        self.searchConfigFrame = QtWidgets.QFrame(self.tab1_line2)
        self.searchConfigFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.searchConfigFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.searchConfigFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchConfigFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchConfigFrame.setLineWidth(0)
        self.searchConfigFrame.setObjectName("searchConfigFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.searchConfigFrame)
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.searchConfigInput = QtWidgets.QLineEdit(self.searchConfigFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.searchConfigInput.sizePolicy().hasHeightForWidth())
        self.searchConfigInput.setSizePolicy(sizePolicy)
        self.searchConfigInput.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchConfigInput.setFont(font)
        self.searchConfigInput.setObjectName("searchConfigInput")
        self.horizontalLayout_8.addWidget(self.searchConfigInput)
        self.searchConfigBtn = QtWidgets.QPushButton(self.searchConfigFrame)
        self.searchConfigBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.searchConfigBtn.setMaximumSize(QtCore.QSize(40, 40))
        self.searchConfigBtn.setText("")
        self.searchConfigBtn.setObjectName("searchConfigBtn")
        self.horizontalLayout_8.addWidget(self.searchConfigBtn)
        self.verticalLayout_9.addWidget(self.searchConfigFrame)
        self.verticalLayout_7.addWidget(self.tab1_line2, 0, QtCore.Qt.AlignTop)
        self.tab1_line3 = QtWidgets.QWidget(self.tab1_top_frame)
        self.tab1_line3.setObjectName("tab1_line3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab1_line3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.searchAS1Label = QtWidgets.QLabel(self.tab1_line3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchAS1Label.setFont(font)
        self.searchAS1Label.setObjectName("searchAS1Label")
        self.verticalLayout_11.addWidget(self.searchAS1Label)
        self.searchAS1Frame = QtWidgets.QFrame(self.tab1_line3)
        self.searchAS1Frame.setMinimumSize(QtCore.QSize(0, 40))
        self.searchAS1Frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.searchAS1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchAS1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchAS1Frame.setLineWidth(0)
        self.searchAS1Frame.setObjectName("searchAS1Frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.searchAS1Frame)
        self.horizontalLayout_10.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.searchAS1Input = QtWidgets.QLineEdit(self.searchAS1Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.searchAS1Input.sizePolicy().hasHeightForWidth())
        self.searchAS1Input.setSizePolicy(sizePolicy)
        self.searchAS1Input.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.searchAS1Input.setFont(font)
        self.searchAS1Input.setObjectName("searchAS1Input")
        self.horizontalLayout_10.addWidget(self.searchAS1Input)
        self.searchAS1Btn = QtWidgets.QPushButton(self.searchAS1Frame)
        self.searchAS1Btn.setMinimumSize(QtCore.QSize(40, 40))
        self.searchAS1Btn.setMaximumSize(QtCore.QSize(40, 40))
        self.searchAS1Btn.setText("")
        self.searchAS1Btn.setObjectName("searchAS1Btn")
        self.horizontalLayout_10.addWidget(self.searchAS1Btn)
        self.verticalLayout_11.addWidget(self.searchAS1Frame)
        self.verticalLayout_7.addWidget(self.tab1_line3)
        self.verticalLayout_4.addWidget(self.tab1_top_frame, 0, QtCore.Qt.AlignTop)
        self.tab1_bottom_frame = QtWidgets.QFrame(self.tab1)
        self.tab1_bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab1_bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab1_bottom_frame.setObjectName("tab1_bottom_frame")
        self.verticalLayout_4.addWidget(self.tab1_bottom_frame, 0, QtCore.Qt.AlignBottom)
        self.tab2 = QtWidgets.QFrame(self.configFrame)
        self.tab2.setGeometry(QtCore.QRect(0, 0, 657, 600))
        self.tab2.setMinimumSize(QtCore.QSize(657, 600))
        self.tab2.setMaximumSize(QtCore.QSize(657, 600))
        self.tab2.setStyleSheet("")
        self.tab2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab2.setLineWidth(0)
        self.tab2.setObjectName("tab2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(0)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.tab2.raise_()
        self.tab1.raise_()
        self.verticalLayout_5.addWidget(self.configFrame)
        self.configBtns = QtWidgets.QFrame(self.configBody)
        self.configBtns.setMinimumSize(QtCore.QSize(0, 50))
        self.configBtns.setMaximumSize(QtCore.QSize(16777215, 50))
        self.configBtns.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.configBtns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configBtns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configBtns.setObjectName("configBtns")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.configBtns)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveBtn = QtWidgets.QPushButton(self.configBtns)
        self.saveBtn.setMinimumSize(QtCore.QSize(100, 40))
        self.saveBtn.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_4.addWidget(self.saveBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.configBtns)
        self.cancelBtn.setMinimumSize(QtCore.QSize(100, 40))
        self.cancelBtn.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_4.addWidget(self.cancelBtn)
        self.verticalLayout_5.addWidget(self.configBtns, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.configBody)
        self.verticalLayout.addWidget(self.body)
        self.configShadow = QtWidgets.QFrame(self.centralwidget)
        self.configShadow.setGeometry(QtCore.QRect(0, 0, 940, 740))
        self.configShadow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configShadow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configShadow.setObjectName("configShadow")
        self.configShadow.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Config"))
        self.tileTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Configuration</span></p></body></html>"))
        self.generalBtn.setText(_translate("MainWindow", "General"))
        self.profilesBtn.setText(_translate("MainWindow", "Profiles"))
        self.searchFileLabel.setText(_translate("MainWindow", "Toir Executable:"))
        self.searchFileInput.setPlaceholderText(_translate("MainWindow", "Click on the search icon and select the Toir executable..."))
        self.useCCBtn.setText(_translate("MainWindow", "Use Custom Config"))
        self.searchConfigLabel.setText(_translate("MainWindow", "Custom Config File:"))
        self.searchConfigInput.setPlaceholderText(_translate("MainWindow", "Click on the search icon and select the custom config file..."))
        self.searchAS1Label.setText(_translate("MainWindow", "Toir config path (Example: C:\\Program Files\\AS1...config):"))
        self.searchAS1Input.setPlaceholderText(_translate("MainWindow", "Click on the search icon and select the custom config file..."))
        self.label_2.setText(_translate("MainWindow", "Coming soon..."))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
