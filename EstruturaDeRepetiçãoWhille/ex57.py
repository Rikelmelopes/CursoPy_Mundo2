#Faça um programa que leia o sexo de uma pessoa, mas só 
# aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a 
# digitação novamente até ter um valor correto

sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input("Valor invalido.Digite novamente[M/F]: ")).strip().upper()[0]
print("sexo {} registrado com sucesso !!!".format(sexo))
