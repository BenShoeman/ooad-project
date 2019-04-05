class Device:
    def __init__(self, name, wattage):
        self.__state = {}
        self.__name = name
        self.__wattage = wattage

        # This is a list of allowed state options, which is set in each specific
        # subclass's constructor
        self.__allowed_states = []
    
    @property
    def state(self):
        return self.__state.copy()
    
    @property
    def name(self):
        return name
    
    @property
    def wattage(self):
        return wattage
    
    def change_state(self, **kwargs):
        for key in kwargs:
            if key in self.__allowed_states:
                self.__state[key] = kwargs[key]
            else:
                print(key, "is not allowed for", type(self))
    
    def is_allowable_state(self, state):
        return state in self.__allowed_states

class Lightbulb(Device):
    pass

class Speaker(Device):
    pass

class Thermostat(Device):
    pass

class Plug(Device):
    pass

class Fan(Device):
    pass

class Lock(Device):
    pass

class SecurityCamera(Device):
    pass