from Room import *

class House:
	def __init__(self):
		self.__rooms = []
		self.__users = []

	@property
	def rooms(self):
		return tuple(self.__rooms)
    
	def add_room(self, name):
		room = Room(name)
		self.__rooms.append(room)
		return room

	def get_room(self):
		while (True):
			print("Enter name of room:")
			roomName = input("> ")

			for r in self.__rooms:
				n = r.name
				if roomName == n:
					return r
			
			print("Room not found \n")
    
	def get_overall_power_usage(self):
		return sum(room.get_power_usage() for room in self.__rooms)
	
	def print_house_info(self):
		for room in self.rooms:
			room.print_room_info()