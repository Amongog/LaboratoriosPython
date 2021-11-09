#!/usr/bin/python3
# -----------------------------------------------------------------------------
#               IE-0117 Programación Bajo Plataformas Abiertas
#           Autor: Samuel Berrocal Soto. samuel.berrocal@ucr.ac.cr
# -----------------------------------------------------------------------------
# Este script ejecuta una función recursiva para la Secuencia de Fibonacci,
# y recibe el índice y opciones mediante argparser.
#   n       --> valor para calcular el n-ésimo número de la secuencia.
#   -c      --> opció para mostrar la secuencia completa.
#   -t      --> opción para mostrar el tiempo de ejecución del script.
# -----------------------------------------------------------------------------
import argparse
import time


# Se comienza a medir el tiempo de ejecución del script.
tiempo_inicio = time.time()


# Secuencia de Fibonacci por método de recursividad.
def fibonacci(n):
    if(n <= 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Función para verificar el tipo de valor de N: entero y positivo.
def check_positive(n):
    n0 = int(n)
    if n0 < 0:
        raise argparse.ArgumentTypeError(
            '\n\'{}\' no es entero y positivo.'.format(n))
    return n0


# Se declara el objeto ArgumentParser.
parser = argparse.ArgumentParser(
    'Calula el N-ésimo número de la secuencia de Fibonacci.'
    )

parser.add_argument(
    'n',
    type=check_positive,        # N debe ser entero y positivo.
    help='N-ésimo valor deseado de la secuencia.'
)
parser.add_argument(
    '--tiempo',
    '-t',
    action="store_true",
    help='Imprime el tiempo total de ejecución del programa.'
)
parser.add_argument(
    '--completa',
    '-c',
    action="store_true",
    help='Calula la secuencia de Fibonacci hasta el N-ésimo valor.'
)
# Se obtiene los argumentos y se guarda en la variable args.
args = parser.parse_args()

# Se ingresan los argumentos a la función recursiva.
# fibonacci(args.n)

if(args.n == 0):
    if(args.completa and args.tiempo):
        print(
            'La secuencia de Fibonacci hasta el índice {} es:'.format(args.n)
        )
        # Imprime el resultado de cada recursión.
        for i in range(args.n+1):
            print(fibonacci(i))
        print(
            'Tiempo total de ejecución:',
            time.time()-tiempo_inicio,
            'segundos.'
        )

    elif(args.completa):
        print(
            'La secuencia de Fibonacci hasta el índice {} es:'.format(args.n)
        )
        for i in range(args.n+1):
            print(fibonacci(i))
    elif(args.tiempo):
        print('El número de Fibonacci para el ídice {} es:'.format(args.n))
        # Imprime el resultado sólo para el índice deseado.
        print(fibonacci(args.n))
        print(
            'Tiempo total de ejecución:',
            time.time()-tiempo_inicio,
            'segundos.'
        )
    else:
        print('El número de Fibonacci para el ídice {} es:'.format(args.n))
        print(fibonacci(args.n))
elif(args.n == 1):
    if(args.completa and args.tiempo):
        print(
            'La secuencia de Fibonacci hasta el índice {} es:'.format(args.n)
        )
        for i in range(args.n+1):
            print(fibonacci(i))
        print(
            'Tiempo total de ejecución:',
            time.time()-tiempo_inicio,
            'segundos.'
        )
    elif(args.completa):
        print(
            'La secuencia de Fibonacci hasta el índice {} es:'.format(args.n)
        )
        for i in range(args.n+1):
            print(fibonacci(i))
    elif(args.tiempo):
        print('El número de Fibonacci para el ídice {} es:'.format(args.n))
        print(fibonacci(args.n))
        print(
            'Tiempo total de ejecución:',
            time.time()-tiempo_inicio,
            'segundos.'
        )
    else:
        print('El número de Fibonacci para el ídice {} es:'.format(args.n))
        print(fibonacci(args.n))
else:
    if(args.completa and args.tiempo):
        print(
            'La secuencia de Fibonacci hasta el índice {} es:'.format(args.n)
        )
        for i in range(args.n+1):
            print(fibonacci(i))
        print(
            'Tiempo total de ejecución:',
            time.time()-tiempo_inicio,
            'segundos.'
        )
    elif(args.completa):
        print(
            'La secuencia de Fibonacci hasta el índice {} es:'.format(args.n)
        )
        for i in range(args.n+1):
            print(fibonacci(i))
    elif(args.tiempo):
        print('El número de Fibonacci para el ídice {} es:'.format(args.n))
        print(fibonacci(args.n))
        print(
            'Tiempo total de ejecución:',
            time.time()-tiempo_inicio,
            'segundos.'
        )
    else:
        print('El número de Fibonacci para el ídice {} es:'.format(args.n))
        print(fibonacci(args.n))
