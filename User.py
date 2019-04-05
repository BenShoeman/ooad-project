class User:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

class InfrequentUser(User):
    pass

class RegularUser(User):
    pass

class AutomationUser(User):
    pass

class PowerUser(User):
    pass

class RealUser(User):
    pass

class Observer(User):
    pass