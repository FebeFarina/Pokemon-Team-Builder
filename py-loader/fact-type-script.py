import json
with open('../data/type_data.json') as poke_data:
    effective_list = []
    t_list = []
    typel = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
    data = json.load(poke_data)

    for i in data :
        type = i['name']
        t_list.append('type('+type.lower()+').')
        type_list = []
        for ie in i['damage_relations']['half_damage_to'] :
            ineff = ie['name']
            type_list.append(ineff)
            effective_list.append('effective('+type.lower()+','+ineff.lower()+',0.5).')
        for se in i['damage_relations']['double_damage_to'] :
            sueff = se['name']
            type_list.append(sueff)
            effective_list.append('effective('+type.lower()+','+sueff.lower()+',2).')
        for no in i['damage_relations']['no_damage_to'] :
            noeff = no['name']
            type_list.append(noeff)
            effective_list.append('effective('+type.lower()+','+noeff.lower()+',0).')
        for n in typel :
            if n not in type_list :
                effective_list.append('effective('+type.lower()+','+n.lower()+',1).')
    out = open('../src/pokemon_facts.pl','a')
    for i in t_list :
        out.write(i+'\n')
    for i in effective_list :
        out.write(i+'\n')
    out.close()