#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 9. Vaise realizar un sorteo no que pode haber un número diferente de gañadores a partir dunhas rifas numeradas entre 0001 e 9999. 

Escribe un script que reciba por teclado o número de premios dispoñibles e imprima os números premiados co formato de 4 díxitos.

Para obter un número número ao azar utiliza o seguinte código:

import random

...

numero_aleatorio = random.randint(1, 9999)
"""

__author__ = "Brais Pose Nieto"

def ignorar_repetidos(premiados: list[int], premio: int) -> bool:
        
    if premio not in premiados:
        
        premiados.append(premio)
        return True
    return False


import random

num_premios = int(input("Numero de premios -> "))

contador = 0

premiados = []


while contador < num_premios:
    numero_aleatorio = random.randint(1, 9999)
    if ignorar_repetidos(premiados,numero_aleatorio) == True:
        contador += 1

    
for premio in premiados:
    print(f"Premiados = {premio:04d}")

