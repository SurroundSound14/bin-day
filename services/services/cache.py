import redis
import os
import json

redis_client = redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

def get(key):
    value = redis_client.get(key)
    return json.loads(value) if value else None

def set(key, value, ttl=86400):
    redis_client.setex(key, ttl, json.dumps(value))
