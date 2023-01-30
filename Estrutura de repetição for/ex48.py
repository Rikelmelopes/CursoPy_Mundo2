#Faça um programa que calcule a soma entre todos os números 
#que são múltiplos de três e que se encontram no intervalo 
#de 1 até 500
soma = 0
contador = 0
for calculo in range(1 , 501 , 2):
    if calculo % 3 == 0:
        soma = soma + calculo
        contador = contador =1 
print("A soma de todos os {} numeros é igual a {}".format(contador,soma))
   
'''s = 0
cont = 0
for C in range(1 , 501 , 2):
    if C % 3 == 0:
        s = s + C
        cont = cont =1 
print("A soma de todos os {} numeros é igual a {}".format(cont,s))'''