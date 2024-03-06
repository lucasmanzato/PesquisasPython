import random

lista = [random.randint(1, 100) for _ in range(100)]
lista.sort()
print(lista)  

x = int(input("Qual valor deseja buscar? "))
cont = 0
cont2 = 0
inicio = 0
fim = len(lista) - 1

while inicio <= fim:
    cont += 1
    meio = (inicio + fim) // 2

    if lista[meio] == x:
        print(f"{x} foi encontrado na posição {meio}. Foram feitas {cont} verificações.")
        leftIndex = rightIndex = meio

        cont2 += 1

        cont += 1
        while lista[leftIndex - 1] == x:
            print(f"{x} foi encontrado na posição {leftIndex - 1}. Foram feitas {cont} verificações.")
            leftIndex = leftIndex - 1
            cont2 += 1

        cont += 1
        while lista[rightIndex + 1] == x:
            print(f"{x} foi encontrado na posição {rightIndex + 1}. Foram feitas {cont} verificações.")
            rightIndex = rightIndex + 1
            cont2 += 1
        cont += 1
        break

    elif lista[meio] < x:
        inicio = meio + 1

    else:
        fim = meio - 1

if cont2 == 0:
    print(f"{x} não foi encontrado na lista.")
else:
    print(f"Total de ocorrências de {x}: {cont2}.")
    print(f"Foram feitas {cont} verificações no total.")
