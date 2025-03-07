import time
import random

def bubble_sort(arr):  # Ordena a lista usando o algoritmo Bubble Sort
    
    n = len(arr) # Pegamos o tamanho da lista arr
    for i in range(n): # Repetimos o processo n vezes 
        swapped = False  # Variável para otimizar se não houver trocas
        for j in range(0, n - i - 1): # Compara pares vizinhos, seguindo o processo de ordenação com o Bubble Sort
                     #[5, 10, 8, 4, 2] range(0,4) 
                     #[5, 10, 8, 4, 2] range(0,3)
                     #[5, 8, 10, 4, 2] range(0,2)
                     #[5, 8, 4, 10, 2] range(0,1) 

            if arr[j] > arr[j + 1]:  # Se estiverem fora de ordem, trocamos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos
                swapped = True # Marca que houve troca
        if not swapped:
            break  # Se não houve trocas, a lista já está ordenada

def medir_tempo(tamanho): # Mede o tempo de execução do Bubble Sort para um array aleatório.
    
    arr = [random.randint(0, 10000) for _ in range(tamanho)]  # Gera lista aleatória
    inicio = time.time()  # Marca o tempo inicial
    bubble_sort(arr)  # Executa o algoritmo
    fim = time.time()  # Marca o tempo final
    return fim - inicio # Retorna o tempo gasto

# Testando para diferentes tamanhos de listas
tamanhos = [100, 1000, 10000, 100000]
for tamanho in tamanhos:
    tempo_gasto = medir_tempo(tamanho)
    print(f"Tempo para ordenar {tamanho} elementos: {tempo_gasto:.3f} segundos")

    




