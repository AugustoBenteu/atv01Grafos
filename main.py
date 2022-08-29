import sys
import numpy as np
from os.path import exists

def salvaResultado(res):
    if (exists('resultado.txt') == False):
        r = open('resultado.txt','x')
        r.write(res + '\n')
    else:
        r = open('resultado.txt','a')
        r.write(res  + '\n')


def leMatriz(nome):
    mat = np.matrix = np.loadtxt(nome)
    res =  nome + ' ' + str(mat.shape[0]) + ' ' + 'linhas' + ' ' + str(mat.shape[1]) + ' ' + 'colunas'
    print(res)
    salvaResultado(res)
    

def main(file):
    leMatriz(file)

if __name__ == '__main__':
    main(str(sys.argv[1]))
    

