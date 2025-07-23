import uuid
from typing import List

from redis import Redis

from app.core.redis import get_redis
from app.models.example import Example

class ExampleRepository:

    def __init__(self):
        self.client: Redis = get_redis()

    def create(self, data: Example) -> None:
        key = f"example:{uuid.uuid4()}"
        with self.client.pipeline() as pipe:
            pipe.hset(key, 'name', data.name)
            pipe.hset(key, 'value', data.value)
            pipe.execute()

    def get(self) -> List[Example]:
        keys = self.client.keys("example:*")
        examples = []

        for key in keys:
            data = self.client.hgetall(key)
            example = Example(
                        name=data[b'name'].decode(), 
                        value=data[b'value'].decode()
                        )
            examples.append(example)

        return examples

