import random
def inverter_lista(lista):
    return lista[::-1]
tamanho_lista = int(input("Digite o tamanho da lista de números: "))
numeros = [random.randint(1, 100) for _ in range(tamanho_lista)]
print("Lista original:", numeros)
numeros_invertidos = inverter_lista(numeros)
print ("Lista invertida:", numeros_invertidos”)