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

def calcular_letra_dni(numero):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[numero % 23]

def comprobar_dni(dni):
    # Comprobar longitud
    if not len(dni) == 9:
        return "Inválido"

    # Comprobar formato usando valores ASCII
    for i in range(8):
        if ord(dni[i]) < 48 or ord(dni[i]) > 57:  # ASCII de '0' es 48 y de '9' es 57
            return "Inválido"
    
    if ord(dni[8]) < 65 or ord(dni[8]) > 90:  # ASCII de 'A' es 65 y de 'Z' es 90
        return "Inválido"

    # Comprobar letra de control
    numero = int(dni[:8])
    letra = dni[8]
    letra_correcta = calcular_letra_dni(numero)

    if not letra == letra_correcta:
        return "Inválido"

    return "Válido"

# Solicitar DNI al usuario
dni = input("Introduce tu DNI: ")
resultado = comprobar_dni(dni)
print(resultado)
