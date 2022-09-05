import sys
import webbrowser as link
from PySide2 import *
from core.ui_interface import *
from Custom_Widgets.Widgets import *
from classes.socialLinks import *
from classes.toir import *

class MainWindow(QMainWindow):
    def __init__(self):
        # CONFIG MAIN WINDOW
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        # EVENT TO LOAD THE TOIR INFINITY/ALPHA
        self.toir = Toir()
        self.ui.loadBtn.clicked.connect(self.toir.load)

        # EVENTS TO OPEN THE SOCIAL LINKS
        self.socialLinks = SocialLinks()
        self.ui.discBtn.clicked.connect(lambda: self.socialLinks.openLink("discord"))
        self.ui.ttBtn.clicked.connect(lambda: self.socialLinks.openLink("twitter"))
        self.ui.gitBtn.clicked.connect(lambda: self.socialLinks.openLink("github"))
        self.ui.ppBtn.clicked.connect(lambda: self.socialLinks.openLink("paypal"))
