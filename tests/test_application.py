import pytest
from uuid import uuid4
from service.layers.domain.player import Player
from service.layers.domain.team import Team
from service.layers.domain.fine import Fine
from service.layers.application.player_service import PlayerUseCase
from service.layers.application.team_service import TeamUseCase
from service.layers.application.fine_service import FineUseCase
from service.layers.infrastructure.repositories import (
    InMemoryPlayerRepository,
    InMemoryTeamRepository,
    InMemoryFineRepository
)

def test_player_service():
    player_repo = InMemoryPlayerRepository()
    player_service = PlayerUseCase(player_repo)

    # Create a team first
    team_id = uuid4()

    # Add player
    player = player_service.add_player(name="Test Player", team_id=team_id)

    # Get player
    retrieved = player_service.get_player(player.id)
    assert retrieved == player

    # Get all players
    players = player_service.get_all_players()
    assert len(players) == 1
    assert players[0] == player

def test_team_service():
    team_repo = InMemoryTeamRepository()
    team_service = TeamUseCase(team_repo)

    # Add team
    team = team_service.add_team(name="Test Team")

    # Get team
    retrieved = team_service.get_team(team.id)
    assert retrieved == team

    # Get all teams
    teams = team_service.get_all_teams()
    assert len(teams) == 1
    assert teams[0] == team

def test_fine_service():
    fine_repo = InMemoryFineRepository()
    fine_service = FineUseCase(fine_repo)

    # Add fine
    fine = fine_service.add_fine(description="Test Fine", amount=10.0)

    # Get fine
    retrieved = fine_service.get_fine(fine.id)
    assert retrieved == fine

    # Get all fines
    fines = fine_service.get_all_fines()
    assert len(fines) == 1
    assert fines[0] == fine
