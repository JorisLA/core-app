from dataclasses import dataclass
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class Fine:
    id: UUID = uuid4()
    description: str = ""
    amount: float = 0
    issued_at: datetime = datetime.now()
