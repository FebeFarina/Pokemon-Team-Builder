import matplotlib
matplotlib.use("Agg")

from pyswip import Prolog
import sys
import os
import tkinter as tk
from tkinter import ttk
import customtkinter


prolog = Prolog()
prolog.consult("src/pokemon_rules.pl")
team_info = []
team_pkm = []

def check_weaknesses():
    general_weakness = []
    if len(team_info) == 0:
        return "Team is empty!"
    text = ', '.join(team_pkm)
    text = f"[{text}]"
    for matchup in prolog.query("teamTypeCovered("+text+",X)"):
        general_weakness.append(matchup['X'])
    general_weakness_dict = list(dict.fromkeys(general_weakness))
    text2.set("Your team is weak of the following types: "+str(general_weakness_dict))
    
def add_pkm():
    if len(team_info) == 6:
        print("Team is full!")
        return
    pkm = entry.get()
    if pkm == "":
        print("No pokemon entered!")
        return
    entry.delete(0, "end")
    weak, resist = get_pkm_weakness(pkm)
    team_info.append([pkm, weak, resist])
    team_pkm.append(pkm)
    check_weaknesses()
    refresh_data()

def get_pkm_weakness(pokemon):
    weak = []
    resist = []
    for matchup in prolog.query("pokemonResistsAndWeaknesses("+pokemon+",R,W)"):
        weak.append(matchup['W'])
        resist.append(matchup['R'])
    weak = [item for sublist in weak for item in sublist]
    resist = [item for sublist in resist for item in sublist]
    weak = list(dict.fromkeys(weak))
    resist = list(dict.fromkeys(resist))
    for types in weak:
        if types in resist:
            weak.remove(types)
            resist.remove(types)
    return weak, resist

def load_data():
    for row in team_info:
        t1.insert("", "end", values=row)

def refresh_data():
    t1.delete(*t1.get_children())
    load_data()

def remove_pkm():
    if len(team_info) == 0:
        print("Team is empty!")
        return
    team_info.pop()
    team_pkm.pop()
    check_weaknesses()
    refresh_data()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Pokemon Team Builder")
root.geometry("500x350")

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, expand=True)

label = customtkinter.CTkLabel(master=frame1, text="Pókemon Team Builder", font=("Roboto", 20))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter a pokemon", font=("Roboto", 12))
entry.pack(pady=12, padx=10)

text2 = tk.StringVar()
label2 = customtkinter.CTkLabel(master=frame1, textvariable=text2, font=("Roboto", 12))
text2.set("Your team is empty!")
label2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame1, text="Add Pokemon", font=("Roboto", 16), command=add_pkm)
button2 = customtkinter.CTkButton(master=frame1, text="Remove Pokemon", font=("Roboto", 16), command=remove_pkm)
button.pack(pady=12, padx=10, side="left")
button2.pack(pady=12, padx=10, side="right")

frame2 = customtkinter.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

t1 = ttk.Treeview(frame2)
column_list_accout = ["Pokemon", "Weaknesses", "Resistances"]
t1["columns"] = column_list_accout
t1["show"] = "headings"
for column in column_list_accout:
    t1.heading(column, text=column)
    t1.column(column, width=50)
t1.place(relheight=1, relwidth=1)
treescroll = ttk.Scrollbar(frame2, orient="vertical", command=t1.yview)
treescroll.configure(command=t1.yview)
t1.configure(yscrollcommand=treescroll.set)
treescroll.pack(side="right", fill="y")

root.mainloop()


