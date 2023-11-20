import random
import time

print("Selection Sort")

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

def test_selection_sort(tamanho, caso):
    if caso == "melhor":
        arr = list(range(1, tamanho + 1))
    elif caso == "medio":
        arr = random.sample(range(1, tamanho + 1), tamanho)
    elif caso == "pior":
        arr = list(range(tamanho, 0, -1))
    
    start_time = time.time()
    trocas, comparacoes = selection_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes

# Teste do algoritmo para os diferentes casos
tamanhos = [1000, 10000, 100000]
casos = ["melhor", "medio", "pior"]

for tamanho in tamanhos:
    for caso in casos:
        tempo, trocas, comparacoes = test_selection_sort(tamanho, caso)
        print("Selection Sort")
        print(f"Tamanho: {tamanho}, Caso: {caso.capitalize()}")
        print(f"Tempo de Execucao: {tempo:.6f} segundos")
        print(f"Quantidade de Trocas: {trocas}")
        print(f"Quantidade de Comparacoes: {comparacoes}")
        print("="*40)
