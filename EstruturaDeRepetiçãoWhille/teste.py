'''c = 1 #contador começa do 1
while c < 10: #Esquanto o contador for menor que 10
    print(c)
    c = c + 1
print("FIM")'''

'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

'''numero = 1
while numero != 0:
    numero = int(input("Digite um valor: "))
print("Finalizado")'''

'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

'''r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? N/S :")).upper()
print("FIM")'''

'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

'''n = 1
par = impar = 0 
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print("Voce digitou {} numeros pares e {} numeros impares".format(par , impar))'''

'''#Faça um programa que leia o sexo de uma pessoa, mas só 
# aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a 
# digitação novamente até ter um valor correto

sexo = str(input('Sexo[M,F]: ')).upper()
while sexo not in 'mMfF':
    sexo = str(input('Digite novamente[M,F]: ')).upper()
print('sexo {} registrado com sucesso'.format(sexo))'''

#Crie um programa que leia dois valores e mostre um menu na 
#tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada 
#caso.
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
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('{} X {} = {}'.format(n1,n2,multiplicação))
    elif opção == 3:
        
        if n1 > n2:
            maior = n1 
        else:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Digite a baixo os novos numeros: ')
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
print('Programa encerrado com sucesso...Volte sempre')
    

    