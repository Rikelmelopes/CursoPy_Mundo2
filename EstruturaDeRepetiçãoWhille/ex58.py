#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai tentar
#  adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer

from random import randint

computador = randint(0 , 10)
print("Sou seu compitador ... Acabei de pensar em um numero de 0 a 10.")
print("Será que voce consegue adivinhar? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Diz qual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente novamente. ")
        elif jogador > computador:
            print("Menos...Tente novamente. ")
print("Acertou com {} tentativas".format(palpites))