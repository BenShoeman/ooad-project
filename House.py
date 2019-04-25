from Room import *

class House:
	def __init__(self):
		self.__rooms = []
		self.__users = []

	@property
	def rooms(self):
		return tuple(self.__rooms)
	
	@property
	def users(self):
		return tuple(self.__users)
    
	def add_room(self, name):
		room = Room(name)
		self.__rooms.append(room)
		return room
	
	def add_user(self, user):
		self.__users.append(user)

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
	
	def get_user(self, name):
		for user in self.__users:
			if user.name == name:
				return user
	
	def get_rooms(self):
		return self.__rooms
    
	def get_overall_power_usage(self):
		return sum(room.get_power_usage() for room in self.__rooms)
	
	def print_house_info(self):
		for room in self.rooms:
			room.print_room_info()