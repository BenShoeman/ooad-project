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
    
    def set_schedule(self, device, time):
        pass
    
    def add_device(self, deviceType):
    		if deviceType == "light":
    			device = Lightbulb(self.__name + " light", 60)
    			self.__devices.append(device)
    		elif deviceType == "speaker":
    			device = Speaker(self.__name + " speaker", 30)
    			self.__devices.append(device)
    		elif deviceType == "thermostat":
    			device = Thermostat(self.__name + " thermostat", 10)
    			self.__devices.append(device)
    		elif deviceType == "plug":
    			device = Plug(self.__name + " plug", 120)
    			self.__devices.append(device)
    		elif deviceType == "fan":
    			device = Fan(self.__name + " fan", 100)
    			self.__devices.append(device)
    		elif deviceType == "lock":
    			device = Lock(self.__name + " lock", 5)
    			self.__devices.append(device)
    		elif deviceType == "security camera":
    			device = SecurityCamera(self.__name + " security camera", 60)
    			self.__devices.append(device)
    		else:
    			print("Invalid device type")
     	
    def get_power_usage(self):
        return sum(dev.wattage for dev in self.__devices)
    
    def print_room_info(self):
        print(self.name)
        for device in self.devices:
            print("\t" + str(device))