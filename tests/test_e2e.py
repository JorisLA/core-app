import pytest
from fastapi.testclient import TestClient
from service.__main__ import APP
from uuid import UUID

client = TestClient(APP)

def test_create_and_get_team():
    # Create team
    response = client.post("/teams/", json={"name": "Team A"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Team A"
    team_id = data["id"]

    # Get team
    response = client.get(f"/teams/{team_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == team_id
    assert data["name"] == "Team A"

def test_create_and_get_player():
    # First create a team
    team_response = client.post("/teams/", json={"name": "Team B"})
    team_id = team_response.json()["id"]

    # Create player
    response = client.post("/players/", json={"name": "Player 1", "team_id": str(team_id)})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Player 1"
    assert UUID(data["team_id"]) == UUID(team_id)
    player_id = data["id"]

    # Get player
    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == player_id
    assert data["name"] == "Player 1"
    assert UUID(data["team_id"]) == UUID(team_id)

def test_add_fine_to_player():
    # First create a player
    team_response = client.post("/teams/", json={"name": "Team C"})
    team_id = team_response.json()["id"]
    player_response = client.post("/players/", json={"name": "Player 2", "team_id": str(team_id)})
    player_id = player_response.json()["id"]
    fine_response = client.post("/fines/", json={"description": "OUBLI", "amount": 2})
    fine_id = fine_response.json()["id"]

    # Add fine to player
    response = client.put(f"/players/{player_id}/fines/{fine_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Fine added to player successfully"

    # Verify fine was added
    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    player_data = response.json()
    assert "fines" in player_data
    assert len(player_data["fines"]) == 1
    assert player_data["fines"][0]["description"] == "OUBLI"
    assert player_data["fines"][0]["amount"] == 2

def test_add_predefined_fine_to_team():
    # First create a team
    response = client.post("/teams/", json={"name": "Team D"})
    assert response.status_code == 200
    data = response.json()
    team_id = data["id"]

    # Add predefined fine to team
    response = client.post(f"/teams/{team_id}/fines/", json={"description": "Late fee", "amount": 10.0})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Predefined fine added to team successfully"

    # Verify fine was added
    response = client.get(f"/teams/{team_id}")
    assert response.status_code == 200
    team_data = response.json()
    assert "predefined_fines" in team_data
    assert len(team_data["predefined_fines"]) == 1
    assert team_data["predefined_fines"][0]["description"] == "Late fee"
    assert team_data["predefined_fines"][0]["amount"] == 10.0
