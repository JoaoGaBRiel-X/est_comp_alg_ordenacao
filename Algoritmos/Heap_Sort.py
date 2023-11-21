import random
import time

def heapify(arr, n, i, comparacoes, trocas):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Comparar com o filho da esquerda
    comparacoes += 1
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    # Comparar com o filho da direita
    comparacoes += 1
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    # Trocar se o maior não for a raiz
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        trocas += 1

        # Heapify recursivamente a subárvore afetada
        trocas, comparacoes = heapify(arr, n, maior, comparacoes, trocas)

    return trocas, comparacoes

def heap_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0

    # Construir um max heap
    for i in range(n // 2 - 1, -1, -1):
        trocas, comparacoes = heapify(arr, n, i, comparacoes, trocas)

    # Extrair elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Trocar
        trocas += 1

        # Heapify a raiz
        trocas, comparacoes = heapify(arr, i, 0, comparacoes, trocas)

    return trocas, comparacoes

def test_heap_sort(arr):
    start_time = time.time()
    trocas, comparacoes = heap_sort(arr.copy())
    end_time = time.time()

    tempo_execucao = end_time - start_time

    return tempo_execucao, trocas, comparacoes
