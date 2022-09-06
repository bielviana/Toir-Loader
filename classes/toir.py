from threading import Thread
import subprocess as sp

class Toir():
    def __init__(self):
        pass

    def load(self):
        toirPath = 'C:\TOIR_INFINITY_12.16.1.1\TOIR_INFINITY.exe'
        thread = Th(1, toirPath)
        thread.start()

class Th(Thread):
    def __init__(self, num, toirPath):
        Thread.__init__(self)
        self.num = num
        self.toirPath = toirPath
    
    def run(self):
        sp.Popen(self.toirPath, shell=True, stdout=sp.PIPE).stdout.read()