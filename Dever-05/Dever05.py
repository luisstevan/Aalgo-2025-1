import numpy as np
import math

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Multiplicação de matrizes tradicional
def multiply_matrices(A, B):
    return np.dot(A, B)

# Resolução das recorrências

def recurrence_1(n):
    if n <= 1:
        return 1
    return 2 * recurrence_1(n // 4) + math.sqrt(n)

def recurrence_2(n):
    if n <= 1:
        return 1
    return 2 * recurrence_2(n // 4) + n

def recurrence_3(n):
    if n <= 1:
        return 1
    return 16 * recurrence_3(n // 4) + n ** 2

# Teste
data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = merge_sort(data)
print("Merge Sort:", sorted_data)

# Testando multiplicação de matrizes
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = multiply_matrices(A, B)
print("Multiplicação de Matrizes:\n", result)

# Testando recorrências
n = 16
print("Recorrência 1:", recurrence_1(n))
print("Recorrência 2:", recurrence_2(n))
print("Recorrência 3:", recurrence_3(n))
