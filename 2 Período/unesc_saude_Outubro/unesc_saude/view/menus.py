from models.calcs import calc_bmi, calc_bmr
import os

def welcome () :
    print("Bem-vindo ao Unesc Saúde\n")

def get_info() :
    patient_info = []
    patient_info.append(input("Digite seu nome: "))
    patient_info.append(float(input("Digite sua altura: ")))
    patient_info.append(float(input("Digite seu peso: ")))
    patient_info.append(int(input("Digite sua idade (em anos): ")))
    patient_info.append(input("Digite seu gênero biológico (M/F): ").upper())
    print(patient_info)
    return patient_info

def want_comeback () :
    choice_menu = input('Deseja voltar ao menu anterior? (s/n): ').upper()
    if choice_menu != "S" :
        os.system("cls")
        print('Obrigado por utilizar o Unesc Saúde.')
        return False
    else :
        return True

def show_menu (patient_info: list) :
    back_menu = True
    while back_menu == True :
        print("""MENU
            1 - Calcular IMC
            2 - Calcular Taxa Metabólica Basal
            3 - Sair""")
        option = int (input("Digite a opção desejada: "))

        match option :
            case 1 :
                calc_bmi(patient_info)
                back_menu = want_comeback()
            case 2 :
                calc_bmr(patient_info)
                back_menu = want_comeback()
            case 3 :
                os.system("cls")
                print('Obrigado por utilizar o Unesc Saúde.')
                back_menu = False
            case _:
                print('Opção inválida.')
