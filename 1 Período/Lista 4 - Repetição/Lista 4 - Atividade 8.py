def calcular_quadrados_e_cubos():
    quadrados = []
cubos = []
for i in range(101):
    quadrado = i ** 2
cubo = i ** 3
quadrados.append(quadrado)
cubos.append(cubo)
return quadrados, cubos
quadrados, cubos = calcular_quadrados_e_cubos()
    print("Quadrados dos números de 0 a 100:")
    for i in range(len(quadrados)):
        print(f"{i}: {quadrados[i]}")
        print("\nCubos dos números de 0 a 100:")
    for i in range(len(cubos)):
        print(f"{i}: {cubos[i]}")