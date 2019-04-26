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
        self._interactionsCount = 0 # This attribute is the User's limit of interactions
        self._automationsCount = 0  # This attribute is the User's limit of automations
    
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
    
    # User will interact with Room depending on its type.
    def interact(self):
        if self._interactionsCount < self._numberInteractions and random.random() < 0.2:
            self._interactionsCount += 1
            interaction = random.choice(["lights on", "lights off", "music on", "music off", "temperature"])
            details = ""
            if interaction == "lights on":
                self.__currentRoom.lights_on()
            elif interaction == "lights off":
                self.__currentRoom.lights_off()
            elif interaction == "music on":
                song = "Song {:04d}".format(random.randint(0, 9999))
                details = " to song {}".format(song)
                self.__currentRoom.play_music(song)
            elif interaction == "music off":
                self.__currentRoom.stop_music()
            else:
                temp = random.randint(68, 78)
                details = " to {} degrees".format(temp)
                self.__currentRoom.set_temperature(temp)
            print("User {} set {} in {}{}.".format(self.__name, interaction, self.__currentRoom.name, details))
    
    # User will automate tasks depending on its type.
    def automate(self):
        if self._automationsCount < self._numAutomationTasks and random.random() < 0.2:
            self._automationsCount += 1
            automation = random.choice(["lights on", "lights off", "music on", "music off", "temperature"])
            details = ""
            task_time = "{:02d}:{:02d}".format(random.randint(0,23), random.randint(0,59))
            if automation == "lights on":
                self.__currentRoom.set_light_schedule(True, task_time)
            elif automation == "lights off":
                self.__currentRoom.set_light_schedule(False, task_time)
            elif automation == "music on":
                song = "Song {:04d}".format(random.randint(0, 9999))
                details = " to song {}".format(song)
                self.__currentRoom.set_speaker_schedule(True, task_time, song=song)
            elif automation == "music off":
                self.__currentRoom.set_speaker_schedule(False, task_time)
            else:
                temp = random.randint(68, 78)
                details = " to {} degrees".format(temp)
                self.__currentRoom.set_thermostat_schedule(temp, task_time)
            print("User {} automated {} at {} in {}{}.".format(self.__name, automation, task_time, self.__currentRoom.name, details))
    
    # Resets the interactions/automations count for future simulations.
    def reset_counts(self):
        self._interactionsCount = 0
        self._automationsCount = 0
    
    # Defines str(user), which is used when displaying what Users are in the House
    def __repr__(self):
        return self.name

# InfrequentUsers only interact with the House rarely and that's it.
class InfrequentUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self._numberInteractions = 3
    self._numAutomationTasks = 0

# RegularUsers interact with the House on a more regular basis and automate a few tasks.
class RegularUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self._numberInteractions = 20
    self._numAutomationTasks = 2

# PowerUsers interact with the House a lot and automate a decent amount of tasks.
class PowerUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self._numberInteractions = 20
    self._numAutomationTasks = 5

# AutomationUsers don't interact with the House but automate a lot of tasks.   
class AutomationUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self._numberInteractions = 0
    self._numAutomationTasks = 10

# RealUsers interact and automate the House on a manual basis, so they don't
# have automatic interactions or automation.
class RealUser(User):
  def __init__(self, name, house):
    super().__init__(name, house)
    self._numberInteractions = 0
    self._numAutomationTasks = 0