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

    for i in range(8):
        tabuleiro["pecas"][i][i] = i # inserindo as rainhas na diagonal
        tabuleiro["rainhas"].append((i, i)) # salvando as posicoes das rainhas

    return tabuleiro