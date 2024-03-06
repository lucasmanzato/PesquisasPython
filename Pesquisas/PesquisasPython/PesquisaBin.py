import random

lista = [random.randint(1, 100) for _ in range(100)]
lista.sort()
print(lista)  

x = int(input("Qual valor deseja buscar? "))

cont = 0
inicio = 0
fim = len(lista) - 1
encontrado = False

while inicio <= fim:
    cont += 1
    meio = (inicio + fim) // 2

    if lista[meio] == x:
        print(f"{x} foi encontrado na posição {meio}, foram feitas {cont} verificações.")
        encontrado = True
        break

    elif lista[meio] < x:
        inicio = meio + 1

    else:
        fim = meio - 1

if encontrado == False:
    print(f"{x} não foi encontrado na lista. Foram feitas {cont} verificações!")
