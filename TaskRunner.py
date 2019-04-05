import time

# taskrunner.run_tasks() will need to be run in a separate thread, since it runs
# in an infinite loop
class TaskRunner:
    def __init__(self):
        self.__tasks = []
    
    @property
    def tasks(self):
        return tuple(self.__tasks)
    
    def add_task(self, task):
        self.__tasks.append(task)
    
    def remove_task(self, task):
        self.__tasks.remove(task)
    
    def run_tasks(self):
        while True:
            for task in self.__tasks:
                task.do_actions()
            time.sleep(60)