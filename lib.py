import random


def esercizio_di_esempio(numeri_da_generare, numero_min, numero_max):
    lista_numeri = [["Numeri generati"], []]

    for _ in range(int(numeri_da_generare)):
        lista_numeri[1].append(random.randint(int(numero_min), int(numero_max)))

    return lista_numeri
