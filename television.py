class Television:
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3

    def __init__(self):
        self.__status=False
        self.__muted=False
        self.__volume=Television.MIN_VOLUME
        self.__channel=Television.MIN_CHANNEL
        self.__call_count=0


    def power(self):
        """
        Method to on and off the TV
        """
        self.__status=True
        self.__call_count+=1
        if self.__call_count%2==0:
            self.__status=False

    def mute(self):
        """
        Method to mute and unmute TV
        """
        self.__muted=True
        

    def channel_up(self):
        """
        Method to increase the TV channel value when the TV is on
        """
        if self.__status:
            if self.__channel<Television.MAX_CHANNEL:
                self.__channel+=1
            else:
                self.__channel=Television.MIN_CHANNEL
        

    def channel_down(self):
        """
        Method to decrease the TV channel value when the TV is on
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel-=1
            else:
                self.__channel=Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increase the TV volume when the TV is on
        """
        if self.__status:
            self.__muted=False
            if self.__volume<Television.MAX_VOLUME:
                self.__volume+=1
            else:
                self.__volume=Television.MAX_VOLUME
                

    def volume_down(self):
        """
        Method to decrease the TV volume when the TV is on
        """
        if self.__status:
            self.__muted=False
            if self.__volume>Television.MIN_VOLUME:
                self.__volume-=1
            else:
                self.__volume=Television.MIN_VOLUME

    def __str__(self):
    """
    Method to show the values of Power,Channel,Volume once called
    """
        if self.__muted is True and self.__status is True :
            return f" Power={self.__status},Channel={self.__channel},Volume={Television.MIN_VOLUME}"
        else:
            return f" Power={self.__status},Channel={self.__channel},Volume={self.__volume}"
                
            
        
        
