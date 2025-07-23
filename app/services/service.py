from typing import List

from app.models.example import Example
from app.repositories.example import ExampleRepository

class ExampleService:
    
    def __init__(self, repository: ExampleRepository = None):
        self.repository = repository or ExampleRepository()

    def create(self, data: Example) -> None:
        self.repository.create(data)
    
    def get(self) -> List[Example]:
        return self.repository.get()