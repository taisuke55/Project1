from PyQt6.QtWidgets import *
from gui import *

class TelevisionLogic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 8
    MIN_CHANNEL = 1
    MAX_CHANNEL = 9

    def __init__(self):
        super().setupUi(self)

        self.__status == False
        self.__muted == False
        self.__volume = TelevisionLogic.MIN_VOLUME
        self.__channel = TelevisionLogic.MIN_CHANNEL

        self.button_power.clicked.connect(lambda:self.power())
        self.volume_slider.valueChanged.connect(lambda:self.slider())
        self.channel_1.clicked.connect(lambda:self.channel1())
        self.channel_2.clicked.connect(lambda:self.channel2())
        self.channel_3.clicked.connect(lambda:self.channel3())
        self.channel_4.clicked.connect(lambda:self.channel4())
        self.channel_5.clicked.connect(lambda:self.channel5())
        self.channel_6.clicked.connect(lambda:self.channel6())
        self.channel_7.clicked.connect(lambda:self.channel7())
        self.channel_8.clicked.connect(lambda:self.channel8())
        self.channel_9.clicked.connect(lambda:self.channel9())
        self.channelUp.clicked.connect(lambda:self.channel_up())
        self.channelDown.clicked.connect(lambda:self.channel_down())
        self.button_mute.clicked.connect(lambda:self.mute())
        self.volumeUp.clicked.connect(lambda:self.volume_up())
        self.volumeDown.clicked.connect(lambda: self.volume_down())

        def power(self) -> None:
            """
            Method to turn on or off a TV's power.
            """
            if self.__status:
                self.__status = False
            else:
                self.__status = True

        def slider(self) -> None:
            self.__volume = self.volume_slider.value()

        def channel1(self) -> None:
            self.__channel = 1

        def channel2(self) -> None:
            self.__channel = 2

        def channel3(self) -> None:
            self.__channel = 3

        def channel4(self) -> None:
            self.__channel = 4

        def channel5(self) -> None:
            self.__channel = 5

        def channel6(self) -> None:
            self.__channel = 6

        def channel7(self) -> None:
            self.__channel = 7

        def channel8(self) -> None:
            self.__channel = 8

        def channel9(self) -> None:
            self.__channel = 9

        def channel_up(self):
            """
            Method to change a channel up.
            """
            if self.__status:
                if self.__channel < TelevisionLogic.MAX_CHANNEL:
                    self.__channel += 1
                else:
                    self.__channel = TelevisionLogic.MIN_CHANNEL

        def channel_down(self) -> None:
            """
            Method to change a channel down.
            """
            if self.__status:
                if self.__channel > TelevisionLogic.MIN_CHANNEL:
                    self.__channel -= 1
                else:
                    self.__channel = TelevisionLogic.MAX_CHANNEL

        def mute(self) -> None:
            """
            Method to mute a TV's sound.
            """
            if self.__status:
                if self.__muted:
                    self.__muted = False
                else:
                    self.__muted = True

        def volume_up(self) -> None:
            """
            Method to change volume up.
            """
            if self.__status:
                self.__muted = False
                if self.__volume < TelevisionLogic.MAX_VOLUME:
                    self.__volume += 1

        def volume_down(self) -> None:
            """
            Method to change volume down.
            """
            if self.__status:
                self.__muted = False
                if self.__volume > TelevisionLogic.MIN_VOLUME:
                    self.__volume -= 1