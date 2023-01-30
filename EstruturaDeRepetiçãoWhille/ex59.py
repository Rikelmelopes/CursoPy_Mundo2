#Crie um programa que leia dois valores e mostre um menu na 
#tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada 
#caso.
from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print('''===NOSSAS OPÇÕES===
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA
    ''')
    opção = int(input("Sua opção? "))
    if opção == 1:
        soma = n1 + n2
        print("A soma entra {} e {} é igual a {}".format(n1,n2,soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print("{} X {} é igual a {}".format(n1,n2,multiplicação))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("entre {} e {} o maior numero é {}".format(n1,n2,maior))

    elif opção == 4:
        print("Digite a baixo os novos numeros: ")
        n1 = int(input("Primeiro numero: "))
        n2 = int(input("Segundo numero: "))
    elif opção == 5:
        print("Finalizando ...")
        sleep(2)
    else:
        print('Opção invalida...Tente novamente')
    print('-=-=-'*10)
print("Fim do programa ... volte sempre")



