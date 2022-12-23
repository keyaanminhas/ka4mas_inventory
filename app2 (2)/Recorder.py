import sounddevice as sd
import soundfile as sf
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys
import queue
import argparse
import tempfile
import os
import re
from pathlib import Path
from threading import Thread
from Dialer import Dialer
from sql import SqlHelper

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        uic.loadUi(os.path.join(Path(__file__).resolve().parent, "Recorder.ui"), self)
        self.dialer = Dialer()
        self.numbers2call = []
        self.pushButtonStopRecord.setEnabled(False)
        self.pushButtonStopCall.setEnabled(False)
        self.pushButtonStartRecord.clicked.connect(self.runRec)
        self.pushButtonStopRecord.clicked.connect(self.stopRec)
        self.pushButtonStartCall.clicked.connect(self.startCalls)
        self.pushButtonStopCall.clicked.connect(self.stopCalls)
        self.add_phone_btn.clicked.connect(self.addPhoneNumber)
        self.recording = False
        self.load_settings()
        
    def load_settings(self):
        helper = SqlHelper('dialer.db')
        
        data = helper.select("select * from dialerSettings")
        # self.lineEditTwilioNumber.setText(data[0][0]) 
        # self.lineEditSid.setText(data[0][1])
        # self.lineEditToken.setText(data[0][2])
        

    def startCalls(self):
        self.pushButtonStopCall.setEnabled(True)
        self.pushButtonStartCall.setEnabled(False)
        tw_num = self.lineEditTwilioNumber.text()
        tw_sid = self.lineEditSid.text()
        tw_atoken = self.lineEditToken.text()
        self.dialer.initDial(tw_num, tw_sid, tw_atoken)
        self.dialer.connect()
        t = Thread(target = lambda :self.dialer.dialNumbers(self.numbers2call))
        t.start()

    def stopCalls(self) :
        self.pushButtonStopCall.setEnabled(False)
        self.pushButtonStartCall.setEnabled(True)
        self.dialer.can_call = False

    def addPhoneNumber(self) :
        phone_number = self.add_num_input.text()
        patrn = re.compile("(\+?\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")

        if patrn.match(phone_number) is None :
            QMessageBox.about(self, "Error", " Invalid phone number")
            return

        self.numbers2call.append(phone_number)
        self.fillNumsTable()
        self.add_num_input.clear()

    def deletePhoneNumber(self, i):
        del self.numbers2call[i]
        self.fillNumsTable()

    def fillNumsTable(self) :
        print(self.numbers2call)
        self.tableWidgetPhoneNumbers.setRowCount(len(self.numbers2call))
        for i, row in enumerate(self.numbers2call) :  
            editline=QtWidgets.QTableWidgetItem(str(row))
            self.tableWidgetPhoneNumbers.setItem(i, 0, editline)

            del_btn = QtWidgets.QPushButton(self.tableWidgetPhoneNumbers)
            del_btn.setText("Delete")
            del_btn.clicked.connect(lambda _, index=i: self.deletePhoneNumber(index))
            self.tableWidgetPhoneNumbers.setCellWidget(i, 1, del_btn)

    def runRec(self) :
        t = Thread(target=self.startRec)
        t.start()

    def startRec(self):
        self.recording = True
        self.pushButtonStartRecord.setEnabled(False)
        self.pushButtonStopRecord.setEnabled(True)
        def int_or_str(text):
            """Helper function for argument parsing."""
            try:
                return int(text)
            except ValueError:
                return text
        
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument(
            '-l', '--list-devices', action='store_true',
            help='show list of audio devices and exit')
        parser.add_argument(
            '-d', '--device', type=int_or_str,
            help='input device (numeric ID or substring)')
        parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        parser.add_argument(
            '-c', '--channels', type=int, default=1, help='number of input channels')
        parser.add_argument(
            'filename', nargs='?', metavar='FILENAME',
            help='audio file to store recording to')
        parser.add_argument(
            '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
        args = parser.parse_args()
        
        try:
       
            if args.list_devices:
                print(sd.query_devices())
                parser.exit(0)
            if args.samplerate is None:
                device_info = sd.query_devices(args.device, 'input')
                # soundfile expects an int, sounddevice provides a float:
                args.samplerate = int(device_info['default_samplerate'])
            if args.filename is None:
                args.filename = tempfile.mktemp(prefix='rec_unlimited_',
                                                suffix='.wav', dir='')
            q = queue.Queue()
        
            def callback(indata, frames, time, status):
                """This is called (from a separate thread) for each audio block."""
                if status:
                    print(status, file=sys.stderr)
                q.put(indata.copy())
        
            # Make sure the file is opened before recording anything:
            filename = os.path.join(Path(__file__).resolve().parent, args.filename)
            with sf.SoundFile(filename, mode='x', samplerate=args.samplerate,
                              channels=args.channels, subtype=args.subtype) as file:
                with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                    channels=args.channels, callback=callback):
                    print('#' * 80)
                    print('press Ctrl+C to stop the recording')
                    print('#' * 80)
                    while self.recording:
                        file.write(q.get())
                    
        
        except KeyboardInterrupt:
            print('\nRecording finished: ' + repr(args.filename))
            parser.exit(0)
        except Exception as e:
            parser.exit(type(e).__name__ + ': ' + str(e))
                            
            
    def stopRec(self):
        self.pushButtonStartRecord.setEnabled(True)
        self.pushButtonStopRecord.setEnabled(False)
        self.recording = False


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())    