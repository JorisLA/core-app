from typing import Dict, List, Optional
from uuid import UUID
from ..domain.player import Player
from ..domain.team import Team
from ..domain.fine import Fine
from ..domain.repositories import PlayerRepository, TeamRepository, FineRepository

class InMemoryPlayerRepository(PlayerRepository):
    def __init__(self):
        self.players: Dict[UUID, Player] = {}

    def get_player(self, player_id: UUID) -> Optional[Player]:
        return self.players.get(player_id)

    def get_all_players(self) -> List[Player]:
        return list(self.players.values())

    def add_player(self, player: Player) -> None:
        self.players[player.id] = player

class InMemoryTeamRepository(TeamRepository):
    def __init__(self):
        self.teams: Dict[UUID, Team] = {}

    def get_team(self, team_id: UUID) -> Optional[Team]:
        return self.teams.get(team_id)

    def get_all_teams(self) -> List[Team]:
        return list(self.teams.values())

    def add_team(self, team: Team) -> None:
        self.teams[team.id] = team

class InMemoryFineRepository(FineRepository):
    def __init__(self):
        self.fines: Dict[UUID, Fine] = {}

    def get_fine(self, fine_id: UUID) -> Optional[Fine]:
        return self.fines.get(fine_id)

    def get_all_fines(self) -> List[Fine]:
        return list(self.fines.values())

    def add_fine(self, fine: Fine) -> None:
        self.fines[fine.id] = fine
