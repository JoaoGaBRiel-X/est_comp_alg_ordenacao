import random
import time

def insertion_sort(arr):
    trocas = 0
    comparacoes = 0

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        comparacoes += 1

        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            trocas += 1
            j -= 1

        arr[j + 1] = chave

    return trocas, comparacoes

def test_insertion_sort(arr):
    start_time = time.time()
    trocas, comparacoes = insertion_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes
