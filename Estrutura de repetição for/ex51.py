#Desenvolva um programa que leia o primeiro termo e a razão 
#de uma PA. No final, mostre os 10 primeiros termos dessa 
#progressão

'''primeiro = int(input("Primeiro elemento : "))
razão = int(input("Razão : "))

ultimo = primeiro + (10 - 1) * razão
ultimo = ultimo + 1

for c in range(primeiro , ultimo , razão):
    print(c)'''

primeiro = int(input("Primeiro elemento : "))
razão = int(input("Razão : "))
decimo = primeiro + (10 - 1) * razão
ultimo = decimo + 1
for c in range(primeiro , ultimo , razão):
    print("{}".format(c),end=" -> ")
print("ACABOU")



