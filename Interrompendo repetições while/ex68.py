'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador 
perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
v = 0
print(12*'==')
print('JOGO DO PAR OU IMPAR')
print(12*'==')

while True: 
    numero = int(input('Escreva um valor: '))
    computador = randint( 0, 10 )
    total = numero + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ìmpar?[P/I] ')).strip().upper()[0]
    print(f'voce jogou {numero} e a maquina jogou {computador}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar de novo......')
print(f'Game over!!Voce ganhou {v} vezes')
        
        
    