:- include("pokemon_facts.pl").

/* Tipos de efectividad */

super_effective(T1, T2):-
    effective(T1, T2, 2).

not_very_effective(T1, T2):-
    effective(T1, T2, 0.5).

no_effect(T1, T2):-
    effective(T1, T2, 0).

resistant(T1, T2):-
    not_veryeffective(T2, T1,).

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