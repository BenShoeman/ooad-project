import random

class User:
    def __init__(self, name, house):
        self.__name = name
        self.__rooms = house.get_rooms()
        self.__currentRoom = self.__rooms[random.randint(0,len(self.__rooms)-1)] #Start in a random room
        self.__interactionsCount = 0
    
    @property
    def name(self):
        return self.__name

    def getCurrentRoom(self):
      return self.__currentRoom

    def move(self):
      if random.random() > 0.5:
        self.__currentRoom = self.__rooms[random.randint(0,len(self.__rooms)-1)] #Move to a random room
      return self.__currentRoom


class InfrequentUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.numberInteractions = 3
    self.numAutomationTasks = 0

    # User randomly interacts with 50% probability if he has interactions left, otherwise 0%
    def interact(self):
        if self.__interactionsCount < self.__numberInteractions and random.random() > 0.5 :
          print("interacting")
          # Perform some action(s) in the room

class RegularUser(User):
  def __init__(self, name, house):
    super().__init__(name)
    self.numberInteractions = 20
    self.numAutomationTasks = 2

    # User randomly interacts with 50% probability if he has interactions left, otherwise 0%
    def interact(self):
        if self.__interactionsCount < self.__numberInteractions and random.random() > 0.5: 
          print("interacting")
          # Perform some action(s) in the room


class AutomationUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.numberInteractions = 0
    self.numAutomationTasks = 10

class PowerUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.numberInteractions = 20
    self.numAutomationTasks = 5

    # User randomly interacts with 50% probability if he has interactions left, otherwise 0%
    def interact(self):
        if self.__interactionsCount < self.__numberInteractions and random.random() > 0.5: 
          print("interacting")
          # Perform some action(s) in the room


class RealUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)

class Observer(User):
    pass
    #Do we need this?