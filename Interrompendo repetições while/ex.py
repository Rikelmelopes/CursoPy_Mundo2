'''n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n #esta somando os numeros digitados
#print("A soma vale {}".format(s))
print(f"A soma vale {s}") #ultilização de f string'''

'''total18 = homensC = mulheres20 = 0
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
print(f'Um total de {total18} pessoas tem mais de 18 anos')
print(f'Um total de {homensC} homens foram cadastrados')
print(f'Um total de {mulheres20} mulheres com menos de 20 anos foram cadastradas')'''
