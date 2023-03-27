'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

'''
ValorTotal = 0
maisde1000 = 0
menor = 0
cont = 0
barato = ''

while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço do produto: '))
    cont += 1
    
    ValorTotal += preço
    
    if preço > 1000:
        maisde1000 += 1
        
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar:[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:_^40}'.format('COMPRA FINALIZADA'))
print(f'O valor total de sua compra foi de R${ValorTotal :.2f}')
print(f'Um total de {maisde1000} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
