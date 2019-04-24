import Time

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

        # This is for comparing the tasks to the Time object
        self.__last_day_run = 0
    
    @property
    def name(self):
        return self.__name
    
    @property
    def time(self):
        return self.__time
    
    def set_time(self, time):
        self.__time = time
    
    def update_actions(self, **kwargs):
        for key in kwargs:
            if self.__device.is_allowable_state(key):
                self.__actions[key] = kwargs[key]
    
    def do_actions(self):
        # Make sure it's the right time to do the actions
        if Time.get_time().has_time_passed(self.__last_day_run, self.time):
            self.__device.change_state(**self.__actions)
            self.__last_day_run = Time.get_time().day