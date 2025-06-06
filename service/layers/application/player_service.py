from typing import List
from uuid import UUID
from ..domain.player import Player
from ..domain.repositories import PlayerRepository
from ..domain.fine import Fine
from ..domain.services import FineService

class PlayerUseCase:
    def __init__(self, player_repo: PlayerRepository):
        self.player_repo = player_repo

    def get_player(self, player_id: UUID) -> Player:
        player = self.player_repo.get_player(player_id)
        if player is None:
            raise ValueError(f"Player with ID {player_id} not found")
        return player

    def get_all_players(self) -> List[Player]:
        return self.player_repo.get_all_players()

    def add_player(self, name: str, team_id: UUID) -> Player:
        player = Player(name=name, team_id=team_id)
        self.player_repo.add_player(player)
        return player

    def add_fine_to_player(self, player_id: UUID, fine: Fine) -> None:
        player = self.get_player(player_id)
        FineService.apply_fine_to_player(player, fine)
        # We would update the repository here in a real implementation
        self.player_repo.add_player(player)
