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

def doBreadthFirst(NEWMAP, problem, myviewer):
    result = breadth_first(problem, graph_search=True, viewer=myviewer)
    path    = [x[1] for x in result.path()]
    print("Ruta realizada Anchura:")
    print(result.path())
    print(printMap(NEWMAP, problem, path))

def doDepthFirst(NEWMAP, problem, myviewer):
    result = depth_first(problem, graph_search=True, viewer=myviewer)
    path    = [x[1] for x in result.path()]
    # print(result.state)
    # print(result.path())
    print("Ruta realizada Profundidad:")
    print(result.path())
    print(printMap(NEWMAP, problem, path))

def doAStar(NEWMAP, problem, myviewer):
    result = astar(problem, graph_search=True, viewer=myviewer)
    path = [x[1] for x in result.path()]
    print("Ruta realizada A*:")
    print(result.path())
    print(printMap(NEWMAP, problem, path))

def init():

    pacman = input("Posicion del pacman: ")
    pacman = validarPosicion(pacman)

    cereza = input("Posicion de la cereza: ")
    cereza = validarPosicion(cereza)

    NEWMAP = reemplazarPosicionesNoOcupadas(MAP, pacman, cereza)
    NEWMAP = [list(x) for x in NEWMAP.split("\n") if x]
    problem = PacmanProblem(NEWMAP)

    myviewer = WebViewer()
    # myviewer = ConsoleViewer()

    ans=True
    while ans:
        print("""
        1. Busqueda en anchura
        2. Busqueda en profundidad
        3. A*
        4. Exit/Quit
        """)
        ans=raw_input("¿Cual opcion deseea ejecutar? ")
        if ans=="1":
            doBreadthFirst(NEWMAP, problem, myviewer)
        elif ans=="2":
            doDepthFirst(NEWMAP, problem, myviewer)
        elif ans=="3":
            doAStar(NEWMAP, problem, myviewer)
        elif ans=="4":
            ans = None
            exit()
        else:
            print("\n Opcion no valida.")

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