#Desenvolva uma lógica que leia o peso e a altura de uma 
#pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre 
#seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
nome = str(input("Digite seu nome : "))
altura = float(input("Digite seu altura : (M) "))
peso = float(input("Digite seu sua peso : (Kg) "))

imc = peso / (altura * altura)
print("{} ,O seu IMC é de {:.2f}".format(nome , imc))
if imc < 18.5:
    print("E ESTA ABAIXO DO PESO")
elif imc > 18.5 and imc <= 25:
    print("E ESTA NO PESO IDEAL")
elif imc > 25 and imc <= 30:
    print("E ESTA SOBREPESO")
elif imc > 30 and imc <= 40:
    print("E ESTA EM OBESIDADE")
else:
    print("OBESIDADE MORBIDA")