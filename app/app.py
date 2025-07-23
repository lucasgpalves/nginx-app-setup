from fastapi import FastAPI
from app.routes.router import router

app = FastAPI(root_path="/api/v1")

app.include_router(router)

def main():
    import uvicorn 
    uvicorn.run(
        app, 
        host="0.0.0.0",
        port=8000
    )