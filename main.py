from registro import *

import os.path

import pickle


def validar_n(titulo='Ingrese un valor: '):
    n = int(input(titulo))
    while n < 0:
        n = int(input('Ingrese un valor adecuado: '))
    return n


def validar_con_rango(li, ls, titulo='Ingrese una opcion: '):
    n = int(input(titulo))
    while li > n > ls:
        n = int(input('Ingrese una opcion que se pueda: '))
    return n


def add_in_order(vec, reg):
    n = len(vec)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if vec[c].identificacion == reg.identificacion:
            pos = c
            break
        if reg.identificacion < vec[c].identificacion:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def busqueda_binaria(vec, num):
    n = len(vec)
    pos = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].identificacion == num:
            pos = c
            break
        if num < vec[c].identificacion:
            der = c - 1
        else:
            izq = c + 1

    return pos


def cargar_vector(n, vec):
    for i in range(n):
        add_in_order(vec, generar_articulo())


def mostrar_vector(vec, l):
    for i in vec:
        if i.origen != l:
            print(to_string(i))


def generar_archivo(vec, tip, x_nombre):
    if os.path.exists(x_nombre):
        print('Eses nombre ya existe...')
        return
    archivo = open(x_nombre, 'wb')
    for i in vec:
        if i.tipo != tip:
            pickle.dump(i, archivo)

    archivo.close()


def mostrar_archivo(x_nombre):
    total = 0
    sumador = 0
    if not os.path.exists(x_nombre):
        print('Ese archivo no existe...')
        return

    archivo = open(x_nombre, 'rb')
    size = os.path.getsize(x_nombre)
    while archivo.tell() < size:
        reg = pickle.load(archivo)
        total += 1
        sumador += reg.precio
        print(to_string(reg))
    print(f'El total de articulos: {total}\n'
          f'Y el promedio de precios es: {sumador // total}')
    archivo.close()


def generar_matriz(vec):
    mat = [[0]*30 for i in range(25)]

    for i in vec:
        fila = i.origen
        columna = i.tipo

        mat[fila][columna] += i.precio
    return mat


def mostrar_matriz(mat):
    for i in range(len(mat)):
        if 4 <= i <= 15:
            for j in range(len(mat[i])):
                if 2 <= j <= 10:
                    if mat[i][j] > 0:
                        print(f'El articulo de origen: {i} y de tipo {j}, vendio: {mat[i][j]}')


def principal():
    opciones = '1- Opcion 1\n' \
               '2- Opcion 2\n' \
               '3- Opcion 3\n' \
               '4- Opcion 4\n' \
               '5- Opcion 5\n' \
               '6- Opcion 6\n' \
               '7- Salir'
    vec = []
    opc = -1
    while opc != 0:
        print(opciones)
        opc = validar_con_rango(1, 7)
        if opc == 1:
            n = validar_n('Ingrese cuantos quiere cargar: ')
            cargar_vector(n, vec)

        if opc == 2:
            i = validar_con_rango(0, 24, 'Ingrese el pais de origen que desea filtrar: ')
            mostrar_vector(vec, i)

        if opc == 3:
            num = validar_n('Ingrese la id del articulo: ')
            indice = busqueda_binaria(vec, num)
            if indice != -1:
                print(to_string(vec[indice]))
            else:
                print('Ese articulo no existe...')

        if opc == 4:
            x_nombre = input('Ingrese el nombre: ')
            tip = validar_con_rango(0, 29, 'Ingrese el tipo que quiere filtrar: ')
            generar_archivo(vec, tip, x_nombre)

        if opc == 5:
            x_nombre = input('Ingrese el nombre: ')
            mostrar_archivo(x_nombre)

        if opc == 6:
            mat = generar_matriz(vec)
            mostrar_matriz(mat)




if __name__ == '__main__':
    principal()


