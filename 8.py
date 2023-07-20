import requests
from pprint import pprint
import json
responses = list()
ids = ['1','2','3','4','5','6']
for id in ids:
    url = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = json.loads(url.text)
    responses.append(data)
    id = url.json()
    pokemon = url.text
    parse_json = json.loads(pokemon)
    id = parse_json['id']
    name = parse_json['name']
    height = parse_json['height']
    weight = parse_json['weight']
    print(f'id: {id}\nname: {name}\nheight: {height}\nweight: {weight}\n')

response = requests.get("https://pokeapi.co/api/v2/pokemon/")
response_dict = response.json()
names = [response_dict['results'][0]['name'],
response_dict['results'][1]['name'],
response_dict['results'][2]['name'],
response_dict['results'][3]['name'],response_dict['results'][4
]['name'],response_dict['results'][5]['name']]

with open('pokemon.txt', 'w') as file:
    for name in names:
        file.writelines(name+"\n")
file.close()