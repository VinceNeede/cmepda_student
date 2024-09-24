class Television:
    def __init__(self):
        self._channel = 1
        self._volume = 30            ### from 0 to 100
        self._state = "off"

    @property
    def channel(self):
        return self._channel
    
    @property
    def volume(self):
        return self._volume
    
    @property
    def state(self):
        return self._state
    
    @property
    def is_on(self):
        return self._state == "on"

    def turn_on(self, channel=None, volume=None):
        if self.is_on:
            print("The TV is already on.")
            return
        if channel is not None:
            self._channel = channel
        if volume is not None:
            self._volume = volume
        self._state = "on"
        
    def turn_off(self):
        if not self.is_on:
            print("The TV is already off.")
            return
        self._state = "off"
        
    def change_channel(self, channel):
        if not self.is_on:
            print("The TV is off. Please turn it on.")
            return
        self._channel = channel

    def increase_volume(self, value=1):
        if not self.is_on:
            print("The TV is off. Please turn it on.")
            return
        self._volume += value

    def decrease_volume(self, value=1):
        if not self.is_on:
            print("The TV is off. Please turn it on.")
            return
        self._volume -= value

    def __str__(self):
        if not self.is_on:
            return "The TV is off."
        return f"Channel: {self._channel}, Volume: {self._volume}"
    
if __name__ == "__main__":
    my_tv = Television()
    print(my_tv)
    my_tv.turn_on(5, 20)
    print(my_tv)
    my_tv.change_channel(10)
    my_tv.increase_volume(2)
    print(my_tv)
    my_tv.decrease_volume()
    print(my_tv)