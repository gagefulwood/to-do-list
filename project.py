from dataclasses import dataclass
from datetime import datetime
from typing import List
from sprint import Sprint

@dataclass
class Project:
    id: str
    name: str
    description: str
    sprints: List[Sprint]
    deadline: datetime
    created_at: datetime
    updated_at: datetime