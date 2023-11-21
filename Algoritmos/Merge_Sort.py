import random
import time

def merge_sort(arr):
    trocas = 0
    comparacoes = 0

    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        trocas_esquerda, comparacoes_esquerda = merge_sort(metade_esquerda)
        trocas_direita, comparacoes_direita = merge_sort(metade_direita)

        trocas += trocas_esquerda + trocas_direita
        comparacoes += comparacoes_esquerda + comparacoes_direita

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            comparacoes += 1
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
                trocas += 1
            k += 1

        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1

    return trocas, comparacoes

def test_merge_sort(arr):
    start_time = time.time()
    trocas, comparacoes = merge_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes
