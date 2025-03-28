def is_palindrome(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    # Caso base: Se o índice inicial ultrapassar o índice final, é um palíndromo
    if start >= end:
        return True

    # Comparar os elementos nas posições 'start' e 'end'
    if arr[start] != arr[end]:
        return False

    # Chamada recursiva com os índices incrementados e decrementados
    return is_palindrome(arr, start + 1, end - 1)

# Testando os exemplos fornecidos:

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(f"array1 é palíndromo? {is_palindrome(array1)}")  # True
print(f"array2 é palíndromo? {is_palindrome(array2)}")  # True
print(f"array3 é palíndromo? {is_palindrome(array3)}")  # True
print(f"array4 é palíndromo? {is_palindrome(array4)}")  # False




