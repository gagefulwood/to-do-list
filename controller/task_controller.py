from services.task_service import TaskService
from models.task import Task, Status

class TaskController:
    def __init__(self, service: TaskService):
        self.service = service

    def handle_add_task(self, name: str, description: str):
        task = Task(name=name, description=description)
        self.service.add_task(task)

    def handle_list_tasks(self, status: Status = None):
        tasks = self.service.get_tasks_by_status(status) if status else self.service.tasks
        for task in tasks:
            print(task)