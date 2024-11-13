#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercicio 7. Un número de DNI ten o seguinte formato 00000000A. Escribe un script que lle pida ao usuario o seu DNI e comprobe que sexa correcto. 

Para iso sigue os seguintes pasos: Comproba a lonxitude da cadea. Comproba que os 8 primeiros díxitos son números e o último é unha letra maiúscula. 

PISTA: utiliza a táboa do código ASCII. Comproba que a letra introducida é o código de control do DNI.

https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/#:~:text=Por%20ejemplo%2C%20si%20el%20n%C3%BAmero,n%C3%BAmeros%20y%20d%C3%ADgito%20de%20control. 

Por último imprime Válido ou Inválido segundo corresponda.
"""

__author__ = "Brais Pose Nieto"

def calcular_indice_hash(tam_tabla, num_divisiones, clave):
    suma_partes = 0
    longitud_clave = len(clave)
    
    i = 0
    while i < longitud_clave:
        parte = clave[i:i+num_divisiones]
        suma_partes += int(parte)
        i += num_divisiones
    
    # Calcular el índice como el resto de dividir la suma por el tamaño de la tabla
    indice = suma_partes % tam_tabla
    
    return indice

# Solicitar parámetros al usuario
tam_tabla = int(input("Introduce el tamaño de la tabla: "))
num_divisiones = int(input("Introduce el número de divisiones por folding: "))
clave = input("Introduce la clave: ")

# Calcular el índice
indice = calcular_indice_hash(tam_tabla, num_divisiones, clave)
print(f"El índice de la clave es: {indice}")
