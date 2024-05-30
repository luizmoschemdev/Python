operacoes = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        operacoes += 1
print("Total de operações realizadas:", operacoes)
