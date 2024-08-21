import random
def gerar_numero_aleatorio():
    return random.randint(1, 100)
def jogo_adivinhacao():
    numero_secreto = gerar_numero_aleatorio()
tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar um número entre 1 e 100.")
while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Palpite muito baixo. Tente novamente.")
    elif palpite > numero_secreto:
        print("Palpite muito alto. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")