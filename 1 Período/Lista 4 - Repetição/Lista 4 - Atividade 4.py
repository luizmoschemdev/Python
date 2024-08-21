num = int(input("Digite um número: "))
numCalc = num
fatorial = 1
print("Fatorial de:", num)
while (numCalc > 0):
        fatorial = fatorial * numCalc
if (numCalc > 1):
    print(num, ".", numCalc)
else:
    print(numCalc)
numCalc = numCalc - 1
print("Resultado Fatorial de", num, "=", fatorial)
