#Sistema de nota da Unesc

n1 = float (input("Digite a nota do primeiro bimestre: "))
n2 = float (input("Digite a nota do segundo bimestre: "))
tp = float (input("Digite a nota do teste de progresso: "))

media = (n1 * 4) + (n2 * 4) + (tp * 2)


if media >= 70:
    print ("Aprovado.")
if media  > 35 < 70:
    print ("Você está de recuperação final.")
if media <= 35:
    print ("Reprovado.")
if media  > 35 < 70:
    neer = float (input("Digite sua nota do EER: "))
eer =  (media + neer) /2
if neer >= 120:
    print ("Aprovado.")
if neer < 120:
    print ("Reprovado.")