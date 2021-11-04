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
    # Si el string sólo contiene letras, continua, sino, reintentar.
    try:
        if(string.isalpha()):
            break
        else:
            raise ValueError()
    except ValueError:
        print('\n(!) No utilice números o carácteres especiales, por favor.')
        continue

    # Si se ingresa SALIR, o una variación de este, se imprime
    # el registro completo de los contactos y finaliza el script.
    # De otra forma, verifica que el tamaño del strin sea correcto y
    # registra un nuevo contacto.
    if(string == 'Salir' or string == 'SALIR' or string == 'salir'):
        print('\n------------------------------')
        print('Lista de Contactos registrada:')
        print('------------------------------')
        for i in range(len(contact_list)):
            print('• '+contact_list[i])
        print('\n\n************ FIN *************')
        break
    else:
        # Primero divide el string ingresado y capitaliza cada entrada
        # de la lista, para luego unificar la lista en una string.
        cap_string = ' '.join(i.capitalize() for i in string.split(' '))
        if(len(string.split(' ')) == 3 or len(string.split(' ')) == 4):
            contact_list.append(cap_string)
            print('\n»»»» Registro exitoso ««««')
        else:
            print('\n(!) Utilice un formato correcto (3 o 4 componentes).')
