#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso 
# de mostrar que tipo de triângulo será formado

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo!!')

    if r1 == r2 == r3: # ou a == b and b == c:
        print('Triângulo Equilatero')

    elif  r1 != r2 != r3 != r1:  #ou a != b and b != c and c != a:
        print('Triângulo escaleno')
    else:
        print("Isôseles")
else:
    print("Os segmentos acima não pode formar um triangulo")