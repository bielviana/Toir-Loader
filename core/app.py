from PySide2 import *
from core.ui_interface import *
from core.ui_config import *
from Custom_Widgets.Widgets import *
from classes.socialLinks import *
from classes.toir import *
from classes.config import *
from os import path as p
import json

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

        self.configWindow = ConfigWindow()

        if p.isfile('config.json') == False:
            with open ('config.json', 'w') as file:
                config = {}
                config['general'] = [1]
                config['general'][0] = {"toirExe": "", "useCustomConfig": False, "configFile": "", "configPath": ""}
                config['profiles'] = []
                json.dump(config, file, indent=4)
            self.configWindow.show()

        # EVENT TO OPEN THE CONFIG WINDOW
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

    def CloseToir(self):
        with open('config.json', 'r') as file:
            config2 = json.load(file)
        loader_exe_path = config2['general'][0]['toirExe'].split('\\')
        
        for file in loader_exe_path:
            if '.EXE' in file or '.exe' in file:
                sp.Popen(f'TASKKILL /IM {file} /F /T', shell=True, stdout=sp.PIPE).stdout.read()

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

        if config['general'][0]['useCustomConfig'] == None:
            with open('config.json', 'w') as file:
                config['general'][0]['useCustomConfig'] = False
                json.dump(config, file, indent=4)

        if config['general'][0]['configFile'] == None:
            with open('config.json', 'w') as file:
                config['general'][0]['configFile'] = ""
                json.dump(config, file, indent=4)

        if config['general'][0]['configPath'] == None:
            with open('config.json', 'w') as file:
                config['general'][0]['configPath'] = ""
                json.dump(config, file, indent=4)
        
        self.ui.searchFileInput.setText(config['general'][0]['toirExe'])
        self.toirExe = self.ui.searchFileInput.text()
        self.configFile = self.ui.searchConfigInput.text()
        self.configPath = self.ui.searchAS1Input.text()
        self.useCustomConfig = config['general'][0]['useCustomConfig']

        if config['general'][0]['useCustomConfig'] == True:
            self.ui.useCCBtn.setText("Don't Use Custom Config")
            self.ui.tab1_line2.setHidden(False)
            self.ui.tab1_line3.setHidden(False)
            self.ui.searchConfigInput.setText(config['general'][0]['configFile'])
            self.ui.searchAS1Input.setText(config['general'][0]['configPath'])
        elif config['general'][0]['useCustomConfig'] == False:
            self.ui.useCCBtn.setText("Use Custom Config")
            self.ui.tab1_line2.setHidden(True)
            self.ui.tab1_line3.setHidden(True)
            self.ui.searchConfigInput.setText('')
            self.ui.searchAS1Input.setText('')

        # ALTERNATE INTO THE CONFIG TABS
        self.ui.tab2.setHidden(True)

        self.ui.generalBtn.clicked.connect(lambda: self.ui.tab2.setHidden(True))
        self.ui.generalBtn.clicked.connect(lambda: self.ui.tab1.setHidden(False))

        self.ui.profilesBtn.clicked.connect(lambda: self.ui.tab1.setHidden(True))
        self.ui.profilesBtn.clicked.connect(lambda: self.ui.tab2.setHidden(False))

        # GENERAL CONFIGS
        self.generalConfig = GeneralConfig()
        self.ui.searchFileBtn.clicked.connect(lambda: self.updateGeneralConfig('toirExe'))
        self.ui.useCCBtn.clicked.connect(lambda: self.updateGeneralConfig('useCustomConfig'))
        self.ui.searchConfigBtn.clicked.connect(lambda: self.updateGeneralConfig('configFile'))
        self.ui.searchAS1Btn.clicked.connect(lambda: self.updateGeneralConfig('configPath'))

        # SAVE OR CANCEL THE CONFIG CHANGES
        self.ui.saveBtn.clicked.connect(self.saveConfig)
        self.ui.cancelBtn.clicked.connect(self.close)

    def updateGeneralConfig(self, type):
        if type == 'toirExe':
            self.ui.searchFileInput.setText(self.generalConfig.searchFile(type))
            self.toirExe = self.ui.searchFileInput.text()
        elif type == 'configFile':
            self.ui.searchConfigInput.setText(self.generalConfig.searchFile(type))
            self.configFile = self.ui.searchConfigInput.text()
        elif type == 'configPath':
            self.ui.searchAS1Input.setText(self.generalConfig.searchFolder(type))
            self.configPath = self.ui.searchAS1Input.text()
        elif type == 'useCustomConfig':
            with open('config.json', 'r') as file:
                config = json.load(file)

            if self.useCustomConfig == True:
                self.ui.useCCBtn.setText("Use Custom Config")
                self.ui.tab1_line2.setHidden(True)
                self.ui.tab1_line3.setHidden(True)
                self.ui.searchConfigInput.setText('')
                self.ui.searchAS1Input.setText('')
                self.useCustomConfig = False
            elif self.useCustomConfig == False:
                self.ui.useCCBtn.setText("Don't Use Custom Config")
                self.ui.tab1_line2.setHidden(False)
                self.ui.tab1_line3.setHidden(False)
                self.ui.searchConfigInput.setText(config['general'][0]['configFile'])
                self.ui.searchAS1Input.setText(config['general'][0]['configPath'])
                self.useCustomConfig = True
    
    def saveConfig(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
        
        if self.toirExe != '' and self.toirExe != None:
            if ".exe" in self.toirExe:
                toirExeError = False
                config['general'][0]['toirExe'] = self.toirExe
            else:
                toirExeError = True
                self.ui.searchFileInput.setText('')
        else:
            toirExeError = False
        
        if self.configFile != '' and self.configFile != None:
            if '.ini' in self.configFile:
                configFileError = False
                config['general'][0]['configFile'] = self.configFile
            else:
                configFileError = True
                self.ui.searchConfigInput.setText('')
        else:
            configFileError = False
        
        if self.configPath != '' and self.configPath != None:
            if p.isfile(self.configPath+'\\info.dat'):
                configPathError = False
                config['general'][0]['configPath'] = self.configPath
            else:
                configPathError = True
                self.ui.searchAS1Input.setText('')
        else:
            configPathError = False
        
        if self.useCustomConfig == False:
            configFileError = False
            configPathError = False

        if configFileError == False and configPathError == False:
            config['general'][0]['useCustomConfig'] = self.useCustomConfig

        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)
        
        if toirExeError == True or configFileError == True or configPathError == True:
            if toirExeError == True:
                self.ui.searchFileInput.setPlaceholderText('Select an EXE file!!!!!')
            if configFileError == True:
                self.ui.searchConfigInput.setPlaceholderText('Select a Toir configuration INI file!!!!!')
            if configPathError == True:
                self.ui.searchAS1Input.setPlaceholderText('Select the correct toir config folder!!!!!')
        else:
            self.close()
            
