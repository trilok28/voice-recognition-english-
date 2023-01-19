from PyQt5 import QtGui
import sys
import datetime
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtWidgets import *

from ronny import Main
import speak
import testProgram
from speak import Spk
from ui import Ui_MainWindow


def wishme():
    ...
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Spk.say("good morning sir...\n")
    elif hour>=12 and hour<18:
        Spk.say("good afternoon sir...\n")
    else:
        Spk.say("good evening sir...\n")
    ...

    Spk.say("I am ronny, please tell me how may I help you....\n")

class MainThread(QThread):
    def __init__(self):                #known to self
        super(MainThread,self).__init__()
    def run(self, tdata=None):
         Main()

startExe = MainThread()

class Gui_start(QMainWindow):
    def setTextGUI(self,text):
        self.gui.info = text

    def __init__(self):

        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.start.clicked.connect(self.startTask)   # moving gui by clickig start button (basically calling function by clicking button
        self.gui.quite.clicked.connect(self.close)      #stop moving gui by clicking quite button



    def startTask(self):

        # start moving guissss
        self.gui.label1 = QtGui.QMovie("..//guiobject//recognize.gif")
        self.gui.label_recog.setMovie(self.gui.label1)
        self.gui.label1.start()


        self.gui.label2 = QtGui.QMovie("..//guiobject//Earth.gif")
        self.gui.label_earth.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("..//guiobject//initiate.gif")
        self.gui.lable_init.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("..//guiobject//textGif.gif")
        self.gui.label_textRecog.setMovie(self.gui.label4)
        self.gui.label4.start()



        #return self.gui
        # showing query
        startExe.start()


        # showing time , date, temprature in time text area
        timer = QTimer(self)
        timer.timeout.connect(self.showTimeDateLive)  # calling function showTimeDateLive
        timer.start(999)

        #return self.gui

    def showTimeDateLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()

        d_ate = QDate.currentDate()
        date = d_ate.toString()


        label_time = "Time : " + time
        label_date = "Date : " + date



        mainMsgData = speak.tdata
        self.gui.info = mainMsgData             #speak.file1.readlines()
        self.gui.MainMsg_tb.setText(self.gui.info)
        self.gui.tb1.setText(label_time)
        self.gui.tb2.setText(label_date)
        self.gui.tb3.setText(testProgram.temprature2)

        #info = "listening......."
       # self.gui.info = Spk.tdata
       # self.gui.MainMsg_tb.setText(self.gui.infos)



GuiApp = QApplication(sys.argv)
ronny_gui = Gui_start()
ronny_gui.show()
exit(GuiApp.exec_())

#Spk.say()
#print(speak.tdata)

