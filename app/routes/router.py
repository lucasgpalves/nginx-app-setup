from typing import List

from fastapi import APIRouter

from app.models.example import Example
from app.services.service import ExampleService

router = APIRouter()
service = ExampleService()

@router.get("/")
def hello_world():
    return {"Hello": "World"}

@router.post("/examples")
def create_example(data: Example):
    return service.create(data)

@router.get("/examples", response_model=List[Example])
def get_example():
    return service.get()