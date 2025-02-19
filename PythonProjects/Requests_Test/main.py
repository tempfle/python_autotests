import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '69b9cdd9847b8ed0924e85f02883ea7b'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}

body_registration ={
    "trainer_token": TOKEN,
    "email": "mixa-lych97@mail.ru",
    "password": "Iloveqastudio1"
} 

body_confirmation= {
    "trainer_token": TOKEN
    }
body_create= {
    "name": "Никитос",
    "photo_id": "48"
}
body_change_name = {
    "pokemon_id": "239217",
    "name": "лосось",
    "photo_id": "522"
}
body_add_pokeball = {
    "pokemon_id": "239217"
}

'''response = requests.post(url= f'{URL}/trainers/trainer_reg', headers = HEADER, json= body_registration)
print(response.text)

response_confirmation= requests.post(url= f'{URL}/trainers/confirm_email',headers = HEADER, json =body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url= f'{URL}/pokemons',headers = HEADER, json =body_create)
print(response_create.text)'''


response_change_name = requests.put(url= f'{URL}/pokemons',headers = HEADER, json =body_change_name)
print(response_change_name.text)

response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball',headers = HEADER, json =body_add_pokeball)