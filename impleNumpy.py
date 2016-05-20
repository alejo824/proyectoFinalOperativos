#Librerias
import numpy as np
#from StringIO import StringIO
#from scipy import linalg

def sumaVectores(A, B):
    C = np.add(A, B)
    return C

def productoVectorial(A, B):
    C = np.cross(A, B)
    return C

def sumaMatrices(A, B):
    C = np.add(A, B)
    return C

def MultiplicacionMatrices(A, B):
    C = np.multiply(A, B)
    return C