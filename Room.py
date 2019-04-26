from Device import *
from Task import *
from TaskRunner import *

# Room.py: contains implementation of the Room class
# Authors: Mike Hering, Ben Shoeman

# The Rooms utilize the Facade pattern. A Room provides a simple means for Users
# to interact with Devices and add Tasks without having to know about those
# details. A Room contains several Devices and keeps track of/changes their
# states, and it also creates Tasks that the TaskRunner can run on those Devices.
class Room:
    # Constructor, creates an empty Room with a name and no Devices
    def __init__(self, name):
        self.__name = name  # This attribute is used to identify the Room
        self.__devices = [] # This attribute contains all Devices in the Room
    
    @property
    def name(self):
        return self.__name
    
    @property
    def devices(self):
        return tuple(self.__devices)
    
    # Gets all devices in the Room of a specific type. Mostly used as a helper
    # method for turning lights on/off, playing/pausing music, etc.
    def get_devices_of_type(self, device_type):
        return tuple(dev for dev in self.__devices if isinstance(dev, device_type))
    
    # Turns all the Lightbulbs in the Room on.
    def lights_on(self):
        lights = self.get_devices_of_type(Lightbulb)
        for light in lights:
            light.change_state(on=True)
    
    # Turns all the Lightbulbs in the Room off.
    def lights_off(self):
        lights = self.get_devices_of_type(Lightbulb)
        for light in lights:
            light.change_state(on=False)
    
    # Turns all the Speakers in the Room on and sets their song.
    def play_music(self, song):
        speakers = self.get_devices_of_type(Speaker)
        for speaker in speakers:
            speaker.change_state(on=True, song=song)
    
    # Turns all the Speakers in the Room off.
    def stop_music(self):
        speakers = self.get_devices_of_type(Speaker)
        for speaker in speakers:
            speaker.change_state(on=False)
    
    # Sets all thermostats in the Room to the specified temperature.
    def set_temperature(self, temperature):
        thermostats = self.get_devices_of_type(Thermostat)
        for thermostat in thermostats:
            thermostat.change_state(temperature=temperature)
    
    # Sets a schedule for the given Device by creating a Task and registering it
    # with the TaskRunner.
    def set_schedule(self, device, state, time):
        task = Task(device.name + " task", time, device, state)
        TaskRunner.get_task_runner().add_task(task)
    
    # Notifies the TaskRunner to remove all scheduled Tasks for a Device.
    def remove_schedule(self, device):
        TaskRunner.get_task_runner().remove_tasks_for_device(device)
    
    # Adds a device of a specific type.
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
    
    # Gets the power usage of the Room as a number of watts.
    def get_power_usage(self):
        return sum(dev.wattage for dev in self.__devices)
    
    # Prints information about the Room (specifically, its name as well as
    # Devices in the Room and their states).
    def print_room_info(self):
        print(self.name)
        if len(self.devices) == 0:
            print("\tNo devices in " + self.name)
        else:
            for device in self.devices:
                print("\t" + str(device))

    # Gets a Device by its name, or if no name is inputted, through terminal input.
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