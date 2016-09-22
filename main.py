import ia
import random

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


def main():
	items = range(9)      # items do tabuleiro
	random.shuffle(items) # embaralhando os items do tabuleiro
	t = cria_tabuleiro(items) # criando o tabuleiro
	operadores = [move_baixo, move_cima, move_direita, move_esquerda] # lista de operadores do problema
	# instanciando o problema
	problema = ia.Problema(t, operadores, teste_meta, funcao_custo)
	print "Saida:", ia.busca(problema, enfileira_fifo)

	return 0

print "O programa executou com saida %d" % (main())
