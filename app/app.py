from fastapi import FastAPI
from app.routes.router import router

app = FastAPI()

app.include_router(router, prefix='/api/v1')

def main():
    import uvicorn 
    uvicorn.run(
        app, 
        host="0.0.0.0",
        port=8000
    )