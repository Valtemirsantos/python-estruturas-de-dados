
print("..........................................................................")


#Programa: Operações completas com lista em Python
#Autor: Valtemir Santos
#Descrição:
#- Lê 6 números do usuário
#- Mostra elementos, pares, ímpares
#- Calcula soma, média, maior e menor valor


dados=[]
#pedir o usuario para digitar 6 numeros.
for i in range(6):
    n=int(input("Digite um numero: "))
    dados.append(n)#adiciona o numero na lista
#mostrar a lista completa
print("A lista completa é:", dados) 
#Acessando elementos da lista.
print("O primeiro elemento é:", dados[0])
print("O último elemento é:", dados[-1])
#Percorrendo a lista com for
print("Mostrando os elementos da lista:")
for valor in dados:
    print(valor, end=' ')
#Mostrar o tamanho da lista
print("\nA lista tem", len(dados), "elementos.")
#Mostrar os numeros pares da lista
print("Os números pares da lista são:")
for valor in dados:
    if valor % 2 == 0:
        print(valor, end=' ')
#Mostrar os numeros impares da lista
print("\nOs números ímpares da lista são:")
for valor in dados:
    if valor % 2 != 0:
        print(valor, end=' ')
#Mostrar a soma dos elementos da lista
soma=sum(dados)
print("\nA soma dos elementos da lista é:", soma)
#Mostrar a média dos elementos da lista
media=soma/len(dados)
print(f'A média dos elementos da lista é: {media:.2f}')
#Mostrar o maior e o menor valor da lista
maior=max(dados)
menor=min(dados)
print("O maior valor da lista é:", maior)
print("O menor valor da lista é:", menor)
print()
#Programa principal
print("Programa finalizado.")
print(".................................................................................")