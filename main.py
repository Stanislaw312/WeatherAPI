from fastapi import FastAPI
from dotenv import load_dotenv
import os
import redis
from typing import Optional
import service

app = FastAPI()
load_dotenv()
API_KEY = os.getenv('API_KEY')
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

@app.get('/weather')
@app.get('/weather/{city}')
async def weather_data(city: Optional[str] = None):
    return await service.weather_data(r, API_KEY, city)
