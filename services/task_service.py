from datetime import datetime
from models.task import Task
from models.enums import Status, Priority

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks_by_status(self, status: Status):
        return [task for task in self.tasks if task.status == status]
    
    def get_tasks_by_priority(self, priority: Priority):
        return [task for task in self.tasks if task.priority == priority]
    
    def get_tasks_by_deadline(self, deadline: datetime): #tweak this to be more robust
        return [task for task in self.tasks if task.deadline == deadline]
    
    def update_task(self, task: Task, **kwargs):
        for key, value in kwargs.items():
            setattr(task, key, value)
        task.updated_at = datetime.now()