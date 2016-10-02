import ia
import random
import copy
import math
import time
import numpy as np

euler = math.exp(1)

def cria_tabuleiro(pecas,rainhas):
    """
    Cria um tabuleiro totalmente alatorio com n rainhas
    @return: um tabuleiro de xadrez com n rainhas
    """

    tabuleiro = {}
    # criando o tabuleiro
    tabuleiro["pecas"] = []
    tabuleiro["pecas"] = pecas
    tabuleiro["rainhas"] = rainhas
    tabuleiro["conflitos"] = 0
    tabuleiro["filhos"] = []

     # salvando as posicoes das rainhas

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
    soma = 0
    h = len(l)
    for i in range(h):
        for j in range(h):
            if i != j and (l[i] - i == l[j] - j or l[i] + i == l[j] + j):

                soma = soma + 1

    return soma




def expande(tabuleiro):

    for i in range(len(tabuleiro["rainhas"]) - 1):
        for j in range(i + 1,len(tabuleiro["rainhas"])):

                t = cria_tabuleiro([],[])
                t["rainhas"] = tabuleiro["rainhas"][:]
                aux = t["rainhas"][i]
                t["rainhas"][i] = t["rainhas"][j]
                t["rainhas"][j] = aux
                t["conflitos"] = heuristica(t["rainhas"])
                tabuleiro["filhos"].append(t)


def melhorfilho(tabuleiro):
    aux = tabuleiro["filhos"][0]
    for i in tabuleiro["filhos"]:
        if aux["conflitos"] > i["conflitos"]:
            aux = i

    return aux


def subida_da_encosta(tabuleiro):
    i = 0
    corrente = tabuleiro

    while(True):
        expande(corrente)
        proximo = melhorfilho(corrente)
        if proximo["conflitos"] > corrente["conflitos"] or corrente["conflitos"] == 0:
            return corrente
        corrente = proximo

        if corrente["conflitos"] == 2 and i < 15:
            i = i + 1
        elif corrente["conflitos"] == 2 and i == 15:
            embaralha(tabuleiro)
            tabuleiro["conflitos"] = heuristica(tabuleiro["rainhas"])
            corrente = tabuleiro



def monta_tabuleiro(tabuleiro):

    tabuleiro["pecas"] = [[0 for j in range(len(tabuleiro["rainhas"]))] for i in range(len(tabuleiro["rainhas"]))]
    for i in range(len(tabuleiro["rainhas"])):
        tabuleiro["pecas"][tabuleiro["rainhas"][i]][i] = i + 1

    return tabuleiro

def recristalizacao(tabuleiro):
    corrente = tabuleiro
    t = 100 * len(tabuleiro["rainhas"])
    while(True):
        random.seed()
        expande(corrente)
        randomico1 = random.randint(0,len(corrente["filhos"]) - 1)
        randomico2 = random.randint(0,len(corrente["filhos"]) - 1)

        if t == 0:
            t = 100 * len(tabuleiro["rainhas"])

        if corrente ["conflitos"] == 0:
            return corrente

        proximo = corrente["filhos"][randomico1]
        delta_e = proximo["conflitos"] - corrente["conflitos"]

        if delta_e < 0:
            corrente = proximo
        else:
            if euler < euler**(delta_e/t):
                while randomico1 == randomico2:
                    randomico2 = random.randint(0,len(corrente["filhos"]) - 1)
                corrente = corrente["filhos"][randomico2]
            else:
                t = t - 1

def main():
    n = 0
    while(n < 4):
        n = input("Digite o numero de rainhas(lembrando que o numero devera ser maior que 3): ")

    l = []
    pecas = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        pecas[i][i] = i+1 # inserindo as rainhas na diagonal
        l.append(i)


    tabuleiro = cria_tabuleiro(pecas,l)

    embaralha(tabuleiro)
    tabuleiro["conflitos"] = heuristica(tabuleiro["rainhas"])
    print "Estado inicial"
    for i in tabuleiro["pecas"]:
        print i
    print "Conflitos:", tabuleiro["conflitos"]

    ini1 = time.time()
    s = subida_da_encosta(tabuleiro)
    fim1 = time.time()

    ini2 = time.time()
    r = recristalizacao(tabuleiro)
    fim2 = time.time()


    s = monta_tabuleiro(s)
    r = monta_tabuleiro(r)

    print "Subida da encosta:"
    print "Solucao:"
    print "rainhas",s["rainhas"]
    for i in s["pecas"]:
        print i
    print "Conflitos:", heuristica(s["rainhas"])
    print "Tempo:", fim1 - ini1

    print "\n------------------------------------------------------------------\n"


    print "Recristalizacao Simulada:"
    print "Solucao:"
    print "rainhas",r["rainhas"]
    for i in r["pecas"]:
        print i
    print "Conflitos", heuristica(r["rainhas"])
    print "Tempo:" ,fim2 - ini2


    return 0

main()
