print("""Bem-vindo ao Unesc Saúde   
      """)
nome_do_paciente: str = input("Digite seu nome: ")
altura_do_paciente: float = float(input("Digite sua altura: "))
peso_do_paciente: float = float(input("Digite seu peso: "))
imc_do_paciente = peso_do_paciente / (altura_do_paciente * altura_do_paciente) 

continue_menu = True
while continue_menu == True :
    print("""MENU
        1 - Calcular IMC
        2 - Calcular Taxa Metabólica Basal
        3 - Sair""")
    opcao_desejada = int (input("Digite a opção desejada: "))

    if opcao_desejada == 1:
        print(f"Seu IMC é {imc_do_paciente}")
        print('Obrigado')
    elif opcao_desejada == 2:
        print("Taxa Metabólica Basal") 
    elif opcao_desejada == 3:
        print("Obrigado por usar o Unesc Saúde.")
        continue_menu = False
    else:
        print('Opção inválida.')