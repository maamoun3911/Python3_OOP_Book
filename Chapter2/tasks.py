from datetime import datetime

last_id = 0

class Task:
    def __init__(self, text: str, accomplishment: bool =False) -> None:
        self.text, self.accomplishment = text, accomplishment
        self.creationdate = datetime.today()
        global last_id
        last_id += 1
        self.id = last_id
    
    def match(self, filter: str):
        return filter in self.text

class Tasks:
    def __init__(self) -> None:
        self.tasklist = []
    
    def add_task(self, text: str, accomplishment: bool= False):
        self.tasklist.append(Task(text, accomplishment))
    
    def _find_task(self, task_id: int) -> None|Task:
        for task in self.tasklist:
            if task.id == task_id:
                return task
        return None
    
    def modify_task(self, task_id: int, accomplishment: bool= False, text: str = ""):
        task = self._find_task(task_id)
        if task and text:
            task.text = text
        if task and task.accomplishment != accomplishment:
            task.accomplishment = accomplishment

    def delete_task(self, task_id: int) -> str:
        for task in self.tasklist:
            if task.id == task_id:
                self.tasklist.pop(self.tasklist.index(task))
                return "Task Deleter"
        return "Not Found Tis task id"

    def show_tasks(self) -> list[Task]:
        return [f"{task.id}-{task.accomplishment}-{task.text}" for task in self.tasklist]