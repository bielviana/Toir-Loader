from threading import Thread
import subprocess as sp
import json
from os import path

class Toir():
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
        self.toirExePath = config['general'][0]['toirExe']

    def load(self):
        thread = Th(1, self.toirExePath)
        thread.start()

class Th(Thread):
    def __init__(self, num, toirPath):
        Thread.__init__(self)
        self.num = num
        self.toirPath = toirPath
    
    def run(self):
        sp.Popen(self.toirPath, shell=True, stdout=sp.PIPE).stdout.read()