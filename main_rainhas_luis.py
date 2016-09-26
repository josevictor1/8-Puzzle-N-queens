import ia
import random


def cria_tabuleiro():
    """
    Cria um tabuleiro totalmente alatorio com n rainhas
    @return: um tabuleiro de xadrez com n rainhas
    """

    tabuleiro = {}
    # criando o tabuleiro
    tabuleiro["pecas"] = [[0 for j in range(8)] for i in range(8)]
    tabuleiro["rainhas"] = []
    tabuleiro["conflitos"] = 0

    for i in range(8):
        tabuleiro["pecas"][i][i] = i+1 # inserindo as rainhas na diagonal
        tabuleiro["rainhas"].append(i) # salvando as posicoes das rainhas

    return tabuleiro


def embaralha(tabuleiro):
    """
    Embaralha as rainhas no tabuleiro
    @param tabuleiro: tabuleiro
    """
    random.shuffle(tabuleiro["rainhas"])
    rainhas = [None for i in tabuleiro["rainhas"]]

    for i in range(len(tabuleiro["rainhas"])):
        rainhas[tabuleiro["rainhas"][i]] = tabuleiro["pecas"][i]

    tabuleiro["pecas"] = rainhas

def heuristica(l):
     h = len(l)
     soma = 0
     for i in range(h):
        for j in range(h):
            if i != j and (l[i] - i == l[j] - j or l[i] + i == l[j] + j):
                soma = soma + 1 
                print "primeira", l[i],i
                print "segunda", l[j],j
     return soma


def main():
    tabuleiro = cria_tabuleiro()
    
    embaralha(tabuleiro)
    for linha in tabuleiro["pecas"]: print linha
    print tabuleiro["rainhas"]

    return 0

main()