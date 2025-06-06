from typing import List
from .player import Player
from .fine import Fine

class FineService:
    @staticmethod
    def calculate_monthly_fines(player: Player) -> float:
        return player.get_total_fines()

    @staticmethod
    def apply_fine_to_player(player: Player, fine: Fine) -> None:
        player.add_fine(fine)
