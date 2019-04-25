class Device:
    def __init__(self, name, wattage):
        self.__state = {}
        self.__name = name
        self.__wattage = wattage

        try:
            self._allowed_states # Check if value exists. If not, make an empty list
        except AttributeError:
            # This is a list of allowed state options, which is set in each specific
            # subclass's constructor, along with default values
            self._allowed_states = []
        self.reset_state()
    
    @property
    def state(self):
        return self.__state.copy()
    
    @property
    def allowed_states(self):
        return tuple(x for x,_ in self._allowed_states)
    
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
    
    def reset_state(self):
        for state, value in self._allowed_states:
            self.__state[state] = value
    
    def change_state(self, **kwargs):
        for key in kwargs:
            if self.is_allowable_state(key):
                self.__state[key] = kwargs[key]
                return True
            else:
                print(key, "is not allowed for", type(self))
                return False
    
    def is_allowable_state(self, state):
        return state in (x for x,_ in self._allowed_states)
    
    def __str__(self):
        return "{} ({}W {}): {}".format(self.name, self.wattage, self.__class__.__name__, self.state)

class Lightbulb(Device):
    def __init__(self, name, wattage=10):
        self._allowed_states = [("on", False), ("brightness", 1)]
        super().__init__(name, wattage)

class Speaker(Device):
    def __init__(self, name, wattage=5):
        self._allowed_states = [("on", False), ("song", "")]
        super().__init__(name, wattage)

class Thermostat(Device):
    def __init__(self, name, wattage=2):
        self._allowed_states = [("temperature", 70), ("ac_on", False), ("heat_on", False)]
        super().__init__(name, wattage)

class Plug(Device):
    def __init__(self, name, wattage=1):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)

class Fan(Device):
    def __init__(self, name, wattage=50):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)

class Lock(Device):
    def __init__(self, name, wattage=1):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)

class SecurityCamera(Device):
    def __init__(self, name, wattage=2):
        self._allowed_states = [("on", False)]
        super().__init__(name, wattage)