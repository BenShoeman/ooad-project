import random # THIRD PARTY LIB USED IN THIS FILE, to randomize User behavior.

# User.py: contains implementation of the User class as well as its subclasses
# Authors: Mike Hering

# User objects represent the users within the smarthome. They can interact
# (change the state of devices by using Rooms they are in) or they can automate
# (schedule changing device state using Rooms they are in). They each have an
# interaction and automation limit based on what kind of user they are, which is
# defined via subclassing.
class User:
    # Constructor, creates a User with a name and associated House, and places them in a random Room.
    def __init__(self, name, house):
        self.__name = name               # This attribute is used to identify the User
        self.__rooms = house.get_rooms() # This attribute tells the Users what Rooms it can access
        house.add_user(self)
        # This attribute is the Room the User is currently in
        self.__currentRoom = self.__rooms[random.randint(0,len(self.__rooms)-1)] #Start in a random room
        self.__interactionsCount = 0 # This attribute is the User's limit of interactions
        self.__automationsCount = 0  # This attribute is the User's limit of automations
    
    @property
    def name(self):
        return self.__name

    # Gets the Room the User is currently located in.
    def getCurrentRoom(self):
      return self.__currentRoom

    # Moves the User to a different Room in the House randomly.
    def move(self):
      if random.random() > 0.5:
        self.__currentRoom = self.__rooms[random.randint(0,len(self.__rooms)-1)] #Move to a random room
      return self.__currentRoom
    
    # Defined in subclasses, User will interact with Room depending on its type.
    def interact(self):
        pass
    
    # Defined in subclasses, User will automate tasks depending on its type.
    def automate(self):
        pass
    
    # Defines str(user), which is used when displaying what Users are in the House
    def __repr__(self):
        return self.name

# InfrequentUsers only interact with the House rarely and that's it.
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

# RegularUsers interact with the House on a more regular basis and automate a few tasks.
class RegularUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
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

# PowerUsers interact with the House a lot and automate a decent amount of tasks.
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

# AutomationUsers don't interact with the House but automate a lot of tasks.   
class AutomationUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self.__numberInteractions = 0
    self.__numAutomationTasks = 10

    def automate(self):
        if self.__automationsCount < self.__automationsCount and random.random() > 0.5: 
          print("automating a device")

# RealUsers interact and automate the House on a manual basis, hence why there
# is no implementation.
class RealUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)