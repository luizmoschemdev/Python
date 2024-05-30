def calcular_imc(peso, altura):
    return peso / (altura ** 2)
while True:
    peso = float(input("Digite o seu peso em quilogramas: "))
    altura = float(input("Digite a sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", imc)
    continuar = input("Deseja calcular outro IMC? (s/n): ")
    if continuar.lower() != 's':
        break