# Time.py: contains implementation of the Time class
# Authors: Ben Shoeman

# Time follows the Singleton pattern. The Time object represents the current
# time in the simulation and is used by Tasks so they can determine when to run.
# The Time object provides a has_time_passed method so the Tasks don't have to
# determine that themselves and loosen the coupling between the Time and Tasks.
class Time:
    # Python doesn't support private constructors, so instead we have to use a
    # private Time class to hide the constructor.
    class __Time:
        # Constructor, creates the Time instance starting at day 1, 00:00.
        def __init__(self):
            self.day = 1    # This represents the day of the simulation
            self.hour = 0   # This represents the hour of the simulation
            self.minute = 0 # This represents the minute of the simulation

        # Goes forward one full day, going to the same hour/minute.
        def add_day(self):
            self.day += 1
        
        # Goes forward to the next day at 00:00.
        def next_day(self):
            self.add_day()
            self.hour = 0
            self.minute = 0
        
        # Goes forward one hour.
        def add_hour(self):
            self.hour = (self.hour + 1) % 24
            if self.hour == 0:
                self.add_day()
        
        # Goes forward one minute.
        def add_minute(self):
            self.minute = (self.minute + 1) % 60
            if self.minute == 0:
                self.add_hour()
        
        # Returns True if time has passed since the given day and time. Used by
        # Tasks to determine if they should run or not.
        def has_time_passed(self, day, time): # Day is int, time is HH:MM time string
            if day > self.day:
                return False
            elif day < self.day:
                return True
            else:
                if ':' in time and len(time) == 5:
                    time_vals = time.split(':')
                    if len(time_vals[0]) == len(time_vals[1]) and time_vals[0].isnumeric() and time_vals[1].isnumeric():
                        hour = int(time_vals[0])
                        minute = int(time_vals[1])
                    else:
                        # Time string incorrect, return None as invalid value
                        return None
                    
                    # If time string valid, check hours then minutes
                    if hour > self.hour:
                        return False
                    elif hour < self.hour:
                        return True
                    else:
                        if minute > self.minute:
                            return False
                        else:
                            return True
                else:
                    return None

    __instance = None # This is the singleton instance

    # Creates the single Time instance if it doesn't exist, and returns the instance.
    def get_time():
        if Time.__instance is None:
            Time.__instance = Time.__Time()
        return Time.__instance
    
    # Creates the single Time instance if it doesn't exist, sets the time, and
    # returns the instance.
    def set_and_get_time(day=None, time=None): # Day is int, Time is time string of format HH:MM
        if day is not None:
            Time.get_time().day = day
        if time is not None:
            if ':' in time and len(time) == 5:
                time_vals = time.split(':')
                if len(time_vals[0]) == len(time_vals[1]) and time_vals[0].isnumeric() and time_vals[1].isnumeric():
                    Time.get_time().hour = int(time_vals[0])
                    Time.get_time().minute = int(time_vals[1])
                # If the checks fail and the string is invalid, do nothing
        return Time.get_time()