"""
Módulo para comparação empírica de algoritmos de ordenação.

Este script atende ao dever 01, comparando o tempo de execução do 
algoritmo Insertion Sort O(n^2) com a função nativa sorted() O(n log n).
"""

import time
import random

TAMANHOS_TESTE = [1000, 5000, 10000, 20000, 50000]

def insertion_sort(arr):
    """
    Ordena uma lista in-place utilizando o algoritmo Insertion Sort.

    Complexidade de tempo: O(n^2).
    """
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def executar_dever():
    """
    Executa os testes de desempenho e exibe os resultados no terminal.
    """
    print("==================================================")
    print(" DEVER DE CASA - A BARREIRA DO n^2")
    print("==================================================\n")
    
    for n in TAMANHOS_TESTE:
        print(f"--- Testando para n = {n} ---")
        
        lista_original = [random.randint(0, 100000) for _ in range(n)]
        
        lista_insertion = lista_original.copy()
        inicio_insertion = time.time()
        insertion_sort(lista_insertion)
        fim_insertion = time.time()
        tempo_insertion = fim_insertion - inicio_insertion
        
        lista_timsort = lista_original.copy()
        inicio_timsort = time.time()
        _ = sorted(lista_timsort)
        fim_timsort = time.time()
        tempo_timsort = fim_timsort - inicio_timsort
        
        print(f"Tempo Insertion Sort O(n^2) : {tempo_insertion:.6f} segundos")
        print(f"Tempo sorted() O(n log n)   : {tempo_timsort:.6f} segundos")
        print("-" * 50)

if __name__ == "__main__":
    executar_dever()