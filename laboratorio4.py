#!/usr/bin/python3
# -----------------------------------------------------------------------------
#               IE-0117 Programación Bajo Plataformas Abiertas
#           Autor: Samuel Berrocal Soto. samuel.berrocal@ucr.ac.cr
# -----------------------------------------------------------------------------
# Este script crea una clase para generar matrices y poder hacer operaciones
# con estas.
# -----------------------------------------------------------------------------
class Matrix:
    """
    Esta clase permite crear matrices y ejecutar sumas y restas entre estas,
    siempre y cuando las matrices sean de la misma dimensión.
    """
    # Punto 1: Método constructor.
    def __init__(self, n, m, valores_iniciales=0):
        """
        Recibe los valores dimensionales de la matriz, y si no se define
        un valor de inicialización para la matriz, se utiliza 0 por default.
        """
        self.filas = int(n)
        self.columnas = int(m)
        # Inicializa cada espacio dentro de la matriz con el valor deseado.
        self.M = [
            [int(valores_iniciales)] * self.columnas for i in range(self.filas)
        ]

    # Punto 2: Método str.
    def __str__(self):
        """
        '+=' Permite concatenar varias líneas.
        'lamba' permite definir una funcion en la misma línea, esto para
        poder utilizar map() de la forma correcta.
            »» lambda {argumento} = funcion{argumento}
        'map()' funciona de la siguiente forma:
            »» map(funcion a aplicar, objeto sobre el cual aplica la funcion)
        """
        string_matriz = ''  # Inicializa la variable.
        string_matriz += ' -' * self.columnas + '\n'
        for i in range(len(self.M)):
            string_matriz += (
                ''.join(map(lambda x: '{0:2}'.format(x), self.M[i])) + '\n'
                )
        string_matriz += ' -' * self.columnas + '\n'
        return string_matriz

    # Punto 3 (Modificado con Punto 5): Método get (getitem).
    def __getitem__(self, posicion):
        """
        Permite acceder una posición dentro de la matriz.
        'isinstance(elemento, tipo)' revisa si la llave es una tupla.
        """
        if isinstance(posicion, tuple):
            i = posicion[0]     # fila.
            j = posicion[1]     # columna.
        return self.M[i][j]

    # Punto 3 (Modificado con Punto 5): Método set(setitem).
    def __setitem__(self, posicion, value):
        """
        Permite modificar una posición dentro de la matriz.
        """
        if isinstance(posicion, tuple):
            i = posicion[0]
            j = posicion[1]
            self.M[i][j] = value

    def __add__(self, other):
        """
        Crea una matriz inicializada en 0, que albergará el resultado de la
        suma.
        """
        resultado = Matrix(n=self.filas, m=self.columnas, valores_iniciales=0)

        # Si ambos objetos son matrices.
        if isinstance(other, Matrix):
            # Suma cada posición con la de la otra matriz.
            for i in range(self.filas):
                for j in range(self.columnas):
                    resultado.M[i][j] = self.M[i][j] + other.M[i][j]
        return resultado

    def __sub__(self, other):
        """
        Crea una matriz inicializada en 0, que albergará el resultado de la
        resta.
        """
        resultado = Matrix(n=self.filas, m=self.columnas, valores_iniciales=0)

        if isinstance(other, Matrix):
            # Resta cada posición con la de la otra matriz.
            for i in range(self.filas):
                for j in range(self.columnas):
                    resultado.M[i][j] = self.M[i][j] - other.M[i][j]
        return resultado


# Programa para verificar el funcionamiento de la clase.
if __name__ == '__main__':

    print('Ingrese las dimensiones (nxm) de las matrices A y B.')
    print('Nota: ambas deben tener la misma dimensión.')

    # Prueba punto 1.
    while True:
        A = Matrix(
            n=input('Matriz A (n = filas): '),
            m=input('Matriz A (m = columnas): '),
            valores_iniciales=input('Inicializar A con: ')
            )
        B = Matrix(
            n=input('Matriz B (n = filas): '),
            m=input('Matriz B (m = columnas): ')
            )
        try:
            if(A.filas != B.filas):
                raise ValueError
            elif(A.columnas != B.columnas):
                raise ValueError
            else:
                break
        except ValueError:
            print('Las dimensiones no coinciden, intente de nuevo.')

    # Prueba Punto 2.
    print('Prueba Punto 2: Impresión de matriz como string.\n')
    print('Matriz A')
    print(A)
    print('Matriz B (Sin inicializar con otro número)')
    print(B)

    # Prueba Punto 3: Get.
    print('Prueba Punto 3 (Modificado con Punto 5.): get.\n')
    print('El valor en la posición [0,0] es', B[0, 0], '\n')
    # Prueba Punto 3: Set.
    print('Prueba Punto 3 (Modificado con Punto 5.): set.\n')
    print('Cambiando [0,0] por » 666.')
    B[0, 0] = 666
    print('El valor en la posición [0,0] es', B[0, 0], '\n')
    print('La matriz completa B ahora se ve así:')
    print(B)

    # Prueba Punto 4: Suma.
    print('Prueba Punto 4: Suma.\n')
    print('Sumando ambas matrices..')
    resultado = A + B
    print(resultado)

    # Prueba Punto 4: Resta.
    print('Prueba Punto 4: Resta.\n')
    print('Restando ambas matrices..')
    resultado = A - B
    print(resultado)
