import ia
import random
import copy
import math

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
               #print i , j
                soma = soma + 1
                #print soma
                #print "primeira", l[i],i
                #print "segunda", l[j],j

    return soma




def expande(tabuleiro):

    for i in range(len(tabuleiro["rainhas"]) - 1):
        for j in range(i + 1,len(tabuleiro["rainhas"])):
                #print i,j
                t = cria_tabuleiro([],[])
                t["rainhas"] = tabuleiro["rainhas"][:]
                #t["rainhas"] = copy.copy(tabuleiro["rainhas"])
                #t["pecas"] = tabuleiro["pecas"][:][:]
                aux = t["rainhas"][i]
                t["rainhas"][i] = t["rainhas"][j]
                t["rainhas"][j] = aux
                t["conflitos"] = heuristica(t["rainhas"])
                #print  t["rainhas"] , "conflitos" , t["conflitos"]
                tabuleiro["filhos"].append(t)


def melhorfilho(tabuleiro):
    aux = tabuleiro["filhos"][0]
    for i in tabuleiro["filhos"]:
        if aux["conflitos"] > i["conflitos"]:
            aux = i
    print "verifica melhot", aux["conflitos"]

    return aux


def subida_de_encosta(tabuleiro):

    corrente = tabuleiro

    while(True):
        expande(corrente)
        proximo = melhorfilho(corrente)
        #print proximo["conflitos"]
        if proximo["conflitos"] > corrente["conflitos"] or corrente["conflitos"] == 0:
            #print "conflitos" ,corrente["conflitos"]
            print corrente["rainhas"]
            return corrente
        corrente = proximo
        #print "conflitos" ,corrente["conflitos"]


def monta_tabuleiro(tabuleiro):

    tabuleiro["pecas"] = [[0 for j in range(len(tabuleiro["rainhas"]))] for i in range(len(tabuleiro["rainhas"]))]
    for i in range(len(tabuleiro["rainhas"])):
        tabuleiro["pecas"][tabuleiro["rainhas"][i]][i] = i + 1

    return tabuleiro

def recristalizacao(tabuleiro):
    corrente = tabuleiro
    t = 400
    while(True):

        random.seed()
        randomico1 = random.randint(0,len(tabuleiro["rainhas"]) - 1)
        randomico2 = random.randint(0,len(tabuleiro["rainhas"]) - 1)

        if t == 0 or corrente ["conflitos"] == 0:
            return corrente
        expande(corrente)
        proximo =  corrente["filhos"][randomico1]
        delta_e = proximo["conflitos"] - corrente["conflitos"]

        print "executou", delta_e

        if delta_e > 0:
            print "passou"
            if euler < math.exp(delta_e/t):
                while randomico1 == randomico2:
                    randomico2 = random.randint(0,len(tabuleiro["rainhas"]) - 1)
                corrente = corrente["filhos"][randomico2]
            t = t - 1


def main():
    n = 8
    l = []
    pecas = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        pecas[i][i] = i+1 # inserindo as rainhas na diagonal
        l.append(i)


    tabuleiro = cria_tabuleiro(pecas,l)

    embaralha(tabuleiro)
    tabuleiro["conflitos"] = heuristica(tabuleiro["rainhas"])
    for i in tabuleiro["pecas"]:
        print i
    print tabuleiro["conflitos"]

    #r = subida_de_encosta(tabuleiro)
    r = recristalizacao(tabuleiro)
    r = monta_tabuleiro(r)
    print "rainhas",r["rainhas"]
    for i in r["pecas"]:
        print i
    print "heuristica", heuristica(r["rainhas"])
    #for i in r["pecas"]:
    #  print i

    return 0

main()
