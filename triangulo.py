#pego os valores e transformo em int
x = int(input("Lado 1: "))
y = int(input("Lado 2: "))
z = int(input("Lado 3: "))


if x == 0 or y == 0 or z == 0: #caso algum dos inputs seja 0 não pode ser um triangulo
    print("Não pode ser um triângulo!")
else:
    if z > x + y or x > z + y or y > z + x: # 1 lado maior que a soma dos dois já não é um triangulo
        print("Não pode ser um triângulo!")
    else:
        if x == y and y == z and z == x:
            print("É um triângulo Equilátero!") # 3 lados dos mesmos tamanhos
        elif x == y or y == z or z == x:
            print("É um triângulo Isósceles!") # 2 lados iguais
        elif x != y and y != z and z != x:
            print("É um triângulo Escaleno!") # 3 lados diferentes
