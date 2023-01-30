#Faça um programa que mostre na tela uma contagem regressiva 
#para o estouro de fogos de artifício, indo de 10 até 0, 
#com uma pausa de 1 segundo entre eles

from time import sleep

print("Vai começar a contagem para os fogos de artificio (-__-)")
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print("POWWWWWWWWWWWWWWW")
sleep(1)
print("POWWWWWWWWWWWWWWW")
sleep(1)
print("POWWWWWWWWWWWWWWW")
sleep(1)
print("POWWWWWWWWWWWWWWW")
sleep(1)
print("POWWWWWWWWWWWWWWW")
sleep(1)
print("POWWWWWWWWWWWWWWW")