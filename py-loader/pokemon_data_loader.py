import requests
import json

with open('../data/pokemon_data.json', 'w') as out:
    list = [] 
    for i in range(1, 386):
      url ="https://pokeapi.co/api/v2/pokemon-form/"+str(i)+"/"
      response = requests.get(url)
      print(i)
      list.append(response.json())
    json.dump(list, out, indent=4)