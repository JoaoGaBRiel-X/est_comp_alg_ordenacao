import random
import time

def quick_sort_iterative(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    # Pilha para armazenar os limites da sublista
    pilha = [(0, n - 1)]

    while pilha:
        # Desempilha os limites da sublista
        inicio, fim = pilha.pop()

        # Particiona a sublista e obtém o índice do pivô
        pivot_index, comparacoes_part, trocas_part = partition(arr, inicio, fim)
        comparacoes += comparacoes_part
        trocas += trocas_part

        # Se houver elementos à esquerda do pivô, empilhe os limites
        if pivot_index - 1 > inicio:
            pilha.append((inicio, pivot_index - 1))

        # Se houver elementos à direita do pivô, empilhe os limites
        if pivot_index + 1 < fim:
            pilha.append((pivot_index + 1, fim))

    return trocas, comparacoes

def partition(arr, inicio, fim):
    pivot = arr[fim]
    i = inicio - 1
    comparacoes = 0
    trocas = 0

    for j in range(inicio, fim):
        comparacoes += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            trocas += 1

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    trocas += 1

    return i + 1, comparacoes, trocas

def test_quick_sort(arr):
    start_time = time.time()
    trocas, comparacoes = quick_sort_iterative(arr.copy())
    end_time = time.time()

    tempo_execucao = end_time - start_time

    return tempo_execucao, trocas, comparacoes
