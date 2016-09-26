import ia 
from random import *
import random

def cria_tabuleiro(n):
    tabuleiro = {}
    random.seed()
	# preenchendo o tabuleiro
    tabuleiro["pecas"] = [[0 for j in range(n)] for i in range(n)]
    tabuleiro["posicao"] = []
    for i in range(n):
        x = randint(0,n-1)
        if not [x,i] in tabuleiro["posicao"]:
            tabuleiro["pecas"][x][i] = 1
            tabuleiro["posicao"].append([x,i])
        else:
            while [x,i] in tabuleiro["posicao"]:
                x = randint(0,n-1)
                tabuleiro["pecas"][x][i] = 1
                tabuleiro["posicao"].append([x,i])
                
    return tabuleiro



def main():
    t = cria_tabuleiro(4) 
    print t["pecas"]
main() 