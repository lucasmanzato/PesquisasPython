import random

lista = [random.randint(1, 100) for _ in range(100)]

print(lista)  

x = int(input("Qual valor deseja buscar? "))

cont = 0
cont2 = 0

for posicao, aux in enumerate(lista):
    cont += 1

    if aux == x:
        cont2 += 1
        print(f"O valor {x} foi encontrado na posição {posicao}, com {cont} verificações.")
        
 
if cont2 > 0:
    print(f"O valor {x} apareceu {cont2} vezes na lista.")
else:
    print(f"Valor {x} não encontrado na lista.")

print(f"Foram feitas {cont} verificações no total.")
