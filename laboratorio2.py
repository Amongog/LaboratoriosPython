#!/usr/bin/python3
# ---------------------------------------------------------------------
#             IE-0117 Programación Bajo Plataformas Abiertas
#         Autor: Samuel Berrocal Soto. samuel.berrocal@ucr.ac.cr
# ---------------------------------------------------------------------
# Este script registra nombres y apellidos que ingresa el usuario.
# Además, rechaza carácteres numéricos o especiales.
# ---------------------------------------------------------------------

# Se debe inicializar la lista de contactos.
contact_list = []
while True:
    string = input('\nIngrese Nombre(s) y Apellidos o digite (SALIR) para salir: ')
    # Verifica si el usuario desea salir e imprimir la lista.
    if(string == 'Salir' or string == 'SALIR' or string == 'salir'):
        print('\n------------------------------')
        print('Lista de Contactos registrada:')
        print('------------------------------')
        for i in range(len(contact_list)):
            print('• '+contact_list[i])
        print('\n\n************ FIN *************')
        break
    try:
        # Prueba si se tiene una palabra, o palabras y espacios.
        if(any(x.isalpha() for x in string)
            and all(x.isalpha() or x.isspace() for x in string) == True):
            print('.')
        else:
            # Si detecta un símbolo o número, alerta un error.
            raise ValueError
    except ValueError:
        print('\n(!) No utilice números o carácteres especiales, por favor.')
        continue # Se salta el resto de la iteración.

    # Capitaliza cada entrada en la lista que se crea al hacer split.
    # Al finalizar esto, lo une de nuevo en un string.
    cap_string = ' '.join(i.capitalize() for i in string.split(' '))
    # Verifica que el tamaño del string sean 3 o 4 palabras.
    if(len(string.split(' ')) == 3 or len(string.split(' ')) == 4):
        contact_list.append(cap_string)
        print('\n»»»» Registro exitoso ««««')
    else:
        print('\n(!) Utilice un formato correcto (3 o 4 componentes).')
