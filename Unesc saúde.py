print("Bem vindo ao UNESC saúde")
print ("""MENU
       1 - Calcular IMC
       2 - Calcular Taxa metabólica Basal
       3 - Sair """)
opcao = int  (input("Digite a opção desejada: "))

if opcao == 1:
    alt_paciente = float (input("Digite sua altura: "))
    peso_paciente =  float (input("Digite seu peso: "))
    imc = peso_paciente / (alt_paciente **2)
    print(f"Seu IMC é: {imc:.2f}")
elif opcao == 2:
    print("Taxa metabólica")
elif opcao == 3:
    print("Obrigado por usar o UNESC saúde!")
else:
    print("Erro")