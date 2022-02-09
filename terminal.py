import argparse
import serial
import sys
from threading import Thread


class SerialReader(Thread):

    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial
        self.stop = False
    
    def kill(self):
        self.stop = True
    
    def run(self):
        while not self.stop:
            try:
                print(self.serial.readline().decode())
            except KeyboardInterrupt:
                break

class SerialWriter(Thread):
    def __init__(self, serial):
        Thread.__init__(self)
        self.serial = serial
        self.stop = False
    
    def kill(self):
        self.stop = True
    
    def run(self):
        while not self.stop:
            try: 
                command = input('>')
                command += '\n'
                self.serial.write(command.encode())
            except KeyboardInterrupt:
                break

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--dev',
        default='/dev/ttyUSB0',
        help='/dev file to access')
    parser.add_argument(
        '-b',
        '--baudrate',
        default='115200',
        help='baudrate')
    args = parser.parse_args()

    ser = serial.Serial(args.dev, args.baudrate)
    serialReader = SerialReader(ser)
    serialWriter = SerialWriter(ser)
    serialReader.start()
    serialWriter.start()

    serialReader.join()
    serialWriter.join()
    sys.exit(0)