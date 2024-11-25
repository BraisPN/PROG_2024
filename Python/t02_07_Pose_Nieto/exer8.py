#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 8. Crea un script que pida as notas dun exame dos alumnos dunha clase para procesalos. 
Tódalas notas téñense que ir almacenando nunha lista. 
Mostra un menú que se mostre continuamente ata que o usuario seleccione a opción saír.
"""

__author__ = "Brais Pose Nieto"

def engadir_nota(lista: list[float], nota: float):

    if not type(lista) == list:
        raise ValueError
    if not type(nota) == float or nota < 0 or nota > 10:
        raise ValueError
    lista.append(nota)

def mostrar_notas(lista: list[float]):

    if not type(lista) == list:
        raise ValueError
    for indice, valor in enumerate(lista):
        print(f"{indice} : {valor}")

def media_notas(lista: list[float]) -> float:

    if not type(lista) == list:
        raise ValueError
    if len(lista) == 0:
        return 0.0
    return sum(lista) / len(lista)

def numero_aprobados(lista: list[float]) -> int:

    if not type(lista) == list:
        raise ValueError
    contador = 0
    for nota in lista:
        if nota >= 5:
            contador += 1
    return contador

def maxima_nota(lista: list[float]) -> float:

    if not type(lista) == list:
        raise ValueError
    if len(lista) == 0:
        return None
    return lista

def eliminar_nota(lista: list[float], indice: int):

    if not type(lista) == list:
        raise ValueError
    if not 0 <= indice < len(lista):
        raise ValueError
    del lista[indice]


lista = []

while True:
    print("a) Engadir nota")
    print("b) Ver media")
    print("c) Ver número de aprobados")
    print("d) Ver máxima nota")
    print("e) Eliminar nota")
    print("f) Saír")

    select = input("-> ")

    if select == "a":

        nota = float(input("Introduce a nota (0-10): "))
        engadir_nota(lista, nota)
        print("Nota engadida correctamente.")
  
    elif select == "b":

        media = media_notas(lista)
        print(f"A media das notas é: {media:.2f}")

    elif select == "c":

        aprobados = numero_aprobados(lista)
        print(f"Número de aprobados: {aprobados}")

    elif select == "d":

        max = maxima_nota(lista)
        if max is None:
            print("Non hai notas na lista.")
        else:
            print(f"A máxima nota é: {max}")

    elif select == "e":

        mostrar_notas(lista)
        indice = int(input("Introduce o índice da nota a eliminar: "))
        eliminar_nota(lista, indice)
        print("Nota eliminada correctamente.")

    elif select == "f":
        print("Saíndo do programa...")
        break
    else:
        print("Opción non válida, volve a tentar.")