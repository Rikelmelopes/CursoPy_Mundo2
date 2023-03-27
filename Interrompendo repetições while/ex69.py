'''

Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''
total18 = homensC = mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()[0]      
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homensC += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print(14*'==')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar:[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    print(14*'==')
print(f'Um total de {total18} pessoas tem mais de 18 anos')
print(f'Um total de {homensC} homens foram cadastrados')
print(f'Um total de {mulheres20} mulheres com menos de 20 anos foram cadastradas')



