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

def ingresar_datos(nome:str, apelidos:str, nota:float, lista:list):
    if not type(nome) == str:
        raise ValueError
    elif not type(apelidos) == str:
        raise ValueError
    elif not type(nota) == float:
        raise ValueError
    if nota < 0 or nota > 10:
        raise ValueError
    alumno = {"nome" : nome, "apelidos" : apelidos, "nota" : nota}
    lista.append(alumno)

def eliminar_alumno(eliminar:str ,lista:list):
    if not type(eliminar) == str:
        raise ValueError
    for i, alumno in enumerate(lista):
        if alumno["nome"] == eliminar:
            del lista[i]

def modificar_datos(modificar:str, lista:list, nova_nota:float):
    if not type(modificar) == str:
        raise ValueError
    if not type(nova_nota) == float:
        raise ValueError
    for alumno in lista:
        if alumno["nome"] == modificar:
            alumno["nota"] = nova_nota

def ver_aprobados(lista:list):
    aprobados = []
    for alumno in lista:
        if alumno["nota"] >= 5:
            aprobado = alumno["nome"] + " " + alumno["apelidos"]
            aprobados.append(aprobado)
    
    return aprobados

while True:
    print("a) Ingresar datos alumno")
    print("b) Eliminar datos alumno")
    print("c) Modificar nota alumno")
    print("d) Ver nomes e apelidos de alumnos aprobados")
    print("g) Sair")
    opcion = input("-> ")
    if opcion == "a":
        nome = str(input("Nome: "))
        apelidos = str(input("Apelidos: "))
        nota = float(input("Nota: "))
        ingresar_datos(nome, apelidos, nota, lista)

    elif opcion == "b":
        print("Alumnos:")
        for i, alumno in enumerate(lista):
            print(alumno["nome"], alumno["apelidos"], alumno["nota"])
        eliminar = str(input("Alumno a eliminar: "))
        eliminar_alumno(eliminar, lista)
    
    elif opcion == "c":
        print("Alumnos:")
        for i, alumno in enumerate(lista):
            print(alumno["nome"], alumno["apelidos"], alumno["nota"])
        modificar = str(input("Alumno a modificar: "))
        nova_nota = float(input("Nova nota: "))
        modificar_datos(modificar, lista, nova_nota)

    elif opcion == "d":
        aprobados = ver_aprobados(lista)
        for aprobado in aprobados:
            print(aprobado)

    elif opcion == "g":
        print("Saindo do programa...")
        break


