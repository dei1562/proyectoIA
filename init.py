import re
from simpleai.search import astar
from pacmanProblem import PacmanProblem

def validarPosicion(pos):
    x = re.findall("\d", pos)
    if not x:
        tmpPos = input(f"La posicion ingresada no es correcta, por favor ingrese otra: ")
        return validarPosicion(tmpPos)

    int_pos = int(pos)
    if int_pos > 13:
        tmpPos = input(f"La posicion ingresada no esta en la matriz, por favor ingrese otra: ")
        return validarPosicion(tmpPos)

    return int_pos

def init():
    pacman = input(f"Posicion del pacman: ")
    pacman = validarPosicion(pacman)

    cereza = input(f"Posicion de la cereza: ")
    cereza = validarPosicion(cereza)

    problem = PacmanProblem(initial_state='')
    problem.pacman = pacman
    problem.cereza = cereza

    result = astar(problem)

    print(result.state)
    print(result.path())

print(
'''
Se tiene la siguiente matriz en la cual se deben ubicar el pacman y la cereza que debe alcanzar el pacman,
las posiciones que se debe ingresar estan dadas en la siguiente matriz de ejemplo:

------------------------
|  1 ||  2 ||  3 ||  4 |
------------------------
|  5 ||  6 || XX ||  7 |
------------------------
|  8 || XX || XX ||  9 |
------------------------
| 10 || 11 || 12 || 13 |
------------------------

Las X representan espacios u obstaculos que no se pueden ocupar.
'''
    )
init()