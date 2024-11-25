#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 4. Realiza unha aplicación co seguinte menú:

a) Ingresar datos alumno

b) Eliminar datos alumno

Débese mostrar unha lista de alumnos nun menú e seleccionar o alumno a eliminar segundo o índice co seguinte formato: indice. apelidos_alumno, nome: nota.
c) Modificar nota alumno

Débese mostrar unha lista de alumnos nun menú e seleccionar o alumno a modificar a nota o índice co seguinte formato: indice. apelidos_alumno, nome: nota.
d) Ver nomes e apelidos de alumnos aprobados

Débese mostrar co seguinte formato: indice. apelidos_alumno, nome: nota
e) Mostra alumnos alfabeticamente:

Débese mostrar co seguinte formato: indice. apelidos_alumno, nome: nota
Podes adaptar o algoritmo de ordenación da tarefa anterior.
f) Ver a nota media.

g) Sair.

Para cada alumno necesitaremos gardar os seguintes datos:

Nome
Apelidos
Nota con decimais.
Axuda:

A información de cada alumno almacenarase nun dicionario.
Para gardar a información de cada alumno utilizaremos unha lista.
"""

__author__ = "Brais Pose Nieto"

lista = []

def ingresar_datos(nome, apelidos, nota, lista, alumno):
    if not type(nome) == str:
        raise ValueError
    elif not type(apelidos) == str:
        raise ValueError
    elif not type(nota) == float:
        raise ValueError
    alumno = {"nome" : nome, "apelidos" : apelidos, "nota" : nota}
    lista.append(alumno)







print("a) Ingresar datos alumno")
opcion = input("-> ")

if opcion == "a":
    nome = str(input("Nome: "))
    apelidos = str(input("Apelidos: "))
    nota = float(input("Nota: "))





