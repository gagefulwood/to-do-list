from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: str
    name: str
    description: str
    category: str
    status: str
    priority: int
    deadline: datetime
    created_at: datetime
    updated_at: datetime


