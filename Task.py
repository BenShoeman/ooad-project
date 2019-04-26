import Time

# Task.py: contains implementation of the Task class
# Authors: Mike Hering, Ben Shoeman

# Task objects change the state of Devices on an automatic basis. They run at a
# given time of the day for a given Device, and do the specified actions (which
# is a dictionary, to match the state dictionary of Devices). Tasks utilize the
# Time object to know if that time has passed or not, so they know to run.
class Task:
    # Constructor, creates a Task with a specific name, time to run, Device, and actions
    def __init__(self, name, time, device, actions=None):
        self.__name = name     # This attribute is used to identify the Task
        self.__time = time     # Time string in 24-hour format "HH:MM", used so the tasks know when to run
        self.__device = device # This is the Device the Task is changing the state of
        self.__actions = {}    # This attribute contains the actions that the Task will run on the Device
        # Only add actions that are allowable for the given Device
        if actions is not None:
            for key in actions:
                if self.__device.is_allowable_state(key):
                    self.__actions[key] = actions[key]

        self.__last_day_run = 0 # This attribute is for comparing the Tasks to the Time object
    
    @property
    def name(self):
        return self.__name
    
    @property
    def time(self):
        return self.__time
    
    @property
    def device(self):
        return self.__device
    
    # Sets the time for the Task to run.
    def set_time(self, time):
        self.__time = time
    
    # Updates the actions of the Task.
    def update_actions(self, **kwargs):
        for key in kwargs:
            if self.__device.is_allowable_state(key):
                self.__actions[key] = kwargs[key]
    
    # Performs the actions of the Task if their scheduled time has passed.
    def do_actions(self):
        # Make sure it's the right time to do the actions
        if Time.get_time().has_time_passed(self.__last_day_run, self.time):
            self.__device.change_state(**self.__actions)
            self.__last_day_run = Time.get_time().day
            print("Performed " + str(self))
    
    # Defines str(task), which is used for the TaskRunner when printing its Tasks.
    def __str__(self):
        return "Task \"{}\" for {} at {}: {}".format(self.name, self.__device.name, self.time, self.__actions)