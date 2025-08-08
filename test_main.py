from fastapi.testclient import TestClient
from main import app
import random

client = TestClient(app)

def test_main_Warsaw():
    response = client.get('/weather/Warsaw')
    assert response.status_code == 200
    data = response.json()
    assert 'Warsaw' in data
    assert 'clouds' in data['Warsaw']
    assert 'temperature' in data['Warsaw']
    assert 'pressure' in data['Warsaw']
    assert 'humidity' in data['Warsaw']
    assert 'wind speed' in data['Warsaw']
  
#polskie znaki  
def test_main_Poznań():
    response = client.get('/weather/Poznań')
    assert response.status_code == 200
    data = response.json()
    assert 'Poznań' in data
    assert 'clouds' in data['Poznań']
    assert 'temperature' in data['Poznań']
    assert 'pressure' in data['Poznań']
    assert 'humidity' in data['Poznań']
    assert 'wind speed' in data['Poznań']
    
#spacje
def test_main_New_York():
    response = client.get('/weather/New York')
    assert response.status_code == 200
    data = response.json()
    assert 'New York' in data
    assert 'clouds' in data['New York']
    assert 'temperature' in data['New York']
    assert 'pressure' in data['New York']
    assert 'humidity' in data['New York']
    assert 'wind speed' in data['New York']
    
#różne nazwy
def test_main_alternative_names():
    response1 = client.get('/weather/Warszawa')
    response2 = client.get('/weather/Warsaw')
    assert response1.status_code == 200
    assert response2.status_code == 200
    data1 = response1.json()['Warszawa']
    data2 = response1.json()['Warszawa']
    assert data1['clouds'] == data2['clouds']
    assert data1['temperature'] == data2['temperature']
    assert data1['pressure'] == data2['pressure']
    assert data1['humidity'] == data2['humidity']
    assert data1['wind speed'] == data2['wind speed']
    
#typy danych
def test_main_datatypes():
    city = random.choice(["Warsaw", "Berlin", "Paris", "London", "Rome", "Madrid", "Oslo", "Vienna",
    "Prague", "Budapest", "Lisbon", "Athens", "Dublin", "Brussels", "Stockholm",
    "Copenhagen", "Helsinki", "Amsterdam", "Zurich", "Munich", "Barcelona"])
    response = client.get(f'/weather/{city}')
    assert response.status_code == 200
    data = response.json()[city]
    assert isinstance(data['clouds'], int)
    assert data['clouds'] >= 0 and data['clouds'] <= 100
    assert isinstance(data['temperature'], (int, float))
    assert isinstance(data['pressure'], int)
    assert isinstance(data['humidity'], (int, float))
    assert data['humidity'] >= 0 and data['humidity'] <= 100
    assert isinstance(data['wind speed'], (int, float))
    
#nie znaleziono miasta
def test_invalid_city_name():
    response = client.get('/weather/TratatatataTakanazwamiastanapewnonieinstniejebulbulbul')
    assert response.status_code == 404
    assert response.json() == {'detail' : 'City not found'}
    
    