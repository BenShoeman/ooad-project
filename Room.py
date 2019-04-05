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
            light.change_state(on=True)
    
    def lights_off(self):
        lights = self.get_devices_of_type(Lightbulb)
        for light in lights:
            light.change_state(on=False)
    
    def play_music(self, song):
        speakers = self.get_devices_of_type(Speaker)
        for speaker in speakers:
            speaker.change_state(on=True, song=song)
    
    def stop_music(self):
        speakers = self.get_devices_of_type(Speaker)
        for speaker in speakers:
            speaker.change_state(on=False)
    
    def set_temperature(self, temperature):
        thermostats = self.get_devices_of_type(Thermostat)
        for thermostat in thermostats:
            thermostat.change_state(temperature=temperature)
    
    def set_schedule(self, device, start_time, end_time):
        pass
    
    def add_device(self, device):
        self.__devices.append(device)
    
    def get_power_usage(self):
        return sum(dev.wattage for dev in self.__devices)