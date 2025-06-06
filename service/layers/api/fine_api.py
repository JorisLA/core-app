from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from pydantic import BaseModel
from ..application.fine_service import FineUseCase
from ..infrastructure.repositories import InMemoryFineRepository

# Initialize repository
fine_repo = InMemoryFineRepository()

# Initialize use case
fine_service = FineUseCase(fine_repo)

# Pydantic models
class FineModel(BaseModel):
    description: str
    amount: float

class FineModelResponse(BaseModel):
    id: UUID
    description: str
    amount: float

# Create router
router = APIRouter()

# Dependency injection
def get_fine_service():
    return fine_service

# Fine endpoints
@router.post("/", response_model=FineModelResponse)
def create_fine(fine: FineModel, fine_service: FineUseCase = Depends(get_fine_service)):
    return fine_service.add_fine(description=fine.description, amount=fine.amount)

@router.get("/", response_model=List[FineModelResponse])
def read_fines(fine_service: FineUseCase = Depends(get_fine_service)):
    return fine_service.get_all_fines()

@router.get("/{fine_id}", response_model=FineModelResponse)
def read_fine(fine_id: UUID, fine_service: FineUseCase = Depends(get_fine_service)):
    try:
        return fine_service.get_fine(fine_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
