class Task:
    def __init__(self, name, time, device, actions=None):
        self.__name = name
        self.__time = time
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
    
    def set_time(self, time):
        self.__time = time
    
    def update_actions(self, **kwargs):
        for key in kwargs:
            if self.__device.is_allowable_state(key):
                self.__actions[key] = kwargs[key]
    
    def __do_actions(self): # We'll need this task to run itself on a timer or the like
        self.__device.change_state(**self.__actions)