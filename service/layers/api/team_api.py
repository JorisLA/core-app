from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from pydantic import BaseModel
from ..application.team_service import TeamUseCase
from ..infrastructure.repositories import InMemoryTeamRepository
from ..domain.fine import Fine

# Initialize repository
team_repo = InMemoryTeamRepository()

# Initialize use case
team_service = TeamUseCase(team_repo)

# Pydantic models
class FineModel(BaseModel):
    id: UUID
    description: str
    amount: float

class TeamModel(BaseModel):
    name: str
    predefined_fines: List[FineModel] = []

class TeamModelResponse(BaseModel):
    id: UUID
    name: str
    predefined_fines: List[FineModel] = []

# Create router
router = APIRouter()

# Dependency injection
def get_team_service():
    return team_service

# Team endpoints
@router.post("/", response_model=TeamModelResponse)
def create_team(team: TeamModel, team_service: TeamUseCase = Depends(get_team_service)):
    return team_service.add_team(name=team.name)

@router.get("/", response_model=List[TeamModelResponse])
def read_teams(team_service: TeamUseCase = Depends(get_team_service)):
    return team_service.get_all_teams()

@router.get("/{team_id}", response_model=TeamModelResponse)
def read_team(team_id: UUID, team_service: TeamUseCase = Depends(get_team_service)):
    try:
        return team_service.get_team(team_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Add predefined fine to team
@router.post("/{team_id}/fines/")
def add_predefined_fine_to_team(
    team_id: UUID,
    fine: FineModel,
    team_service: TeamUseCase = Depends(get_team_service)
):
    try:
        fine_entity = Fine(description=fine.description, amount=fine.amount)
        team_service.add_predefined_fine_to_team(team_id, fine_entity)
        return {"message": "Predefined fine added to team successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
