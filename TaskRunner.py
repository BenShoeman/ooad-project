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
        
        def run_tasks(self):
            for task in self.__tasks:
                task.do_actions()
    
    __instance = None

    def get_task_runner():
        if TaskRunner.__instance is None:
            TaskRunner.__instance = __TaskRunner()
        return TaskRunner.__instance