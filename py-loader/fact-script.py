import json

with open('../data/pokemon_data.json', 'r') as pokemon_data:
    type_data = json.load(pokemon_data)
    pokemon_list = []
    type_list = []
    for pokemon in type_data:
      name = pokemon['name']
      pokemon_fact = 'pokemon('+name.lower()+').'
      pokemon_list.append(pokemon_fact)
      types = pokemon['types']
      for t in types:
        type = t['name']
        type_list.append('type('+name.lower()+','+type.lower()+').')
    out = open('../src/pokemon_facts.pl','w+')
    for p in pokemon_list:
      out.write(p+'\n')
    for t in type_list:
      out.write(t+'\n')
    out.close()