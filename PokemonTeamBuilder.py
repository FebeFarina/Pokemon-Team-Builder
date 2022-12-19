import matplotlib
matplotlib.use("Agg")

from pyswip import Prolog
import sys
import os
import customtkinter

def add_pkm():
    if len(team) == 6:
        print("Team is full!")
        return
    pkm = entry.get()
    if pkm == "":
        print("No pokemon entered!")
        return
    if pkm in team:
        print("Pokemon already in team!")
        return
    # if not prolog.assertz("pokemon("+pkm+")"):
    #     print("Pokemon not found!")
    #     return
    team.append(pkm)
    print(team)
    entry.delete(0, "end")
    weak, resist = get_pkm_weakness(pkm)
    print("Weaknesses: {}".format(weak))
    print("Resistances: {}".format(resist))


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

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Pokemon Team Builder")
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pókemon Team Builder", font=("Arial", 20))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter a pokemon", font=("Arial", 12))
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Add Pokemon", font=("Arial", 16), command=add_pkm)
button.pack(pady=12, padx=10)


prolog = Prolog()
prolog.consult("src/pokemon_rules.pl")
team = []
team_weaknesses = []
team_resistances = []

root.mainloop()


