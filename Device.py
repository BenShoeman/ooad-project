class Device:
    def __init__(self, name, wattage):
        self.__state = {}
        self.__name = name
        self.__wattage = wattage

        try:
            self.__allowed_states # Check if value exists. If not, make an empty list
        except AttributeError:
            # This is a list of allowed state options, which is set in each specific
            # subclass's constructor, along with default values
            self.__allowed_states = []
        self.reset_state()
    
    @property
    def state(self):
        return self.__state.copy()
    
    @property
    def allowed_states(self):
        return tuple(x for x,_ in self.__allowed_states)
    
    @property
    def name(self):
        return name
    
    @property
    def wattage(self):
        return wattage
    
    def reset_state(self):
        for state, value in self.__allowed_states:
            self.__state[state] = value
    
    def change_state(self, **kwargs):
        for key in kwargs:
            if self.is_allowable_state(key):
                self.__state[key] = kwargs[key]
            else:
                print(key, "is not allowed for", type(self))
    
    def is_allowable_state(self, state):
        return state in (x for x,_ in self.__allowed_states)

class Lightbulb(Device):
    def __init__(self, name, wattage=10):
        self.__allowed_states = [("on", False), ("brightness", 1)]
        super().__init__(name, wattage)

class Speaker(Device):
    def __init__(self, name, wattage=5):
        self.__allowed_states = [("on", False), ("song", "")]
        super().__init__(name, wattage)

class Thermostat(Device):
    def __init__(self, name, wattage=2):
        self.__allowed_states = [("temperature", 70), ("ac_on", False), ("heat_on", False)]
        super().__init__(name, wattage)

class Plug(Device):
    def __init__(self, name, wattage=1):
        self.__allowed_states = [("on", False)]
        super().__init__(name, wattage)

class Fan(Device):
    def __init__(self, name, wattage=50):
        self.__allowed_states = [("on", False)]
        super().__init__(name, wattage)

class Lock(Device):
    def __init__(self, name, wattage=1):
        self.__allowed_states = [("on", False)]
        super().__init__(name, wattage)

class SecurityCamera(Device):
    def __init__(self, name, wattage=2):
        self.__allowed_states = [("on", False)]
        super().__init__(name, wattage)