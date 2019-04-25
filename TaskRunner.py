# TaskRunner is a singleton pattern that runs all available tasks
class TaskRunner:
    class __TaskRunner:
        def __init__(self):
            self.__tasks = []
        
        @property
        def tasks(self):
            return tuple(self.__tasks)
        
        def add_task(self, task):
            self.__tasks.append(task)
        
        def remove_task(self, task):
            self.__tasks.remove(task)
        
        def remove_tasks_for_device(self, device):
            for task in self.__tasks:
                if task.device == device:
                    self.remove_task(task)
        
        def run_tasks(self):
            for task in self.__tasks:
                task.do_actions()
        
        def print_tasks(self):
            print("Currently Running Tasks:")
            if len(self.__tasks) == 0:
                print("No tasks currently running.")
            else:
                for task in self.__tasks:
                    print("\t" + str(task))
    
    __instance = None

    def get_task_runner():
        if TaskRunner.__instance is None:
            TaskRunner.__instance = TaskRunner.__TaskRunner()
        return TaskRunner.__instance