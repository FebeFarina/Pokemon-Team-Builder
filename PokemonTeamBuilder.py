import matplotlib
matplotlib.use("Agg")

from pyswip import Prolog
import sys
import os
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Pokemon Team Builder")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

prolog = Prolog()
prolog.consult("src/pokemon_rules.pl")
team = []
team_weaknesses = []
team_resistances = []
while len(team) < 6:
    pokemon = input("Enter a pokemon: ")
    if pokemon == "quit":
        break
    team.append(pokemon)
print("Your team is: {}.".format(team))
text = ', '.join(team)
text = f"[{text}]"
for matchup in prolog.query("teamResistsAndWeaknesses("+text+",R,W)"):
    team_weaknesses.append(matchup['W'])
    team_resistances.append(matchup['R'])
full_team_weak_list = [item for sublist in team_weaknesses for item in sublist]
full_team_resist_list = [item for sublist in team_resistances for item in sublist]
full_team_weak_list = list(dict.fromkeys(full_team_weak_list))
full_team_resist_list = list(dict.fromkeys(full_team_resist_list))
for types in full_team_weak_list:
    if types in full_team_resist_list:
        full_team_weak_list.remove(types)
        full_team_resist_list.remove(types)
print("Your team is weak against: {}.".format(full_team_weak_list))
print("Your team is resistant against: {}.".format(full_team_resist_list))


