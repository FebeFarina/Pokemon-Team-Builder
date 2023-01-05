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

pokemonResistsAndWeaknesses([], [], []).
pokemonResistsAndWeaknesses(T, R, W) :-
    type(T),
    !,
    findall(X, weak(T, X), W),
    findall(X, resistant(T, X), R),
    !.
pokemonResistsAndWeaknesses(P, R, W) :-
  pokemon(P),
  !,
  have_type(P, T),
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
  !,
  T = [F|B],
  pokemonResistsAndWeaknesses(F, PR, PW),
  teamResistsAndWeaknesses(B, TR, TW),
  append(PR, TR, R),
  append(PW, TW, W).

checkTypeSuggestions([], _).
checkTypeSuggestions(T, S) :-
  team(T),
  !,
  T = [F|B],
  not(have_type(F, S)),
  checkTypeSuggestions(B, S).

teamTypeSuggestions(T, S) :-
  teamResistsAndWeaknesses(T, _, W),
  member(X, W),
  findall(S, resistant(S, X), Suggestions),
  member(S, Suggestions),
  checkTypeSuggestions(T, S).