#Librerias
import os, shutil
#from time import time
import numpy as np
import impleNumpy as iN
from StringIO import StringIO
#from scipy import linalg


def datos(tipo, numero, filas, filasn, columnas):
    if(tipo == "SumaVectores"):
        if(os.path.exists(tipo+'/SolucionNumpy') and os.path.exists(tipo+'/SolucionThread') and os.path.exists(tipo+'/SolucionMultiProcessing')):
            shutil.rmtree(tipo+'/SolucionNumpy', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionThread', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionMultiProcessing', ignore_errors=False, onerror=None)
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')
        else:
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')

        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-'
            + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            A = data[0:filas, 0]
            B = data[0:filas, 1]
            #tiempoInicioN = time()
            C = iN.sumaVectores(A, B)
           # tiempoFinN = time() - tiempoInicioN

            np.savetxt(tipo + '/' + 'SolucionNumpy' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionThread' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionMultiProcessing' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

    if(tipo == "ProductoVectorial"):

        if(os.path.exists(tipo+'/SolucionNumpy') and os.path.exists(tipo+'/SolucionThread') and os.path.exists(tipo+'/SolucionMultiProcessing')):
            shutil.rmtree(tipo+'/SolucionNumpy', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionThread', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionMultiProcessing', ignore_errors=False, onerror=None)
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')
        else:
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')

        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-'
            + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.array(data)
            #redefino los vectores para poderlos utilizar
            a = data[0:filas, 0]
            b = data[0:filas, 1]
            #vectores con las dimensiones requeridas para el producto vectorial
            A = [a[0], a[1], a[2]]
            B = [b[0], b[1], b[2]]

            #tiempoInicioN = time()
            C = iN.productoVectorial(A, B)
           # tiempoFinN = time() - tiempoInicioN

            np.savetxt(tipo + '/' + 'SolucionNumpy' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionThread' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionMultiProcessing' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

    if(tipo == "ProductoPunto"):
        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-' + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            matriz1 = data[0:filas / 2]
            matriz2 = data[3:filas]
            matriz3 = matriz1 * matriz2
            print ("\n"+matriz3+"\n")

    if(tipo == "ProductoVectorMatriz"):
        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-' + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            matriz1 = data[0:filas / 2]
            matriz2 = data[3:filas]
            matriz3 = matriz1 * matriz2
            print ("\n"+matriz3+"\n")

    if(tipo == "SumaMatrices"):

        if(os.path.exists(tipo+'/SolucionNumpy') and os.path.exists(tipo+'/SolucionThread') and os.path.exists(tipo+'/SolucionMultiProcessing')):
            shutil.rmtree(tipo+'/SolucionNumpy', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionThread', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionMultiProcessing', ignore_errors=False, onerror=None)
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')
        else:
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')

        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-'
            + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            A = data[0:filas / 2]
            B = data[filas / 2:filas]
            #tiempoInicioN = time()
            C = iN.sumaMatrices(A, B)
           # tiempoFinN = time() - tiempoInicioN

            np.savetxt(tipo + '/' + 'SolucionNumpy' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionThread' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionMultiProcessing' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

    if(tipo == "ProductoMatrices"):
        if(os.path.exists(tipo+'/SolucionNumpy') and os.path.exists(tipo+'/SolucionThread') and os.path.exists(tipo+'/SolucionMultiProcessing')):
            shutil.rmtree(tipo+'/SolucionNumpy', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionThread', ignore_errors=False, onerror=None)
            shutil.rmtree(tipo+'/SolucionMultiProcessing', ignore_errors=False, onerror=None)
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')
        else:
            os.mkdir(tipo+'/SolucionNumpy')
            os.mkdir(tipo+'/SolucionThread')
            os.mkdir(tipo+'/SolucionMultiProcessing')

        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-'
            + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            A = data[0:filas / 2]
            B = data[filas / 2:filas]
            #tiempoInicioN = time()
            C = iN.MultiplicacionMatrices(A, B)
           # tiempoFinN = time() - tiempoInicioN

            np.savetxt(tipo + '/' + 'SolucionNumpy' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionThread' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')

            np.savetxt(tipo + '/' + 'SolucionMultiProcessing' + '/' + tipo + '-' + str(filasn)
            + '-' + str(columnas)
            + '-' + str(i) + 'salida-Numpy.txt', C, fmt='%1.0f')









    if(tipo == "ProductoMatrizEscalar"):
        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-' + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            matriz1 = data[0:filas / 2]
            matriz2 = data[3:filas]
            matriz3 = matriz1 * matriz2
            print ("\n"+matriz3+"\n")

    if(tipo == "MatrizT"):
        for i in range(1, numero + 1):
            pfile = open(tipo + '/' + tipo + '-' + str(filasn) + '-' + str(columnas)
            + '-' + str(i) + '.txt', 'r')
            data = pfile.read()
            pfile.close()
            data = np.genfromtxt(StringIO(data))
            data = np.matrix(data)
            matriz1 = data[0:filas / 2]
            matriz2 = data[3:filas]
            matriz3 = matriz1 * matriz2
            print ("\n"+matriz3+"\n")








