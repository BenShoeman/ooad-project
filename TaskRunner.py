# TaskRunner.py: contains implementation of the TaskRunner class
# Authors: Ben Shoeman

# The TaskRunner follows the Singleton pattern. The TaskRunner manages all the
# Tasks for the smarthome and tells the Tasks to run. It also aggregates info
# about the Tasks it contains and prints that info when needed.
class TaskRunner:
    # Python doesn't support private constructors, so instead we have to use a
    # private TaskRunner class to hide the constructor.
    class __TaskRunner:
        # Constructor, creates a TaskRunner with no tasks
        def __init__(self):
            self.__tasks = []
        
        @property
        def tasks(self):
            return tuple(self.__tasks)
        
        # Adds a Task to the TaskRunner.
        def add_task(self, task):
            self.__tasks.append(task)
        
        # Removes a Task from the TaskRunner.
        def remove_task(self, task):
            self.__tasks.remove(task)
        
        # Removes all Tasks associated with a particular Device.
        def remove_tasks_for_device(self, device):
            for task in self.__tasks:
                if task.device == device:
                    self.remove_task(task)
        
        # Tells all Tasks to do their actions.
        def run_tasks(self):
            for task in self.__tasks:
                task.do_actions()
        
        # Prints information about all the current scheduled Tasks.
        def print_tasks(self):
            print("Currently Running Tasks:")
            if len(self.__tasks) == 0:
                print("No tasks currently running.")
            else:
                for task in self.__tasks:
                    print("\t" + str(task))
    
    __instance = None # This is the singleton instance

    # Creates the single TaskRunner instance if it doesn't exist, and returns
    # the instance.
    def get_task_runner():
        if TaskRunner.__instance is None:
            TaskRunner.__instance = TaskRunner.__TaskRunner()
        return TaskRunner.__instance