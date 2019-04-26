from Room import *

# House.py: contains implementation of the House class
# Authors: Mike Hering, Ben Shoeman

# The House is the foundation of the smarthome, which contains all the Rooms and
# Users of the smarthome. The House also aggregates information like overall
# power usage, info about rooms and devices, etc.
class House:
	# Constructor, creates an empty House with no Rooms or Users
	def __init__(self):
		self.__rooms = [] # This attribute contains all Rooms in the House
		self.__users = [] # This attribute contains all Users in the House

	@property
	def rooms(self):
		return tuple(self.__rooms)
	
	@property
	def users(self):
		return tuple(self.__users)
    
	# Adds a Room with a specific name.
	def add_room(self, name):
		room = Room(name)
		self.__rooms.append(room)
		return room
	
	# Adds a User to the home.
	def add_user(self, user):
		self.__users.append(user)

	# Gets a Room by its name, or if no name is inputted, through terminal input.
	def get_room(self, name=None):
		if name is not None:
			for room in self.__rooms:
				if room.name == name:
					return room
		else:
			while (True):
				print("Enter name of room:")
				roomName = input("> ")

				for r in self.__rooms:
					n = r.name
					if roomName == n:
						return r
				
				print("Room not found \n")
	
	# Gets a User by its name.
	def get_user(self, name):
		for user in self.__users:
			if user.name == name:
				return user
	
	# Gets the Rooms in the House.
	def get_rooms(self):
		return self.__rooms

	# Gets the House's overall power usage as a number of watts.
	def get_overall_power_usage(self):
		return sum(room.get_power_usage() for room in self.__rooms)
	
	# Prints information about the House (specifically, what Rooms are in the
	# House as well as Devices in those Rooms and their states).
	def print_house_info(self):
		for room in self.rooms:
			room.print_room_info()

	# Turns off all lights and speakers in the House and sets the thermostats to
	# 68 degrees.
	def sleep(self):
		for room in self.rooms:
			room.lights_off()
			room.stop_music()
			room.set_temperature(68)

	# Turns on the lights of the House entry.
	def wake(self):
		self.get_room("Entry").lights_on()