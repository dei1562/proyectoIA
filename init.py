#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import re
from simpleai.search import SearchProblem, astar, breadth_first, depth_first
from simpleai.search.viewers import ConsoleViewer, BaseViewer, WebViewer
from pacmanProblem import PacmanProblem

## Se define la estructura del laberinto
MAP = """
######
#1234#
#56#7#
#8##9#
#ABCD#
######
"""

def validarPosicion(pos):
    pos = str(pos)
    x = re.findall("\d", pos)
    if not x:
        tmpPos = input("La posicion ingresada no es correcta, por favor ingrese otra: ")
        return validarPosicion(tmpPos)

    int_pos = int(pos)
    if int_pos > 13:
        tmpPos = input("La posicion ingresada no esta en la matriz, por favor ingrese otra: ")
        return validarPosicion(tmpPos)

    return pos

def reemplazarPosicionesNoOcupadas(strMap, pacman, cereza):
    
    switcher = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D"
    }

    NEWMAP = strMap.replace(switcher.get(int(pacman), "Posicion invalida"), "o")
    NEWMAP = NEWMAP.replace(switcher.get(int(cereza), "Posicion invalida"), "x")
    NEWMAP = NEWMAP.replace("1", " ")
    NEWMAP = NEWMAP.replace("2", " ")
    NEWMAP = NEWMAP.replace("3", " ")
    NEWMAP = NEWMAP.replace("4", " ")
    NEWMAP = NEWMAP.replace("5", " ")
    NEWMAP = NEWMAP.replace("6", " ")
    NEWMAP = NEWMAP.replace("7", " ")
    NEWMAP = NEWMAP.replace("8", " ")
    NEWMAP = NEWMAP.replace("9", " ")
    NEWMAP = NEWMAP.replace("A", " ")
    NEWMAP = NEWMAP.replace("B", " ")
    NEWMAP = NEWMAP.replace("C", " ")
    NEWMAP = NEWMAP.replace("D", " ")

    return NEWMAP

def printMap(NEWMAP, problem, path): 
    for y in range(len(NEWMAP)):
        for x in range(len(NEWMAP[y])):
            if (x, y) == problem.initial:
                print("o", end='')
            elif (x, y) == problem.goal:
                print("x", end='')
            elif (x, y) in path:
                print("·", end='')
            else:
                print(NEWMAP[y][x], end='')
        print()

def init():
    pacman = input("Posicion del pacman: ")
    pacman = validarPosicion(pacman)

    cereza = input("Posicion de la cereza: ")
    cereza = validarPosicion(cereza)

    NEWMAP = reemplazarPosicionesNoOcupadas(MAP, pacman, cereza)
    NEWMAP = [list(x) for x in NEWMAP.split("\n") if x]
    problem = PacmanProblem(NEWMAP)

    my_viewer = WebViewer()

    # resultb = breadth_first(problem, graph_search=True, viewer=my_viewer)
    # path    = [x[1] for x in resultb.path()]
    # print("Busqueda en Anchura")
    # print(resultb.path())
    # print(printMap(NEWMAP, problem, path))

    resultd = depth_first(problem, graph_search=True, viewer=my_viewer)
    print(resultd.state)
    print(resultd.path())

    # resulta = astar(problem, graph_search=True)
    # path = [x[1] for x in resulta.path()]
    # print("Busqueda A*")
    # print(resulta.path())
    # print(printMap(NEWMAP, problem, path))

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