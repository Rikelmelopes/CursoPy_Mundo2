from datetime import date

atual = date.today().year
nascimento = int(input("Seu ano de nascimento : "))
idade = atual - nascimento
print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <= 19:
    print("JUNIOR")
elif idade > 19 and idade <= 20:
    print("SENIOR")
else:
    print("MASTER")

'===================================================================================='

from datetime import date

atual = date.today().year
nascimento = int(input("Seu ano de nascimento : "))
idade = atual - nascimento
print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SENIOR")
else:
    print("MASTER")