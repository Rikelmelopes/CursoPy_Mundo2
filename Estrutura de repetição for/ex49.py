#Refaça o DESAFIO 9, mostrando a tabuada de um número que o 
#usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite o numero : "))
for tabuada in range(0 , 11):
    print("{} X {} = {} ".format(numero,tabuada,numero*tabuada))

'''numero = int(input("Digite o numero : "))
for tabuada in range(0 , 11):
    multiplicação = numero * tabuada
    print("{} X {} = {} ".format(numero,tabuada,multiplicação))'''
    