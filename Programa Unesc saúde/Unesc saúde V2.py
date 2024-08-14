#Aplicativo Unesc Saúde | Atividade de Aula
print("""Bem-vindo ao Unesc Saúde   
      """)
nome_do_paciente: str = input("Digite seu nome: ")
altura_do_paciente = float(input("Digite sua altura: "))
peso_do_paciente = float(input("Digite seu peso: "))
idade_do_paciente = int(input("Digite sua idade (em anos): "))
genero_biologico = input("Digite seu gênero biológico (M/F): ").upper()#coloca todas as letra em maiusculo

def calcular_imc (peso_do_paciente, altura_do_paciente):
    calcular_imc = peso_do_paciente / (altura_do_paciente * altura_do_paciente)
    print (f"seu imc é {calcular_imc:2f}")

def retorno_menu ():
    escolha_menu = input('Deseja voltar ao menu anterior? (s/n): ').upper()
    if escolha_menu != "S" :
                print('Obrigado por utilizar o Unesc Saúde.')
                return False
    else :
                return True

def calcular_taxa_basal (peso_do_paciente,altura_em_centimetros, idade_do_paciente) :
    if genero_biologico == "m":
                    tmb = 66 + (13.7 * peso_do_paciente) + (5 * altura_em_centimetros) - (6.8 * idade_do_paciente) 
                    print(f"Sua Taxa Metabólica Basal é {tmb} calorias.") 
    else :
                    tmb = 665 + (9.6 * peso_do_paciente) + (1.8 * altura_em_centimetros) - (4.7 * idade_do_paciente)
                    print(f"Sua Taxa Metabólica Basal é {tmb} calorias.")
                 
voltar_ao_menu = True
while voltar_ao_menu == True :
    print("""MENU
        1 - Calcular IMC
        2 - Calcular Taxa Metabólica Basal
        3 - Sair""")
    opcao_desejada = int (input("Digite a opção desejada: "))

    match opcao_desejada :
        case 1 :
            calcular_imc = calcular_imc(peso_do_paciente, altura_do_paciente)
            escolha_menu = input('Deseja voltar ao menu anterior? (s/n): ').upper()
            voltar_ao_menu = retorno_menu()

        case 2 :
            altura_em_centimetros = altura_do_paciente * 100
            calcular_taxa_basal = calcular_taxa_basal (peso_do_paciente,altura_em_centimetros, idade_do_paciente)
            voltar_ao_menu = retorno_menu()

        case 3 :
            print('Obrigado por utilizar o Unesc Saúde.')
            voltar_ao_menu = False
        case _:
            print('Opção inválida.')
            