import time

def fatorial(n):
    """
    Função recursiva para calcular o fatorial de um número.
    Caso base: fatorial(0) = 1
    Caso recursivo: fatorial(n) = n * fatorial(n-1)
    """
    if n == 0 or n == 1:
        return 1
    else:
    return n * fatorial(n - 1)

# Valores de n para teste
valores_n = [10, 100, 500, 1000]

tempos_execucao = {}

for n in valores_n:
    inicio = time.time()
    try:
        resultado = fatorial(n)
    except RecursionError:
        resultado = "Erro: Recursão muito profunda"
    fim = time.time()
    
    tempos_execucao[n] = fim - inicio
    print(f"Fatorial({n}) calculado em {tempos_execucao[n]:.5f} segundos")
