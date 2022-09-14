import easygui

class GeneralConfig():
    def __init__(self):
        pass

    def searchFile(self, type):
        if type == 'toirExe':
            self.type = "*.exe"
            self.titleType = 'the Toir executable'
        elif type == 'configFile':
            self.type = '*.ini'
            self.titleType = 'your custom config file'

        filePath = easygui.fileopenbox(title=f'Select {self.titleType}', default=self.type)

        if filePath == None:
            filePath = ''

        return filePath

    def searchFolder(self, type):
        if type == 'configPath':
            self.type = 'configPath'
            self.titleType = 'the Toir config folder'
        
        filePath = easygui.diropenbox(title=f'Select {self.titleType}') + '\\'

        if filePath == None:
            filePath = ''
        
        return filePath
