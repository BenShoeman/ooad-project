from Device import *
from Task import *
from TaskRunner import *

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
    
    def set_schedule(self, device, state, time):
        task = Task(device.name + " task", time, device, state)
        TaskRunner.get_task_runner().add_task(task)
    
    def remove_schedule(self, device):
        TaskRunner.get_task_runner().remove_tasks_for_device(device)
    
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
                return False
            return True
     	
    def get_power_usage(self):
        return sum(dev.wattage for dev in self.__devices)
    
    def print_room_info(self):
        print(self.name)
        if len(self.devices) == 0:
            print("\tNo devices in " + self.name)
        else:
            for device in self.devices:
                print("\t" + str(device))

    def get_device(self, name=None):
	    if name is not None:
		    for device in self.__devices:
			    if device.name == name:
				    return device
	    else:
		    while (True):
			    print("Enter name of device:")
			    deviceName = input("> ")

			    for d in self.__devices:
				    n = d.name
				    if deviceName == n or n == self.__name + " " + deviceName:
					    return d
				
			    print("Device not found \n")