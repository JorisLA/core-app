from typing import List
from uuid import UUID
from ..domain.fine import Fine
from ..domain.repositories import FineRepository

class FineUseCase:
    def __init__(self, fine_repo: FineRepository):
        self.fine_repo = fine_repo

    def get_fine(self, fine_id: UUID) -> Fine:
        fine = self.fine_repo.get_fine(fine_id)
        if fine is None:
            raise ValueError(f"Fine with ID {fine_id} not found")
        return fine

    def get_all_fines(self) -> List[Fine]:
        return self.fine_repo.get_all_fines()

    def add_fine(self, description: str, amount: float) -> Fine:
        fine = Fine(description=description, amount=amount)
        self.fine_repo.add_fine(fine)
        return fine
