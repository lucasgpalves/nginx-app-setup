import os
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

HOST=os.getenv("REDIS_HOST")
PORT=int(os.getenv("REDIS_PORT"))

r = Redis(
    host=HOST,
    port=PORT,
)

def get_redis() -> Redis:
    return r