# Time is a singleton pattern that represents the current time in the simulation
class Time:
    class __Time:
        def __init__(self):
            self.day = 1
            self.hour = 0
            self.minute = 0

        def add_day(self):
            self.day += 1
        
        def next_day(self):
            self.add_day()
            self.hour = 0
            self.minute = 0
        
        def add_hour(self):
            self.hour = (self.hour + 1) % 24
            if self.hour == 0:
                self.add_day()
        
        def add_minute(self):
            self.minute = (self.minute + 1) % 60
            if self.minute == 0:
                self.add_hour()
        
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

    __instance = None

    def get_time():
        if Time.__instance is None:
            Time.__instance = Time.__Time()
        return Time.__instance
    
    def set_and_get_time(day=None, time=None): # Day is int, Time is time string of format HH:MM
        Time.get_time() # Create singleton instance
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