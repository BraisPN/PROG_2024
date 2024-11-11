#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 5. O cifrado César é un tipo de cifrado de substitución no que unha letra do texto orixinal é substituída por outra letra que é un número fixo de posicións posteriores no alfabeto.

Por exemplo se o desprazamento é 5, a ‘a’ cifrarase coa ‘f’. Débense ignorar os espazos en branco.

Se nun desprazamento rematan as letras, volverase a comezar polo comezo do alfabeto.

Supoñer que todos os nomes están en minúsculas e están compostos só polas seguintes letras: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.

Realiza a implantación deste algoritmo na función cifra_cesar(texto: str, desprazamento: int): str. Recorda que os caracteres diferentes as letras se deben manter. Comproba se o tipo de datos introducidos son válidos, e senón é así lanza unha excepción ValueError.

O propio script debe utilizar ditas función para cifrar un texto introducido polo usuario para mostrar o texto cifrado por pantalla. O usuario tamén indicará por teclado o desprazamento. Ademais recorda capturar a excepción.

"""

__author__ = "Brais Pose Nieto"

def cifra_cesar(texto: str, desprazamento: int) -> str:
    # Verificar que el tipo de datos es correcto
    if not isinstance(texto, str) or not isinstance(desprazamento, int):
        raise ValueError("Datos introducidos no válidos: 'texto' debe ser una cadena y 'desprazamento' un entero.")
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamanho = len(alfabeto)
    
    resultado = ""
    
    for char in texto:
        # Si el carácter está en el alfabeto, lo ciframos
        if char in alfabeto:
            # Encuentra el índice de la letra y aplica el desplazamiento
            indice_original = alfabeto.index(char)
            indice_cifrado = (indice_original + desprazamento) % tamanho
            resultado += alfabeto[indice_cifrado]
        else:
            # Mantener caracteres que no están en el alfabeto
            resultado += char
    
    return resultado

# Captura de datos del usuario y manejo de excepciones
try:
    texto_usuario = input("Introduce el texto a cifrar: ")
    desprazamento_usuario = int(input("Introduce el desprazamento: "))
    
    texto_cifrado = cifra_cesar(texto_usuario, desprazamento_usuario)
    print("Texto cifrado:", texto_cifrado)

except ValueError as e:
    print("Error:", e)
