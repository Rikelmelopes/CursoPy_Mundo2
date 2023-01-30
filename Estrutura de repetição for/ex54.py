#Crie um programa que leia o ano de nascimento de sete pessoas
#.No final, mostre quantas pessoas ainda não atingiram a 
#maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for c in range(1 ,8):
    ano = int(input("Digite o ano de nascimento : "))
    idade = atual - ano
    if idade >=18:
        totalMaior = totalMaior + 1
    else:
        totalMenor = totalMenor + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totalMaior))
print("e tambem tivemos {} pessoas menores de idade".format(totalMenor))