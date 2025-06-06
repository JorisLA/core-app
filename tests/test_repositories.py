import pytest
from uuid import uuid4
from service.layers.domain.player import Player
from service.layers.domain.team import Team
from service.layers.domain.fine import Fine
from service.layers.infrastructure.repositories import (
    InMemoryPlayerRepository,
    InMemoryTeamRepository,
    InMemoryFineRepository
)

def test_player_repository():
    repo = InMemoryPlayerRepository()
    player = Player(name="Test Player", team_id=uuid4())
    repo.add_player(player)

    retrieved = repo.get_player(player.id)
    assert retrieved == player

    players = repo.get_all_players()
    assert len(players) == 1
    assert players[0] == player

def test_team_repository():
    repo = InMemoryTeamRepository()
    team = Team(name="Test Team")
    repo.add_team(team)

    retrieved = repo.get_team(team.id)
    assert retrieved == team

    teams = repo.get_all_teams()
    assert len(teams) == 1
    assert teams[0] == team

def test_fine_repository():
    repo = InMemoryFineRepository()
    fine = Fine(description="Test Fine", amount=10.0)
    repo.add_fine(fine)

    retrieved = repo.get_fine(fine.id)
    assert retrieved == fine

    fines = repo.get_all_fines()
    assert len(fines) == 1
    assert fines[0] == fine
