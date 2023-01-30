#Faça um programa que leia um número inteiro e diga se ele é 
#ou não um número primo

numero = int(input("informe um numero : "))
total = 0
for c in range(1 , numero + 1):
    if numero % c == 0:
        print("\033[33m" , end= " ")
        total = total + 1
    else:
        print("\033[31m",end= " ")
    print("{}".format(c), end=" ")
print("\n\033[O numero {} foi divisivel {} vezes".format(numero,total))
if total == 2:
    print("Primo")
else:
    print("Não é primo")
