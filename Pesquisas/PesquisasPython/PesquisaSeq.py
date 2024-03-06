import random

lista = [random.randint(1, 100) for _ in range(100)]

print(lista)  

x = int(input("Qual valor deseja buscar? "))
cont = 0
for posicao, aux in enumerate(lista):
    
    if aux == x:
        print(f"Valor {x} encontrado na posição {posicao}.")
        print(f"foram feitas {cont} verificações para encontrar o valor.")
        break
else:
    print(f"Valor não encontrado na lista!")

