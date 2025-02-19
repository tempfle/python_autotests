import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '69b9cdd9847b8ed0924e85f02883ea7b'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
TRAINER_ID = "19842"

def test_status_code():
   response = requests.get(url = f'{URL}/pokemons', params={'trainer_id': TRAINER_ID}) 
   assert response.status_code == 200

    
def test_of_response():
       response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID}) 
       assert response_get.json()["data"][0]['trainer_name'] == 'Сам Сусам'