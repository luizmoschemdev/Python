import time
def contagem_regressiva(numero):
    while numero > 0:
        print(numero)
time.sleep(1) # Espera 1 segundo
numero = 1
print("Decolagem!")
numero_inicial = int(input("Digite um número para a contagem regressiva: "))
contagem_regressiva(numero_inicial)
