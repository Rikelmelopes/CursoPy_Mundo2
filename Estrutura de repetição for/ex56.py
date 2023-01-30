#Desenvolva um programa que leia o nome, idade e sexo de 4 
#pessoas. No final do programa, mostre: a média de idade do 
#grupo, qual é o nome do homem mais velho e quantas mulheres
#têm menos de 20 anos

#CONTADORES
SomaDaIdade = 0
MediaIdade = 0
MaiorIdadeHomem = 0
NomeVelho = 0
MenorIdadeMulher = 0 

for p in range(1 , 5):
    print("{} PESSOA".format(p))
    nome = str(input("NOME : ")).strip()#Tirar espaços
    idade = int(input("IDADE : "))
    sexo = str(input("SEXO [M/F] : ")).strip()#Tirar espaços
    SomaDaIdade = SomaDaIdade + idade
    if p == 1 and sexo in 'Mm':
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if  sexo in 'Mm' and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        MenorIdadeMulher = MenorIdadeMulher + 1
MediaIdade = SomaDaIdade / 4 # dividiu pelas 4 pessoas
print("A media de idade do frupo é {}".format(SomaDaIdade))
print("O homem mais velho do grupo tem {} anos e seu nome é {}".format(MaiorIdadeHomem,NomeVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(MenorIdadeMulher))
        
