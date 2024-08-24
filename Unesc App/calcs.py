def calc_square ():
    alt_square = float ("Digite a altura do seu quadrado: ")
    area_square = alt_square * alt_square
    print(f"A área de seu quadrado é: {area_square}.")

def calc_circle ():
    ray_circle = float ("Digite o raio do seu círculo: ")
    area_circle = 3.14 * (ray_circle * ray_circle)
    print (f"A área de seu cícrulo é: {area_circle}.")

def calc_trangle ():
    base = float ("Digite a altura do seu triângulo: ")
    alt = float ("Digite a altura do seu triângulo: ")
    area_triangle = (base *  alt) / 2
    print (f"A área de seu triângulo é: {area_triangle}")

def calc_cilinder ():
    ray_cilinder = float ("Digite o raio do seu cilindro: ")
    alt_cilinder = float ("Digite a altura do seu cilindro: ")
    vol_cilinder = 3.14 * alt_cilinder * (ray_cilinder * ray_cilinder)
    print (f"O volume do seu cilindro é: {vol_cilinder}.")