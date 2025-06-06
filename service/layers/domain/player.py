from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4
from .fine import Fine

@dataclass
class Player:
    id: UUID = uuid4()
    name: str = ""
    team_id: UUID = uuid4()
    fines: List[Fine] = field(default_factory=list)

    def add_fine(self, fine: Fine):
        self.fines.append(fine)

    def get_total_fines(self) -> float:
        return sum(fine.amount for fine in self.fines)
