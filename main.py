import ia
from random import *
import random
import time

comparacoes = 0

def cria_tabuleiro(items):
	"""
	Funcao que cria um tabuleiro novo para ser resolvido pelos algoritmos inteligentes
	@paaram items: itens que vao compor o tabuleiro. O maximo de itens e 9 para
	construir uma matriz 3x3
	"""
	tabuleiro = {}
	# posicionando as pecas
	tabuleiro["pecas"] = [[items[i * 3 + j] for j in range(3)] for i in range(3)]

	for i in range(3):
		for j in range(3):
			# encontrando a peca "branca" para movimentar
			if tabuleiro["pecas"][i][j] == 0:
				tabuleiro["posicao"] = i, j
				break

	return tabuleiro

# operacoes definidas em cima do tabuleiro. Todos devidamente testados

def move_esquerda(tabuleiro):
	"""
	Move a peca branca para esquerda.
	@param tabuleiro: tabuleiro onde a peca sera movida
	@return uma copia resultante do trabalho de movimentar a peca ou None caso continue
	o mesmo.
	"""
	i, j = tabuleiro["posicao"] # obtendo a linha e a coluna do tabuleiro atual

	if j == 0: return None # caso nao de pra realizar nenhum movimento a partir daqui

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i][j - 1] = novo["pecas"][i][j - 1], novo["pecas"][i][j]
	novo["posicao"] = i, j - 1

	return novo


def move_direita(tabuleiro):
	"""
	Move a peca branca para direita.
	@param tabuleiro: tabuleiro onde a peca sera movida
	@return uma copia resultante do trabalho de movimentar a peca ou None caso continue
	o mesmo.
	"""
	"""
	Move a peca branca para cima.
	@param tabuleiro: tabuleiro onde a peca sera movida
	@return uma copia resultante do trabalho de movimentar a peca ou None caso continue
	o mesmo.
	"""
	i, j = tabuleiro["posicao"] # obtendo a linha e a coluna do tabuleiro atual

	if j == 2: return None # caso nao de pra realizar nenhum movimento a partir daqui

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i][j + 1] = novo["pecas"][i][j + 1], novo["pecas"][i][j]
	novo["posicao"] = i, j + 1

	return novo


def move_cima(tabuleiro):
	"""
	Move a peca branca para cima.
	@param tabuleiro: tabuleiro onde a peca sera movida
	@return uma copia resultante do trabalho de movimentar a peca ou None caso continue
	o mesmo.
	"""
	i, j = tabuleiro["posicao"] # obtendo a linha e a coluna do tabuleiro atual

	if i == 0: return None # caso nao de pra realizar nenhum movimento a partir daqui

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i - 1][j] = novo["pecas"][i - 1][j], novo["pecas"][i][j]
	novo["posicao"] = i - 1, j

	return novo


def move_baixo(tabuleiro):
	"""
	Move a peca branca para baixo.
	@param tabuleiro: tabuleiro onde a peca sera movida
	@return uma copia resultante do trabalho de movimentar a peca ou None caso continue
	o mesmo.
	"""
	i, j = tabuleiro["posicao"] # obtendo a linha e a coluna do tabuleiro autal

	if i == 2: return None

	novo = {}
	novo["pecas"] = [[elemento for elemento in linha] for linha in tabuleiro["pecas"]]
	novo["pecas"][i][j], novo["pecas"][i + 1][j] = novo["pecas"][i + 1][j], novo["pecas"][i][j]
	novo["posicao"] = i + 1, j

	return novo



def funcao_custo(tabuleiro):
	"""
	Retorna o custo do arranjo atual do tabuleiro ate a meta
	@param tabuleiro: tabuleiro em seu arranjo atual de pecas
	@return: a quantidade de pecas fora do lugar
	"""

	return 1


def teste_meta(tabuleiro):
	"""
	Funcao que verifica se o arranjo atual do tabuleiro esta de acordo com a meta
	@param tabuleiro: estado atual do tabuleiro
	@return true se o tabuleiro e a meta, false caso contrario
	"""

	return tabuleiro["pecas"] == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def enfileira_fifo(lista_1, lista_2):
	return lista_2 + lista_1

def enfileira_lifo(lista_1,lista_2):
	return lista_1 + lista_2

def embaralha(tabuleiro,operadores):
	random.seed()
	n = randint(1000,10000)
	l = [0,1,2,3]

	for i in range(n):
		random.shuffle(l)
		for j in l:
			if operadores[j](tabuleiro) != None:
				tabuleiro = operadores[j](tabuleiro)
				#print tabuleiro["pecas"]
	tabuleiro = operadores[randint(0,3)](tabuleiro)
	return tabuleiro

def heuristica_desordenado(tabuleiro):
	meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
	contador = 0
	for i in range(3):
		for j in range(3):
			if meta[i][j] != tabuleiro["pecas"][i][j]:
				contador = contador + 1
	return contador

def heuristica_manhattan(tabuleiro):
	meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
	soma = 0
	#print tabuleiro["pecas"]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					if meta[i][j] == tabuleiro["pecas"][k][l]:
						soma = soma + abs(int(i - k)) + abs(int(j - l))
						#print soma
	return soma




def main():
	items = [4,1,3,2,6,8,7,5,0]      # items do tabuleiro
	#random.shuffle(items) # embaralhando os items do tabuleiro
	teste1 = cria_tabuleiro(items) # criando o tabuleiro

	operadores = [move_baixo, move_cima, move_direita, move_esquerda] # lista de operadores do problema
	# instanciando o problema
	#teste = embaralha(t,operadores)

	#teste1 = [[1,2,3],[4,0,6],[7,5,8]]

	#Problemas:
	"""Sem heuristica:"""
	#largura
	problema = ia.Problema(teste1, operadores, teste_meta, funcao_custo)
	#profundiade
	problema1 = ia.Problema(teste1, operadores, teste_meta, funcao_custo)
	#gulosa
	problema2 = ia.Problema(teste1, operadores, teste_meta, heuristica_desordenado)
	#A* desordenado
	problema3 = ia.Problema(teste1, operadores, teste_meta, heuristica_desordenado)
	#A* Manhattan
	problema4 = ia.Problema(teste1, operadores, teste_meta, heuristica_manhattan)

	ini = time.time()
	resultado = ia.busca(problema, enfileira_fifo)
	fim = time.time()
	ini1 = time.time()
	resultado1 = ia.busca(problema1, enfileira_lifo)
	fim1 = time.time()
	ini2 = time.time()
	resultado2 = ia.buscagulosa(problema2, enfileira_lifo)
	fim2 = time.time()
	ini3 = time.time()
	resultado3 = ia.buscaaestrela(problema3, enfileira_lifo)
	fim3 = time.time()
	ini4 = time.time()
	resultado4 = ia.buscaaestrela(problema4, enfileira_lifo)
	fim4 = time.time()

	print "Busca em Largura"
	print "Estado Inicial:",teste1["pecas"]
	print "Saida Busca em Largura: ", resultado
	print "Tempo: ", fim - ini
	print "Numero de comparacoes: ", problema.comparacoes
	print "-------------------------------------------------"
	print "Busca em Profundiade"
	print "Estado Inicial:",teste1["pecas"]
	print "Saida Busca em Largura: ", resultado1
	print "Tempo: ", fim1 - ini1
	print "Numero de comparacoes: ", problema1.comparacoes
	print "-------------------------------------------------"
	print "Busca em Gulosa"
	print "Estado Inicial:",teste1["pecas"]
	print "Saida Busca em Largura: ", resultado2
	print "Tempo: ", fim2 - ini2
	print "Numero de comparacoes: ", problema2.comparacoes
	print "-------------------------------------------------"
	print "Busca A* numero de pessas fora do lugar"
	print "Estado Inicial:",teste1["pecas"]
	print "Saida Busca em Largura: ", resultado3
	print "Tempo: ", fim3 - ini3
	print "Numero de comparacoes: ", problema3.comparacoes
	print "-------------------------------------------------"
	print "Busca A* Distancia de Manhattan"
	print "Estado Inicial:",teste1["pecas"]
	print "Saida Busca em Largura: ", resultado4
	print "Tempo: ", fim4 - ini4
	print "Numero de comparacoes: ", problema4.comparacoes
	print "-------------------------------------------------"

	"""Com heuristica:"""
	"""		Numero de pecas fora de posicao		"""
	"""problema = ia.Problema(teste, operadores, teste_meta, heuristica_desordenado)"""
	"""		Distancia de Manhattan		"""
	"""problema = ia.Problema(teste, operadores, teste_meta, heuristica_manhattan)"""

	"""Buscas:"""


	"""print "Saida Busca em Profundidade:", ia.busca(problema, enfileira_lifo)"""
	"""print "Saida Busca Gulosa:", ia.buscagulosa(problema, enfileira_lifo)"""
	"""print "Saida Busca A*:", ia.buscaaestrela(problema, enfileira_lifo)"""
	return 0

print "O programa executou com saida %d" % (main())
