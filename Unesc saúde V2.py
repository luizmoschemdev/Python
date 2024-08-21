#Aplicativo Unesc Saúde | Atividade de Aula
from calcs import calcular_imc, calcular_taxa_basal
from menu import retorno_menu
print("""Bem-vindo ao Unesc Saúde   
            """)
nome_do_paciente: str = input("Digite seu nome: ")
altura_do_paciente = float(input("Digite sua altura: "))
peso_do_paciente = float(input("Digite seu peso: "))
idade_do_paciente = int(input("Digite sua idade (em anos): "))
genero_biologico = input("Digite seu gênero biológico (M/F): ").upper()#coloca todas as letra em maiusculo

def mostrar_menu() :                           
         
    voltar_ao_menu = True
    while voltar_ao_menu == True :
        print("""MENU
                        1 - Calcular IMC
                        2 - Calcular Taxa Metabólica Basal
                        3 - Sair""")
        opcao_desejada = int (input("Digite a opção desejada: "))

        match opcao_desejada :
            case 1 :
                calcular_imc
                retorno_menu
                voltar_ao_menu = retorno_menu()

            case 2 :
                calcular_taxa_basal
                retorno_menu
                voltar_ao_menu = retorno_menu()

            case 3 :
                    print('Obrigado por utilizar o Unesc Saúde.')
                    voltar_ao_menu = False
            case _:
                    print('Opção inválida.')
