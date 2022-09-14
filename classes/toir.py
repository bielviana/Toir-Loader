from threading import Thread
import subprocess as sp
import json
from os import path
import os
from time import sleep

class Toir():
    def __init__(self):
        pass

    def load(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
        self.toirExePath = config['general'][0]['toirExe']
        self.toirConfigFile = config['general'][0]['configFile']
        self.toirConfigPath = config['general'][0]['configPath']

        thToir = ThToir(1, self.toirExePath)
        thToir.start()

        sleep(1.5)
        
        for dirpath, subfolders, files in os.walk(self.toirConfigPath):
            for file in files:
                if len(file) > 7 and '.ini' in file:
                    self.toirConfigFileName = file
                    sp.Popen(f'del "{path.join(self.toirConfigPath, file)}"', shell=True, stdout=sp.PIPE).stdout.read()
        sp.Popen(f'copy "{self.toirConfigFile}" "{path.join(self.toirConfigPath, self.toirConfigFileName)}"', shell=True, stdout=sp.PIPE).stdout.read()
class ThToir(Thread):
    def __init__(self, num, toirPath):
        Thread.__init__(self)
        self.num = num
        self.toirPath = toirPath
    
    def run(self):
        sp.Popen(self.toirPath, shell=True, stdout=sp.PIPE).stdout.read()