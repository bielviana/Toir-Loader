from genericpath import isfile
from PySide2 import *
from core.ui_interface import *
from core.ui_config import *
from Custom_Widgets.Widgets import *
from classes.socialLinks import *
from classes.toir import *
from classes.config import *
from os import path as p
import json
import easygui

class MainWindow(QMainWindow):
    def __init__(self):
        # CONFIG MAIN WINDOW
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={
            'resources/ui_interface.json'
        })
        self.show()

        if p.isfile('config.json') == False:
            with open ('config.json', 'w') as file:
                config = {}
                config['general'] = [1]
                config['general'][0] = {"toirExe": "", "configFile": ""}
                config['profiles'] = []
                json.dump(config, file, indent=4)
            self.configWindow = ConfigWindow()
            self.configWindow.show()

        # EVENT TO OPEN THE CONFIG WINDOW
        try:
            self.ui.configBtn.clicked.connect(self.configWindow.show)
        except:
            self.configWindow = ConfigWindow()
            self.ui.configBtn.clicked.connect(self.configWindow.show)
                
        # EVENT TO LOAD THE TOIR INFINITY/ALPHA
        self.toir = Toir()
        self.ui.loadBtn.clicked.connect(self.toir.load)

        # EVENTS TO OPEN THE SOCIAL LINKS
        self.socialLinks = SocialLinks()
        self.ui.discBtn.clicked.connect(lambda: self.socialLinks.openLink('discord'))
        self.ui.ttBtn.clicked.connect(lambda: self.socialLinks.openLink('twitter'))
        self.ui.gitBtn.clicked.connect(lambda: self.socialLinks.openLink('github'))
        self.ui.ppBtn.clicked.connect(lambda: self.socialLinks.openLink('paypal'))

class ConfigWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ConfigWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={
            'resources/ui_config.json'
        })

        # LOAD CONFIGS
        with open('config.json', 'r') as file:
            config = json.load(file)

        if config['general'][0]['toirExe'] == None:
            with open('config.json', 'w') as file:
                config['general'][0]['toirExe'] = ""
                json.dump(config, file, indent=4)

        if config['general'][0]['configFile'] == None:
            with open('config.json', 'w') as file:
                config['general'][0]['configFile'] = ""
                json.dump(config, file, indent=4)

        self.ui.searchFileInput.setText(config['general'][0]['toirExe'])
        self.ui.searchConfigInput.setText(config['general'][0]['configFile'])

        self.toirExe = self.ui.searchFileInput.text()
        self.configFile = self.ui.searchConfigInput.text()

        # ALTERNATE INTO THE CONFIG TABS
        self.ui.tab2.setHidden(True)

        self.ui.generalBtn.clicked.connect(lambda: self.ui.tab2.setHidden(True))
        self.ui.generalBtn.clicked.connect(lambda: self.ui.tab1.setHidden(False))

        self.ui.profilesBtn.clicked.connect(lambda: self.ui.tab1.setHidden(True))
        self.ui.profilesBtn.clicked.connect(lambda: self.ui.tab2.setHidden(False))

        # GENERAL CONFIGS
        self.generalConfig = GeneralConfig()
        self.ui.searchFileBtn.clicked.connect(lambda: self.updateGeneralConfig('toirExe'))
        self.ui.searchConfigBtn.clicked.connect(lambda: self.updateGeneralConfig('configFile'))

        # SAVE OR CANCEL THE CONFIG CHANGES
        self.ui.saveBtn.clicked.connect(self.saveConfig)
        self.ui.cancelBtn.clicked.connect(self.close)

    def updateGeneralConfig(self, type):
        self.filePath = self.generalConfig.searchFile(type)

        if type == 'toirExe':
            self.ui.searchFileInput.setText(self.filePath)
            self.toirExe = self.ui.searchFileInput.text()
        if type == 'configFile':
            self.ui.searchConfigInput.setText(self.filePath)
            self.configFile = self.ui.searchConfigInput.text()
    
    def saveConfig(self):
        toirExeError = True
        configFileError = True
        with open('config.json', 'r') as file:
            config = json.load(file)
        
        if self.toirExe != '' and self.toirExe != None:
            if ".exe" in self.toirExe:
                config['general'][0]['toirExe'] = self.toirExe
                toirExeError = False
            else:
                toirExeError = True
                self.ui.searchFileInput.setText("")
        if self.configFile != '' and self.configFile != None:
            if '.ini' in self.configFile:
                config['general'][0]['configFile'] = self.configFile
                configFileError = False
            else:
                configFileError = True
                self.ui.searchConfigInput.setText("")
        
        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)
        
        # if toirExeError == True:
        #     toirExeError_msg = '• Toir executable: Select an EXE file\n'
        # else:
        #     toirExeError_msg = ''
        # if configFileError == True:
        #     configFileError_msg = '• Custom config file: Select a Toir configuration INI file\n'
        # else:
        #     configFileError_msg = ''
        
        if toirExeError == True or configFileError == True:
            # error_msg = f'{toirExeError_msg}{configFileError_msg}'
            # easygui.codebox(title='Error!', msg='Some settings have not been changed.', text=error_msg)
            if toirExeError == True:
                self.ui.searchFileInput.setPlaceholderText('Select an EXE file!!!!!')
            if configFileError == True:
                self.ui.searchConfigInput.setPlaceholderText('Select a Toir configuration INI file!!!!!')
        else:
            self.ui.saveBtn.clicked.connect(self.close)
