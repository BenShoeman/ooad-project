class User:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

class InfrequentUser(User):
  def __init__(self, name):
    super().__init__(name)
    self.numberInteractions = 3
    self.numAutomationTasks = 0

class RegularUser(User):
  def __init__(self, name):
    super().__init__(name)
    self.numberInteractions = 20
    self.numAutomationTasks = 2

class AutomationUser(User):
  def __init__(self, name):
    super().__init__(name)
    self.numberInteractions = 0
    self.numAutomationTasks = 10

class PowerUser(User):
  def __init__(self, name):
    super().__init__(name)
    self.numberInteractions = 20
    self.numAutomationTasks = 5

class RealUser(User):
  def __init__(self, name):
    super().__init__(name)

class Observer(User):
    pass
    #Do we need this?