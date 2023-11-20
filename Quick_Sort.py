import random
import time

print("Quick Sort")

def quick_sort(arr):
    trocas = 0
    comparacoes = 0
    if len(arr) <= 1:
        return arr, trocas, comparacoes
    else:
        pivot = arr.pop()
        menores = []
        maiores = []
        for elemento in arr:
            comparacoes += 1
            if elemento <= pivot:
                menores.append(elemento)
            else:
                maiores.append(elemento)
                trocas += 1

        ordenados_menores, trocas_menores, comparacoes_menores = quick_sort(menores)
        ordenados_maiores, trocas_maiores, comparacoes_maiores = quick_sort(maiores)

        return ordenados_menores + [pivot] + ordenados_maiores, trocas + trocas_menores + trocas_maiores, comparacoes + comparacoes_menores + comparacoes_maiores

def test_quick_sort(tamanho, caso):
    if caso == "melhor":
        arr = list(range(1, tamanho + 1))
    elif caso == "medio":
        arr = random.sample(range(1, tamanho + 1), tamanho)
    elif caso == "pior":
        arr = list(range(tamanho, 0, -1))
    
    start_time = time.time()
    ordenados, trocas, comparacoes = quick_sort(arr.copy())
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes

# Teste do algoritmo para os diferentes casos
tamanhos = [1000, 10000, 100000]
casos = ["melhor", "medio", "pior"]

for tamanho in tamanhos:
    for caso in casos:
        tempo, trocas, comparacoes = test_quick_sort(tamanho, caso)
        print("Quick Sort")
        print(f"Tamanho: {tamanho}, Caso: {caso.capitalize()}")
        print(f"Tempo de Execucao: {tempo:.6f} segundos")
        print(f"Quantidade de Trocas: {trocas}")
        print(f"Quantidade de Comparacoes: {comparacoes}")
        print("="*40)