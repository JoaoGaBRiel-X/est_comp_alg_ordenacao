import random
import time

from Algoritmos.Bubble_Sort import test_bubble_sort
from Algoritmos.Improved_Bubble_Sort import test_improved_bubble_sort
from Algoritmos.Insertion_Sort import test_insertion_sort
from Algoritmos.Selection_Sort import test_selection_sort
from Algoritmos.Merge_Sort import test_merge_sort
from Algoritmos.Quick_Sort import test_quick_sort
from Algoritmos.Heap_Sort import test_heap_sort

# Geracao das listas
crescente1 = list(range(1, 1000 + 1))
aleatorio1 = random.sample(range(1, 1000 + 1), 1000)
decrescente1 = list(range(1000, 0, -1))
crescente2 = list(range(1, 10000 + 1))
aleatorio2 = random.sample(range(1, 10000 + 1), 10000)
decrescente2 = list(range(10000, 0, -1))
crescente3 = list(range(1, 100000 + 1))
aleatorio3 = random.sample(range(1, 100000 + 1), 100000)
decrescente3 = list(range(100000, 0, -1))


def teste(tamanho, caso, funcao, arr):
    t, tr, comp = funcao(arr)
    print(f"Tamanho: {tamanho}, Caso: {caso.capitalize()}")
    print(f"Tempo de Execucao: {t:.6f} segundos")
    print(f"Quantidade de Trocas: {tr}")
    print(f"Quantidade de Comparacoes: {comp}")
    print("="*40)

def teste_casos(funcao):
    # Teste do algoritmo para os diferentes casos
    tamanhos = [1000, 10000, 100000]
    casos = ["melhor", "medio", "pior"]
    for tamanho in tamanhos:
        for caso in casos:
            if tamanho == 1000:
                if caso == "melhor":
                    teste(tamanho, caso, funcao, crescente1.copy())
                if caso == "medio":
                    teste(tamanho, caso, funcao, aleatorio1.copy())
                if caso == "pior":
                    teste(tamanho, caso, funcao, decrescente1.copy())
            if tamanho == 10000:
                if caso == "melhor":
                    teste(tamanho, caso, funcao, crescente2.copy())
                if caso == "medio":
                    teste(tamanho, caso, funcao, aleatorio2.copy())
                if caso == "pior":
                    teste(tamanho, caso, funcao, decrescente2.copy())
            if tamanho == 100000:
                if caso == "melhor":
                    teste(tamanho, caso, funcao, crescente3.copy())
                if caso == "medio":
                    teste(tamanho, caso, funcao, aleatorio3.copy())
                if caso == "pior":
                    teste(tamanho, caso, funcao, decrescente3.copy())

######################################################################
# BUBBLE SORT ########################################################
######################################################################
print("BUBBLE SORT")
teste_casos(test_bubble_sort)
print("FIM")
print(" ")

######################################################################
# IMPROVED BUBBLE SORT ###############################################
######################################################################
print("IMPROVED BUBBLE SORT")
teste_casos(test_improved_bubble_sort)
print("FIM")
print(" ")

######################################################################
# INSERTION SORT #####################################################
######################################################################
print("INSERTION SORT")
teste_casos(test_insertion_sort)
print("FIM")
print(" ")

######################################################################
# SELECTION SORT #####################################################
######################################################################
print("SELECTION SORT")
teste_casos(test_selection_sort)
print("FIM")
print(" ")

######################################################################
# MERGE SORT #########################################################
######################################################################
print("MERGE SORT")
teste_casos(test_merge_sort)
print("FIM")
print(" ")

######################################################################
# QUICK SORT #########################################################
######################################################################
print("QUICK SORT")
teste_casos(test_quick_sort)
print("FIM")
print(" ")

######################################################################
# HEAP SORT ##########################################################
######################################################################
print("HEAP SORT")
teste_casos(test_heap_sort)
print("FIM")
print(" ")
