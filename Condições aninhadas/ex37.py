#Escreva um programa em Python que leia um número inteiro 
# qualquer e peça para o usuário escolher qual será a base 
# de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal

numero = int(input("Digite um numero inteiro : "))
print('''escolha umas das bases de converção
[1]Binário
[2]Octal
[3]Hexadecimal''')
opção = int(input("Sua opção : "))
if opção == 1:
    print("O {} convertido em binário é igual a :{}".format(numero,bin(numero)[2:]))
elif opção == 2:
    print("O {} convertido em octal é igual a :{}".format(numero,oct(numero)[2:]))
elif opção == 3:
    print("O {} convertido em hexadecimal é igual a :{}".format(numero,hex(numero)[2:]))
else:
    print("Opção invalida , Tente novmente !!")

