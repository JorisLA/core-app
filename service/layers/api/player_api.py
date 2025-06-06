from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from pydantic import BaseModel
from ..api.fine_api import get_fine_service
from ..application.fine_service import FineUseCase
from ..application.player_service import PlayerUseCase
from ..infrastructure.repositories import InMemoryPlayerRepository
from ..infrastructure.repositories import InMemoryFineRepository
from ..domain.fine import Fine

# Initialize repository
player_repo = InMemoryPlayerRepository()
# Initialize use case
player_service = PlayerUseCase(player_repo)

# Pydantic models
class FineModel(BaseModel):
    id: UUID

class PlayerModel(BaseModel):
    name: str
    team_id: UUID
    fines: List[FineModel] = []

class PlayerModelResponse(BaseModel):
    id: UUID
    name: str
    team_id: UUID
    fines: List[FineModel] = []

# Create router
router = APIRouter()

# Dependency injection
def get_player_service():
    return player_service

# Player endpoints
@router.post("/", response_model=PlayerModelResponse)
def create_player(player: PlayerModel, player_service: PlayerUseCase = Depends(get_player_service)):
    return player_service.add_player(name=player.name, team_id=player.team_id)

@router.get("/", response_model=List[PlayerModelResponse])
def read_players(player_service: PlayerUseCase = Depends(get_player_service)):
    return player_service.get_all_players()

@router.get("/{player_id}", response_model=PlayerModelResponse)
def read_player(player_id: UUID, player_service: PlayerUseCase = Depends(get_player_service)):
    try:
        return player_service.get_player(player_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Add fine to player
@router.put("/{player_id}/fines/{fine_id}")
def add_fine_to_player(
    player_id: UUID,
    fine_id: UUID,
    player_service: PlayerUseCase = Depends(get_player_service),
    fine_service: FineUseCase = Depends(get_fine_service),
):
    try:
        fine: Fine = fine_service.get_fine(fine_id=fine_id)
        player_service.add_fine_to_player(player_id, fine.id)
        return {"message": "Fine added to player successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
