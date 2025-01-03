from dataclasses import dataclass, field, asdict
from datetime import datetime
from .enums import Status, Priority

@dataclass(order=True)
class Task:
    name: str
    description: str
    category: str
    status: Status = field(default=Status.PENDING)
    priority: Priority = field(default=Priority.NONE)
    deadline: datetime
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    

