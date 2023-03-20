n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n #esta somando os numeros digitados
#print("A soma vale {}".format(s))
print(f"A soma vale {s}") #ultilização de f string