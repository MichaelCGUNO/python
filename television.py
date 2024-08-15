class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''Initialize the TV with power off, muted state, minimum volume, and minimum channel.'''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''Method to toggle the power status of the TV.'''
        self.__status = not self.__status

    def mute(self):
        '''Method to toggle the mute status of the TV.'''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''Method to increase the TV channel'''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''Method to decrease the TV channel'''
        if self.__status:
            if self.__channel > Television.MIN_VOLUME:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''Method to increase the TV volume'''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''Method to decrease the TV volume'''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''Method to show the TV status.
        :return tv status
        '''
        if self.__status:
            if self.__muted:
                volume = Television.MIN_VOLUME
            else:
                volume = self.__volume

            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
