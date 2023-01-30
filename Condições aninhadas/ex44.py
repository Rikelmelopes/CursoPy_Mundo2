#Elabore um programa que calcule o valor a ser pago por um 
# produto, considerando o seu preço normal e condição de 
# pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

preço = float(input("Digite o valor do produto :R$"))

print('''FORMAS DE PAGAMENTO
[1]dinheiro/Cheque
[2]à vista no cartão
[3]em até 2x no cartão
[4]3x ou mais no cartão
''')
opção = int(input("Sua opção : "))

if opção == 1:
    op1 = preço - (preço * 10 / 100)
    print("Sua compra de R${:.2f} vai sair por R${:.2f}".format(preço,op1))

elif opção ==2:
     op1 = preço - (preço * 5 / 100)
     print("Sua compra de R${:.2f} vai sair por R${:.2f}".format(preço,op1))

elif opção == 3:
    op1 = preço / 2
    print("R${:.2f} em 2x sai sem juros e fica R${:.2f} por mes".format(preço,op1))

elif opção == 4:
    op1 = preço + (preço * 20 / 100)
    QuantParcelas = int(input("quantidade de parcelas :"))
    CalculoParcelas = op1 / QuantParcelas
    print("sua compra será parcelada em {} parcelas de {:.2f}".format(QuantParcelas,CalculoParcelas))
    print("Sua compra de R${:.2f} vai custar no final R${:.2f}".format(preço,op1))

else:
    opção = 0
    print("Forma de pagamento invalida , Tente novamente !!!!")




