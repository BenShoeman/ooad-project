# Device.py: contains implementation of the Device class as well as its subclasses
# Authors: Mike Hering, Ben Shoeman

# Device objects represent the actual devices in the smarthome. They have an
# associated state that indicates whether the device is on/off, what music it is
# playing, etc. based on what kind of device it is (the kind being determined by
# subclassing).
class Device:
    def __init__(self, name, wattage):
        self.__state = {}        # This attribute is used to represent the state of the device (on/off status, song playing, etc.)
        self.__name = name       # This attribute is used to identify the Device
        self.__wattage = wattage # This attribute is used to calculate overall Room/House wattage

        # Check if value exists. If not, make an empty list
        try:
            self._allowed_states # This attribute is used to define what states are allowed.
                                 # For example, a Speaker has an associated song that plays
                                 # on it, but that would not make sense for a Lightbulb
        except AttributeError:
            # This is a list of allowed state options, which is set in each specific
            # subclass's constructor, along with default values
            self._allowed_states = []
        self.reset_state() # Set the default values
    
    @property
    def state(self):
        return self.__state.copy()
    
    @property
    def allowed_states(self):
        return tuple(x for x,_ in self._allowed_states)
    
    # Gets what type a value for a specific state should be.
    def getType(self, state):
        for s, val in self._allowed_states:
            if s == state:
                return type(val)

    @property
    def name(self):
        return self.__name
    
    @property
    def wattage(self):
        return self.__wattage
    
    # Resets the Device's state to the defaults defined in allowed_states.
    def reset_state(self):
        for state, value in self._allowed_states:
            self.__state[state] = value
    
    # Changes the Device's state based on the keyword arguments.
    def change_state(self, **kwargs):
        for key in kwargs:
            if self.is_allowable_state(key):
                self.__state[key] = kwargs[key]
                return True
            else:
                print(key, "is not allowed for", type(self))
                return False
    
    # Returns True if the state is an allowable state.
    def is_allowable_state(self, state):
        return state in (x for x,_ in self._allowed_states)
    
    # Defines str(device), which is used for Rooms when printing information.
    def __str__(self):
        return "{} ({}W {}): {}".format(self.name, self.wattage, self.__class__.__name__, self.state)

# A Lightbulb represents a smart light in the Room.
# Its allowed states are "on" and "brightness".
class Lightbulb(Device):
    def __init__(self, name, wattage=10):
        self._allowed_states = [("on", False), ("brightness", 1)]
        super().__init__(name, wattage)

# A Speaker represents a smart speaker in the Room.
# Its allowed states are "on" and "song".
class Speaker(Device):
    def __init__(self, name, wattage=5):
        self._allowed_states = [("on", False), ("song", "")]
        super().__init__(name, wattage)

# A Thermostat represents a smart thermostat in the Room.
# Its allowed states are "temperature", "ac_on", and "heat_on".
class Thermostat(Device):
    def __init__(self, name, wattage=2):
        self._allowed_states = [("temperature", 70), ("ac_on", False), ("heat_on", False)]
        super().__init__(name, wattage)

# A Plug represents a smart plug in the Room.
# Its only allowed state is "on".
class Plug(Device):
    def __init__(self, name, wattage=1):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)

# A Fan represents a smart fan in the Room.
# Its only allowed state is "on".
class Fan(Device):
    def __init__(self, name, wattage=50):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)

# A Lock represents a smart lock in the Room.
# Its only allowed state is "on".
class Lock(Device):
    def __init__(self, name, wattage=1):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)

# A SecurityCamera represents a smart security camera in the Room.
# Its only allowed state is "on".
class SecurityCamera(Device):
    def __init__(self, name, wattage=2):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)