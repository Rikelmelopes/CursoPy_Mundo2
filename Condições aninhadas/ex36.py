#Escreva um programa para aprovar o empréstimo bancário para 
#a compra de uma casa. Pergunte o valor da casa, o salário 
#do comprador e em quantos anos ele vai pagar. A prestação 
#mensal não pode exceder 30% do salário ou então o empréstimo
#será negado

ValorCasa = float(input("Digite o valor da casa : R$"))
Salario = float(input("Digite o valor de seu salario : R$"))
Qanos = int(input("Em quantos anos voce quer pagar :"))

meses = Qanos * 12
prestação = ValorCasa / meses

if prestação > Salario * 0.3:
    print("Imprestimo não aprovado")
else:
    print("O valor da prestação ficou R${: .2f}".format(prestação))

