from Room import *

class House:
    def __init__(self):
        self.__rooms = []
        self.__users = []

    @property
    def rooms(self):
        return tuple(self.__rooms)
    
    def add_room(self, name):
        self.__rooms.append(Room(name))
    
    def get_overall_power_usage(self):
        return sum(room.get_power_usage() for room in self.__rooms)