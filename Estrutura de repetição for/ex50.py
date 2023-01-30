#Desenvolva um programa que leia seis números inteiros e mostre 
#a soma apenas daqueles que forem pares. Se o valor digitado 
#for ímpar, desconsidere-o

soma = 0
contador = 0
for c in range(1 , 7):
    num = int(input("Digite o {} valor : ".format(c)))
    if num % 2  == 0:
        soma = soma + num
        contador = contador = 1
print('Voce informou {} numeros e a soma dos numeros pares igual a : {}'.format(c,soma))   

