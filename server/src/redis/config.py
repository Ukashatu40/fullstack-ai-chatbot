import os
from dotenv import load_dotenv
import json

load_dotenv()

try:
    import redis.asyncio as redis_async
except ImportError as exc:
    raise ImportError(
        "The server Redis client requires 'redis.asyncio'. "
        "Install it in the server environment with: pip install redis>=4.5.0"
    ) from exc

class Redis():
    def __init__(self):
        """initialize connection"""
        self.REDIS_URL = os.environ['REDIS_URL']
        self.REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
        self.REDIS_USER = os.environ.get('REDIS_USER')
        self.REDIS_HOST = os.environ.get('REDIS_HOST')
        self.REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
        
        if self.REDIS_URL and self.REDIS_URL.startswith(('redis://', 'rediss://')):
            self.connection_url = self.REDIS_URL
        else:
            self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"

    async def create_connection(self):
        self.connection = redis_async.from_url(
            self.connection_url, db=0)
        return self.connection

    async def create_rejson_connection(self):
        """Create async Redis connection for JSON operations."""
        return await self.create_connection()