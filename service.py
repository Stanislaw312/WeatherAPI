from fastapi import FastAPI, HTTPException
import httpx
import json
import os
import redis
from typing import Optional

async def weather_data(r, API_KEY, city: Optional[str] = None):
    if not city:
        return {'city' : 'not found'}
    if (r.exists(city)):
        weather = json.loads(r.get(city))
        return {'city': city, 'weather': weather, 'source': 'cache', 'cache ttl': r.ttl(city)}
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        if response.status_code == 404:
            return {'city' : 'not found'}

        if response.status_code != 200:
            return {"error": data.get("message", "Nie udało się pobrać danych.")}
    
    weather = {'clouds' : data['clouds']['all'],
              'temperature' : data["main"]["temp"],
              'pressure' : data["main"]["pressure"],
              'humidity' : data["main"]["humidity"],
              'wind speed' : data['wind']['speed']}
    
    r.setex(city, 1800, json.dumps(weather))
        
    return {'city': city, 'weather': weather, 'source': 'api', 'cache ttl': r.ttl(city)}