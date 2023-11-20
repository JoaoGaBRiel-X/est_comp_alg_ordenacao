import random
import time

print("Insertion Sort")

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

def test_insertion_sort(tamanho, caso):
    if caso == "melhor":
        arr = list(range(1, tamanho + 1))
    elif caso == "medio":
        arr = random.sample(range(1, tamanho + 1), tamanho)
    elif caso == "pior":
        arr = list(range(tamanho, 0, -1))
    
    start_time = time.time()
    trocas, comparacoes = insertion_sort(arr)
    end_time = time.time()
    
    tempo_execucao = end_time - start_time
    
    return tempo_execucao, trocas, comparacoes

# Teste do algoritmo para os diferentes casos
tamanhos = [1000, 10000, 100000]
casos = ["melhor", "medio", "pior"]

for tamanho in tamanhos:
    for caso in casos:
        tempo, trocas, comparacoes = test_insertion_sort(tamanho, caso)
        print("Insertion Sort")
        print(f"Tamanho: {tamanho}, Caso: {caso.capitalize()}")
        print(f"Tempo de Execucao: {tempo:.6f} segundos")
        print(f"Quantidade de Trocas: {trocas}")
        print(f"Quantidade de Comparacoes: {comparacoes}")
        print("="*30)
