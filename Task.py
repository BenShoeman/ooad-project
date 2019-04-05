import time

class Task:
    def __init__(self, name, time, device, actions=None):
        self.__name = name
        self.__time = time # time is a time string, in 24-hour time HH:MM
        self.__device = device
        self.__actions = {}
        if actions is not None:
            for key in actions:
                if self.__device.is_allowable_state(key):
                    self.__actions[key] = actions[key]

        self.__actions = actions if actions is not None else {}
    
    @property
    def name(self):
        return name
    
    @property
    def time(self):
        return time
    
    def set_time(self, time):
        self.__time = time
    
    def update_actions(self, **kwargs):
        for key in kwargs:
            if self.__device.is_allowable_state(key):
                self.__actions[key] = kwargs[key]
    
    def do_actions(self):
        # Make sure it's the right time to do the actions
        if time.strftime("%H:%M", time.localtime()) == self.time:
            self.__device.change_state(**self.__actions)