import sys
import pyttsx3
import datetime
import threading
from pygame import mixer
from PyQt5.QtGui import QMovie
import speech_recognition as sr
from asset.responser import Responser
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

mixer.init()
engine = pyttsx3.init()
lastQuery = "Start"
isDeltaStarted = False
screen = "[BANNER]"

responseEngine = Responser()

def greeting_function():

    greeting = ""

    currentHour = int(datetime.datetime.now().hour)
    if currentHour >= 0 and currentHour < 12:
        greeting = 'Good Morning!'

    if currentHour >= 12 and currentHour < 18:
        greeting = 'Good Afternoon!'

    if currentHour >= 18 and currentHour !=0:
        greeting = 'Good Evening!'

    return greeting

def speech_text(self, text):
    global lastQuery
    self.update_signal.emit(f"voice_screen")
    print('Computer: {}'.format(text))
    engine.say(text)
    engine.runAndWait()
    self.update_signal.emit(f"standby_screen")
   
def processor(self, query):
    speech_text(self,Responser.respond(query))


class SpeechRecognitionThread(QThread):

    update_signal = pyqtSignal(str)

    def run(self):
        global lastQuery
        while True:
            r = sr.Recognizer()
            query = ""

            with sr.Microphone() as source:
                if lastQuery != "":
                    mixer.music.load('media/audio/recognizer-sound.mp3')
                    mixer.music.play()
                    lastQuery = ""
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print('User: ' + query + '\n')
                lastQuery = query
                
                processor(self, query) # Send the qurry to processor
                

            except sr.UnknownValueError:
                pass


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.setWindowTitle("Delta Assistant")
        self.setFixedSize(800, 600)  # Set a fixed size to disable resizing

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # First Standby Screen GIF
        self.banner_label = QLabel(self)
        self.banner_movie = QMovie("media/images/banner-screen.gif")
        self.banner_label.setMovie(self.banner_movie)
        layout.addWidget(self.banner_label)

        # Second Standby Screen GIF
        self.standby_label = QLabel(self)
        self.standby_movie = QMovie("media/images/standby-screen.gif")
        self.standby_label.setMovie(self.standby_movie)
        self.standby_label.setVisible(False)
        layout.addWidget(self.standby_label)

        # Second Standby Screen GIF
        self.voice_label = QLabel(self)
        self.voice_movie = QMovie("media/images/voice-screen.gif")
        self.voice_label.setMovie(self.voice_movie)
        self.voice_label.setVisible(False)
        layout.addWidget(self.voice_label)

        # Start the first standby GIF explicitly
        self.banner_movie.start()

        # Use a QTimer to switch to the second standby GIF after 4 seconds
        timer = QTimer(self)
        timer.timeout.connect(self.show_second_standby_gif)
        timer.start(5000)

        # Center the window on the screen
        self.center_on_screen()


    def deltaIntro(self):
        mixer.music.load('media/audio/recognizer-sound.mp3')
        mixer.music.play()
        engine.say("Hello {} I am Delta, your virtual assistant. How may I help you!".format(greeting_function()))
        engine.runAndWait()

    def start_delta(self):
        self.deltaIntro()
        self.speech_recognition_thread = SpeechRecognitionThread()
        self.speech_recognition_thread.update_signal.connect(self.update_label)  # Connect the signal to the slot
        self.speech_recognition_thread.start()

    def show_banner_screen(self):
        self.banner_label.setVisible(True)
        self.voice_label.setVisible(False)
        self.standby_label.setVisible(False)
        self.banner_movie.start()

    def show_voice_screen(self):
        self.banner_label.setVisible(False)
        self.voice_label.setVisible(True)
        self.standby_label.setVisible(False)
        self.voice_movie.start()

    def show_standby_screen(self):
        self.banner_label.setVisible(False)
        self.voice_label.setVisible(False)
        self.standby_label.setVisible(True)
        self.standby_movie.start()

    def show_second_standby_gif(self):
        global isDeltaStarted, screen

        if screen == "[BANNER]":
            self.show_banner_screen()

        elif screen == "[VOICE]":
            self.show_voice_screen()

        elif screen == "[STANDBY]":
            self.show_standby_screen()
        
        if isDeltaStarted == False:
            self.start_delta()

            # Show Standby after staring
            screen = "[STANDBY]"
            self.show_standby_screen()

            isDeltaStarted = True

    def update_label(self, message):

        global screen;

        if message == "voice_screen":
            screen = "[VOICE]"
            self.show_voice_screen()

        elif message == "standby_screen":
            screen = "[STANDBY]"
            self.show_standby_screen()

    def center_on_screen(self):
        frame_geometry = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MyMainWindow()
    mainWin.show()
    sys.exit(app.exec_())
