
# Pokémon Team Builder

Una herramienta desarrolada en Prolog y Python para analizar las debilidades y resistencias de un equipo Pokémon.


## Documentación

[Informe Práctica 4 - Inteligencia Artificial](https://github.com/FebeFarina/Pokemon-Team-Builder/blob/main/doc/Informe_P04.pdf)


## Instalaciones

El proyecto requiere de PySwip, tkinter y customtkinter para funcionar. Para ello, será necesario instalar ciertas dependencias:

### PySwip
1) Install SWI-Prolog:
    ```
    sudo apt install swi-prolog
    ```
    If you don't want the X bindings, just use the `swi-prolog-nox` package.

2) Install and activate a virtual environment as described before.

3) Install pyswip from Python package index using:
    ```
    pip install pyswip
    ```

4) Run a quick test by running following code at your Python console:
    ```python
    from pyswip import Prolog
    prolog = Prolog()
    prolog.assertz("father(michael,john)")
    ```

## tkinter y customtkinter
    pip install tkinter
    pip install customtkinter

    
## Ejecución del programa

Deberá de ejecutar el script **PokemonTeamBuilder.py** de la siguiente forma:
````
python3 PokemonTeamBuilder.py
````
Se abrirá una ventana con la herramienta de constructor de equipos. Para añadir un Pokémon, introduzca su nombre
en el input y pulse el botón *Add Pokémon*. Para eliminar la última entrada introducida, solo hace falta pulsar *Remove Pokémon*
