:- include("pokemon_facts.pl").

/* Tipos de efectividad */

super_effective(T1, T2):-
    effective(T1, T2, 2).

not_very_effective(T1, T2):-
    effective(T1, T2, 0.5).

no_effect(T1, T2):-
    effective(T1, T2, 0).

resistant(T1, T2):-
    not_very_effective(T2, T1).

weak(T1, T2):-
    super_effective(T2, T1).

/* Búsqueda de debilidades y fuerzas */

weak_against(P, X):-
    pokemon(P),
    have_type(P, T),
    weak(T, X).

strong_against(P, X):-
    pokemon(P),
    have_type(P, T),
    super_effective(T, X).

cWR(R, W, L):-
    type(R),
    \+ member(R, W),
    append([], [R], L).
cWR(_R, _W, []).

cancelWeaknessResists([], _W, []).
cancelWeaknessResists([R|TR], W, L) :-
  is_list(TR),
  is_list(W),
  cancelWeaknessResists(TR, W, TailL),
  cWR(R, W, WRList),
  append(WRList, TailL, L).

pokemonResistsAndWeaknesses([], [], []).
pokemonResistsAndWeaknesses(T, R, W) :-
    type(T),
    findall(X, weak(T, X), W),
    findall(X, resistant(T, X), R),
    cancelWeaknessResists(R, W, L).
pokemonResistsAndWeaknesses(P, R, W) :-
  pokemon(P),
  have_type(P, T),
  !,
  pokemonResistsAndWeaknesses(T, R, W).

/* Reglas de equipos */

team([]).
team([P|TP]):-
    is_list(TP),
    pokemon(P),
    team(TP).

teamResistsAndWeaknesses([], [], []).
teamResistsAndWeaknesses(T, R, W) :-
  team(T),
  T = [F|B],
  pokemonResistsAndWeaknesses(F, PR, PW),
  teamResistsAndWeaknesses(B, TR, TW),
  append(PR, TR, R),
  append(PW, TW, W).

teamTypeCovered(T) :-
  teamResistsAndWeaknesses(T, R, _W),
  member(normal, R),
  member(fire, R),
  member(water, R),
  member(electric, R),
  member(grass, R),
  member(ice, R),
  member(fighting, R),
  member(poison, R),
  member(ground, R),
  member(flying, R),
  member(psychic, R),
  member(bug, R),
  member(rock, R),
  member(ghost, R),
  member(dragon, R),
  member(dark, R),
  member(steel, R),
  member(fairy, R).