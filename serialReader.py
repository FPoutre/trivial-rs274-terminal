from threading import Thread

class SerialReader(Thread):
    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial
    
    def run(self):
        while self.serial.is_open:
            print(self.serial.readLine())