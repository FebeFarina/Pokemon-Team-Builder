import requests
import json

with open('../data/type_data.json', 'w') as out:
    list = [] 
    for i in range(1, 19):
      url ="https://pokeapi.co/api/v2/type/"+str(i)+"/"
      response = requests.get(url)
      print(i)
      list.append(response.json())
    json.dump(list, out,indent=4)