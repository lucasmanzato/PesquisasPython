import random

def SeqSimples(lista, x):
    cont = 0
    for posicao, aux in enumerate(lista):
        
        if aux == x:
            print(f"Valor {x} encontrado na posição {posicao}.")
            print(f"foram feitas {cont} verificações para encontrar o valor.")
            break

    else:
        print(f"Valor não encontrado na lista.")

def SeqCompleta(lista, x):
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

def BinSimples(lista, x):
  
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
        print(f"{x} não foi encontrado na lista. Foram feitas {cont} verificações.")

def BinCompleta(lista, x):

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

def default():
    print("Opção inválida!")

def main():
    lista = [random.randint(1, 100) for _ in range(100)]

    print(lista)  # Para verificar se está correto
    print('------------------------------------------------------------------------------')
    opc = int(input("Qual tipo de Busca deseja realizar: \n 1- Sequencial Simples \n 2- Sequencial Completa \n 3- Binária Simples \n 4- Binária Completa \n Digite o número da opção desejada: "))
    if opc == 3 or opc == 4:
        lista.sort()
        print(lista)  # Para verificar se está correto
        print
            
    x = int(input("Qual valor deseja buscar? "))
    
    if opc == 1:
        SeqSimples(lista, x)
    elif opc == 2:
        SeqCompleta(lista, x)
    elif opc == 3:
        BinSimples(lista, x)
    elif opc == 4:
        BinCompleta(lista, x)    
    else:
        default()

main()
