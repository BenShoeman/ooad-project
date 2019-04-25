import random

class User:
    def __init__(self, name, house):
        self.__name = name
        self.__rooms = house.get_rooms()
        house.add_user(self)
        self.__currentRoom = self.__rooms[random.randint(0,len(self.__rooms)-1)] #Start in a random room
        self.__interactionsCount = 0
        self.__automationsCount = 0
    
    @property
    def name(self):
        return self.__name

    def getCurrentRoom(self):
      return self.__currentRoom

    def move(self):
      if random.random() > 0.5:
        self.__currentRoom = self.__rooms[random.randint(0,len(self.__rooms)-1)] #Move to a random room
      return self.__currentRoom
    
    def __repr__(self):
        return self.name

class InfrequentUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.__numberInteractions = 3
    self.__numAutomationTasks = 0

    # User randomly interacts with 50% probability if he has interactions left, otherwise 0%
    def interact(self):
        if self.__interactionsCount < self.__numberInteractions and random.random() > 0.5 :
          print("interacting")
          # Perform some action(s) in the room

class RegularUser(User):
  def __init__(self, name, house):
    super().__init__(name)
    self.__numberInteractions = 20
    self.__numAutomationTasks = 2

    # User randomly interacts with 50% probability if he has interactions left, otherwise 0%
    def interact(self):
        if self.__interactionsCount < self.__numberInteractions and random.random() > 0.5: 
          print("interacting")
          # Perform some action(s) in the room

    def automate(self):
        if self.__automationsCount < self.__automationsCount and random.random() > 0.5: 
          print("automating a device")

class PowerUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.__numberInteractions = 20
    self.__numAutomationTasks = 5

    # User randomly interacts with 50% probability if he has interactions left, otherwise 0%
    def interact(self):
        if self.__interactionsCount < self.__numberInteractions and random.random() > 0.5: 
          print("interacting")
          # Perform some action(s) in the room
      
    def automate(self):
        if self.__automationsCount < self.__automationsCount and random.random() > 0.5: 
          print("automating a device")
          
class AutomationUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.__numberInteractions = 0
    self.__numAutomationTasks = 10

    def automate(self):
        if self.__automationsCount < self.__automationsCount and random.random() > 0.5: 
          print("automating a device")


class RealUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)

class Observer(User):
    pass
    #Do we need this?