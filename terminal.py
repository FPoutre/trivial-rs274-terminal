import argparse
import serial
import sys
import signal

from serialReader import SerialReader
from serialWriter import SerialWriter


def cleanup(sig, frame):
    global ser, serialReader, serialWriter
    print("Closing Serial Connection...")
    ser.close()
    print("Done.")
    print("Waiting for all threads to stop...")
    serialReader.join()
    serialWriter.join()
    print("Done. Goodbye !")
    sys.exit(0)

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
    ser.open()
    serialReader.start()
    serialWriter.start()

    signal.signal(signal.SIGINT, cleanup)
    signal.pause()

