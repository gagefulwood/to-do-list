from dataclasses import dataclass
from datetime import datetime
from typing import List
from task import Task

@dataclass
class Sprint:
    id: str
    name: str
    goal: str
    tasks: List[Task]
    status: str
    start_date: datetime
    end_date: datetime