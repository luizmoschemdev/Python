import random
def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
        return True
numero_aleatorio = random.randint(1, 100)
if eh_primo(numero_aleatorio):
    print(f"O número {numero_aleatorio} é primo.")
else:
    print(f"O número {numero_aleatorio} não é primo.")do