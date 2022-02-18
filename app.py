#!/usr/bin/env python
#

import random


def vue_python_sandbox(numeri_da_generare: str, numero_min: str, numero_max: str) -> list[list[str]]:
    lista_numeri = [["Numeri generati:"], []]

    for _ in range(int(numeri_da_generare)):
        lista_numeri[1].append(random.randint(int(numero_min), int(numero_max)))

    return lista_numeri


if __name__ == '__main__':
    #
    # Da utilizzare solo a fini di debug...
    #

    numeri_da_generare = input("Inserisci quanti numeri vuoi generare: ")
    numero_min = input("Inserisci il numero minimo: ")
    numero_max = input("Inserisci il numero massimo: ")

    risultato = vue_python_sandbox(numeri_da_generare, numero_min, numero_max)

    print()
    for riga in risultato:
        riga_formattata = ", ".join(map(lambda el: f"{el}", riga))

        print(riga_formattata)
