import random
import time

def improved_bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    for i in range(n):
        trocas_na_iteracao = 0

        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                trocas_na_iteracao += 1

        # Se não houve trocas na última iteração, a lista está ordenada
        if trocas_na_iteracao == 0:
            break

    return trocas, comparacoes

def test_improved_bubble_sort(arr):   
    start_time = time.time()
    trocas, comparacoes = improved_bubble_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes
