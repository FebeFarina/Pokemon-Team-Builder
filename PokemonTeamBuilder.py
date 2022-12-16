from pyswip import Prolog

prolog = Prolog()
prolog.consult("src/pokemon_rules.pl")
team = []
while len(team) < 6:
    weak_list = []
    pokemon = input("Enter a pokemon: ")
    if pokemon == "quit":
        break
    team.append(pokemon)
    for weakness in prolog.query("weak_against("+pokemon+",X)"):
        if weakness['X'] not in weak_list:
            weak_list.append(weakness['X'])
    print("{} is weak against: {}.".format(pokemon, weak_list))
print("Your team is: {}.".format(team))