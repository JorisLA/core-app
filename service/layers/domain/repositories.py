from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from .player import Player
from .team import Team
from .fine import Fine

class PlayerRepository(ABC):
    @abstractmethod
    def get_player(self, player_id: UUID) -> Optional[Player]:
        pass

    @abstractmethod
    def get_all_players(self) -> List[Player]:
        pass

    @abstractmethod
    def add_player(self, player: Player) -> None:
        pass

class TeamRepository(ABC):
    @abstractmethod
    def get_team(self, team_id: UUID) -> Optional[Team]:
        pass

    @abstractmethod
    def get_all_teams(self) -> List[Team]:
        pass

    @abstractmethod
    def add_team(self, team: Team) -> None:
        pass

class FineRepository(ABC):
    @abstractmethod
    def get_fine(self, fine_id: UUID) -> Optional[Fine]:
        pass

    @abstractmethod
    def get_all_fines(self) -> List[Fine]:
        pass

    @abstractmethod
    def add_fine(self, fine: Fine) -> None:
        pass
