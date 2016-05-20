# -*- coding: utf-8 -*-
#Librerias
import os, shutil
import numpy as np
import procesar


def main():
    tipo = int(input("Seleccione una operacón basica.\n\n1.Suma de vectores\n"
    + "2.Producto vectorial\n3.Producto punto\n4.Producto de un vector por una matriz\n"
    + "\n5.Suma de matrices\n6.Producto de matrices\n"
    + "7.Producto de una matriz por un escalar\n"
    + "8.Matriz transpuesta\n"))
    if(tipo < 1 or tipo > 8):
        print("Opcción no valida")
    else:
        if(tipo == 1):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite el tamaño del vector:"))
            filasn = filas
            generarMatriz("SumaVectores", numero, filas,filasn, 2)
        if(tipo == 2):
            numero = int(input("Digite numero de archivos:"))


            generarMatriz("ProductoVectorial", numero, 3,3, 2)
        if(tipo == 3):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite el tamaño del vector:"))
            filasn = filas
            generarMatriz("ProductoPunto", numero, filas,filasn, 1)
        if(tipo == 4):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite numero de filas:"))
            filasn = filas
            columnas = int(input("Digite numero de columnas:"))
            generarMatriz("ProductoVectorMatriz", numero, filas,filasn, columnas + 1)
        if(tipo == 5):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite numero de filas:"))
            filasn = filas
            columnas = int(input("Digite numero de columnas:"))
            generarMatriz("SumaMatrices", numero, filas * 2,filasn, columnas)
        if(tipo == 6):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite numero de filas:"))
            filasn = filas
            columnas = int(input("Digite numero de columnas:"))
            generarMatriz("ProductoMatrices", numero, filas * 2,filasn, columnas)
        if(tipo == 7):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite numero de filas:"))
            filasn = filas
            columnas = int(input("Digite numero de columnas:"))
            generarMatriz("ProductoMatrizEscalar", numero, filas,filasn, columnas)
        if(tipo == 8):
            numero = int(input("Digite numero de archivos:"))
            filas = int(input("Digite numero de filas:"))
            filasn= filas
            columnas = int(input("Digite numero de columnas:"))
            generarMatriz("MatrizT", numero, filas,filasn, columnas)



def generarMatriz(tipo, numero, filas, filasn, columnas):

    if(os.path.exists(tipo)):
        shutil.rmtree(tipo, ignore_errors=False, onerror=None)
        os.mkdir(tipo)
    else:
        os.mkdir(tipo)

    for i in range(1, numero + 1):
        matriz = np.random.randint(100, size=(filas, columnas))
        np.savetxt(tipo + '/' + tipo + '-' + str(filasn) + '-' + str(columnas)
        + '-' + str(i) + '.txt', matriz, fmt='%1.0f')

    procesar.datos(tipo, numero, filas, filasn, columnas)


#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
