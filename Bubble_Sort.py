import random
import time

print("Bubble Sort")

def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1

    return trocas, comparacoes

def test_bubble_sort(tamanho, caso):
    if caso == "melhor":
        arr = list(range(1, tamanho + 1))
    elif caso == "medio":
        arr = random.sample(range(1, tamanho + 1), tamanho)
    elif caso == "pior":
        arr = list(range(tamanho, 0, -1))
    
    start_time = time.time()
    trocas, comparacoes = bubble_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes

# Teste do algoritmo para os diferentes casos
tamanhos = [1000, 10000, 100000]
casos = ["melhor", "medio", "pior"]

for tamanho in tamanhos:
    for caso in casos:
        tempo, trocas, comparacoes = test_bubble_sort(tamanho, caso)
        print("Bubble Sort")
        print(f"Tamanho: {tamanho}, Caso: {caso.capitalize()}")
        print(f"Tempo de Execucao: {tempo:.6f} segundos")
        print(f"Quantidade de Trocas: {trocas}")
        print(f"Quantidade de Comparacoes: {comparacoes}")
        print("="*40)