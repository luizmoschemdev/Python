#Aplicativo Unesc Saúde | Atividade de Aula
print("""Bem-vindo ao Unesc Saúde   
      """)
nome_do_paciente = str (input("Digite seu nome: "))
altura_do_paciente = float(input("Digite sua altura: "))
peso_do_paciente = float(input("Digite seu peso: "))
idade_do_paciente = int(input("Digite sua idade (em anos): "))
genero_biologico = input("Digite seu gênero biológico (M/F): ").upper() #qualquer coisa digitada vai ficar em maiusculo

voltar_ao_menu = True
while voltar_ao_menu == True :
    print("""MENU
        1 - Calcular IMC
        2 - Calcular Taxa Metabólica Basal
        3 - Sair""")
    opcao_desejada = int (input("Digite a opção desejada: "))

    match opcao_desejada :
        case 1 :
            imc_do_paciente = peso_do_paciente / (altura_do_paciente * altura_do_paciente) 
            print(f"Seu IMC é {imc_do_paciente:.2f}")
            escolha_menu = input('Deseja voltar ao menu anterior? (s/n): ').upper()
            if escolha_menu != "S " :
                print('Obrigado por utilizar o Unesc Saúde.')
                voltar_ao_menu = False
            else :
                voltar_ao_menu = True             
        
        case 2 :
            altura_em_centimetros = altura_do_paciente * 100
            match genero_biologico :
                case "M" | "m" | "Masculino":
                    tmb = 66 + (13.7 * peso_do_paciente) + (5 * altura_em_centimetros) - (6.8 * idade_do_paciente) 
                    print(f"Sua Taxa Metabólica Basal é {tmb} calorias.") 
                case "F" | "f" | "Feminino" :
                    tmb = 665 + (9.6 * peso_do_paciente) + (1.8 * altura_em_centimetros) - (4.7 * idade_do_paciente)
                    print(f"Sua Taxa Metabólica Basal é {tmb} calorias.")
                case _:
                    print("Você não digitou corretamente seu gênero.\nNão podemos calcular o TMB.")
            escolha_menu = input('Deseja voltar ao menu anterior? (s/n): ').upper()
            if escolha_menu != "S" :
                print('Obrigado por utilizar o Unesc Saúde.')
                voltar_ao_menu = False
            else :
                voltar_ao_menu = True 
        case 3 :
            print('Obrigado por utilizar o Unesc Saúde.')
            voltar_ao_menu = False
        case _:
            print('Opção inválida.')
            