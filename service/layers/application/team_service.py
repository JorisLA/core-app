from typing import List
from uuid import UUID
from ..domain.team import Team
from ..domain.repositories import TeamRepository
from ..domain.fine import Fine

class TeamUseCase:
    def __init__(self, team_repo: TeamRepository):
        self.team_repo = team_repo

    def get_team(self, team_id: UUID) -> Team:
        team = self.team_repo.get_team(team_id)
        if team is None:
            raise ValueError(f"Team with ID {team_id} not found")
        return team

    def get_all_teams(self) -> List[Team]:
        return self.team_repo.get_all_teams()

    def add_team(self, name: str) -> Team:
        team = Team(name=name)
        self.team_repo.add_team(team)
        return team

    def add_predefined_fine_to_team(self, team_id: UUID, fine: Fine) -> None:
        team = self.get_team(team_id)
        team.add_predefined_fine(fine)
        # We would update the repository here in a real implementation
        self.team_repo.add_team(team)
