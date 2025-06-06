from dataclasses import dataclass, field
from typing import List
from uuid import UUID, uuid4
from .fine import Fine

@dataclass
class Team:
    id: UUID = uuid4()
    name: str = ""
    predefined_fines: List[Fine] = field(default_factory=list)

    def add_predefined_fine(self, fine: Fine):
        self.predefined_fines.append(fine)
