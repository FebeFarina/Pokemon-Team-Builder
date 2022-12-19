import matplotlib
matplotlib.use("Agg")

from pyswip import Prolog
import sys
import os
from tkinter import *
from tkinter import ttk

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

prolog = Prolog()
prolog.consult("src/pokemon_rules.pl")
team = []
team_names = ("Pokemon")
team_weaknesses = []
team_resistances = []
while len(team) < 6:
    pokemon = input("Enter a pokemon: ")
    if pokemon == "quit":
        break
    team.append(pokemon)
    team_names.append(pokemon)
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

lst = [(1,'Raj','Mumbai',19), 
(2,'Aaryan','Pune',18), 
(3,'Vaishnavi','Mumbai',20), 
(4,'Rachna','Mumbai',21), 
(5,'Shubham','Delhi',21)]
total_rows = len(lst)
total_columns = len(lst[0])

root = Tk()

root.title("Pokemon Team Builder")
root.geometry("500x500")

set = ttk.Treeview(root)
set.pack()

set['columns']= team_names
set.column("#0", width=0,  stretch=NO)
set.column("id",anchor=CENTER, width=80)
set.column("full_Name",anchor=CENTER, width=80)
set.column("award",anchor=CENTER, width=80)

set.heading("#0",text="",anchor=CENTER)
set.heading("id",text="ID",anchor=CENTER)
set.heading("full_Name",text="Full_Name",anchor=CENTER)
set.heading("award",text="Award",anchor=CENTER)

root.mainloop()


