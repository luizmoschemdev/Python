maior = 0
menor = 10
nmaior = 0
nmenor = 0
i = 0

while (i < 10):
    num = int(input('Digite o número do aluno: '))
    alt = float(input('Digite a altura do aluno em metros: '))
    
    if (alt > maior):
        maior = alt
        nmaior = num

    if (alt < menor):
        menor = alt
        nmenor = num
    
    i += 1

print('O número do aluno com a maior altura é: %d, com %.2f m' % (nmaior, maior))
print('O número do aluno com a menor altura é: %d, com %.2f m' % (nmenor, menor))



