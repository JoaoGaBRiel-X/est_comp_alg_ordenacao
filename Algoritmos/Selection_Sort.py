import random
import time

def selection_sort(arr):
    trocas = 0
    comparacoes = 0
    n = len(arr)

    for i in range(n - 1):
        indice_menor = i

        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[indice_menor]:
                indice_menor = j

        if i != indice_menor:
            arr[i], arr[indice_menor] = arr[indice_menor], arr[i]
            trocas += 1

    return trocas, comparacoes

def test_selection_sort(arr):
    start_time = time.time()
    trocas, comparacoes = selection_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes
