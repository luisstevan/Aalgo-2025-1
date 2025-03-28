import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(raiz, valor):
    """ Insere um novo nó na ABB """
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    else:
        raiz.direita = inserir(raiz.direita, valor)
    return raiz

def pesquisar(raiz, valor):
    """ Pesquisa um valor na ABB """
    if raiz is None or raiz.valor == valor:
        return raiz
    if valor < raiz.valor:
        return pesquisar(raiz.esquerda, valor)
    return pesquisar(raiz.direita, valor)

def encontrar_minimo(no):
    """ Encontra o menor valor em uma ABB """
    atual = no
    while atual and atual.esquerda is not None:
        atual = atual.esquerda
    return atual

def remover(raiz, valor):
    """ Remove um nó da ABB """
    if raiz is None:
        return raiz
    if valor < raiz.valor:
        raiz.esquerda = remover(raiz.esquerda, valor)
    elif valor > raiz.valor:
        raiz.direita = remover(raiz.direita, valor)
    else:
        if raiz.esquerda is None:
            return raiz.direita
        elif raiz.direita is None:
            return raiz.esquerda
        temp = encontrar_minimo(raiz.direita)
        raiz.valor = temp.valor
        raiz.direita = remover(raiz.direita, temp.valor)
    return raiz

def construir_arvore(n):
    """ Constrói uma ABB com N nós """
    if n < 1:
        return None
    valores = random.sample(range(1, 101), n)
    raiz = No(valores[0])
    for valor in valores[1:]:
        inserir(raiz, valor)
    return raiz, valores

def imprimir_arvore(raiz, nivel=0):
    """ Imprime a ABB de forma hierárquica """
    if raiz is not None:
        imprimir_arvore(raiz.direita, nivel + 1)
        print(' ' * 4 * nivel + '->', raiz.valor)
        imprimir_arvore(raiz.esquerda, nivel + 1)

# Exemplo de uso
N = 15  # Número de nós desejados
arvore, valores = construir_arvore(N)
print("Árvore gerada:")
imprimir_arvore(arvore)
print("Valores inseridos:", valores)

# Teste das operações
valor_pesquisa = valores[5]  # Escolhe um valor aleatório para pesquisa
print(f"\nPesquisando {valor_pesquisa} na árvore: ", "Encontrado" if pesquisar(arvore, valor_pesquisa) else "Não encontrado")

valor_remover = valores[3]  # Escolhe um valor aleatório para remoção
print(f"\nRemovendo {valor_remover} da árvore...")
arvore = remover(arvore, valor_remover)
imprimir_arvore(arvore)
