from Device import *

class Room:
    def __init__(self, name):
        self.__name = name
        self.__devices = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def devices(self):
        return tuple(self.__devices)
    
    def get_devices_of_type(self, device_type):
        return tuple(dev for dev in self.__devices if isinstance(dev, device_type))
    
    def lights_on(self):
        lights = self.get_devices_of_type(Lightbulb)
        for light in lights:
            pass # Set light device state to on
    
    def lights_off(self):
        lights = self.get_devices_of_type(Lightbulb)
        for light in lights:
            pass # Set light device state to off
    
    def play_music(self):
        speakers = self.get_devices_of_type(Speaker)
        for speaker in speakers:
            pass # Set speaker device state to on with a specific song
    
    def stop_music(self):
        speakers = self.get_devices_of_type(Speaker)
        for speaker in speakers:
            pass # Set speaker device state to off
    
    def set_temperature(self, temperature):
        pass
    
    def set_schedule(self, device, start_time, end_time):
        pass
    
    def add_device(self, device):
        self.__devices.append(device)
    
    def get_power_usage(self):
        return sum(dev.get_power_usage() for dev in self.__devices)