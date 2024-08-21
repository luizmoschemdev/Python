from calcs import calcular_imc, calcular_taxa_basal

def boas_vindas() :
    print("""Bem-vindo ao Unesc Saúde   
            """)


def retorno_menu ():
        escolha_menu = input('Deseja voltar ao menu anterior? (s/n): ').upper()
        if escolha_menu != "S" :
                    print('Obrigado por utilizar o Unesc Saúde.')
                    return False
        else :
                    return True
        
def mostrar_menu(altura_do_paciente, peso_do_paciente, idade_do_paciente, genero_biologico):               
        voltar_ao_menu = True
        while voltar_ao_menu == True :
            print("""MENU
                1 - Calcular IMC
                2 - Calcular Taxa Metabólica Basal
                3 - Sair""")
            opcao_desejada = int (input("Digite a opção desejada: "))

            match opcao_desejada :
                case 1: 
                    calcular_imc(peso_do_paciente, altura_do_paciente)
                    voltar_ao_menu = retorno_menu()
                case 2: 
                    altura_em_centimetros = altura_do_paciente * 100
                    calcular_taxa_basal(peso_do_paciente, altura_em_centimetros, idade_do_paciente, genero_biologico)
                    voltar_ao_menu = retorno_menu()
                case 3 :
                    print('Obrigado por utilizar o Unesc Saúde.')
                    voltar_ao_menu = False
                case _:
                    print('Opção inválida.')
                    