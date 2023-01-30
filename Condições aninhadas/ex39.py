# Faça um programa que leia o ano de nascimento de um jovem e 
# informe, de acordo com a sua idade, se ele ainda vai se 
# alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa 
# também deverá mostrar o tempo que falta ou que passou do 
# prazo.

from datetime import date

nasc = int(input("Ano de nascimento : "))

atual = date.today().year
idade = atual - nasc
print("Quem nasce em {} tem {} anos em {}".format(nasc,idade,atual))
if idade == 18:
    print("Se aliste imediatamente")

elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print("Voce ainda não esta pronto, faltam {} anos para o alistamento ".format(saldo))
    print("voce devera se alistar em {}".format(ano))
    
elif idade > 18:
     saldo = idade - 18
     ano = atual - saldo
     print("Passou do prazo, Voce deveria ter se elistado há {} anos ".format(saldo))
     print("Voce deveria ter se alisrado em {}".format(ano))
    




