#!/usr/bin/python3

import sys

while True:
    iterador = input('Defina el número de líneas de altura de la pirámide: ')
    try:
        iterador = int(iterador)
        break
    except ValueError:
        print('\'{}\' no es válido. Introduzca un número válido'.format(iterador))
        continue

# carne = input('Digite su carné: ')
# ultimo_caracter_carne = carne[-1]

while True:
    try:
        carne = input('Digite su carné: ')
        ultimo_caracter_carne = carne[-1]
    except ValueError:
        print('Por favor, intente de nuevo')
        continue

    if(ultimo_caracter_carne in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        break
    else:
        print('\'{}\' no es un carné válido, debe terminar en un número. Ingrese su carné nuevamente: '.format(carne))
        continue

# print('El número final del carné ingresado es {}'.format(ultimo_caracter_carne))
ultimo_numero_carne = int(ultimo_caracter_carne)

if(ultimo_numero_carne % 2) == 0:
    # asd
    for i in range(iterador,0,-1):
        print(carne*i)
        if(i == 0):
            break
        else:
            continue
else:
    for i in range(1,iterador+1):
        print('{}'.format(carne*i))
        i += 1
        if(i == iterador+1):
            break
        else:
            continue
