from threading import Thread

class SerialWriter(Thread):
    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial
    
    def run(self):
        while self.serial.is_open:
            command = input('>')
            self.serial.write(command.encode())