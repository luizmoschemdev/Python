from calcs import calculator, money_convertor, task_list

def welcome ():
    print ("Bem vindo ao aplicativo multitarefas.")

def return_menu():
    back_menu = input("Deseja voltar ao menu principal? S/N ")
    match back_menu:
        case "s" | "S":
            return True
        case "N" | "n":
            return False
    
def show_menu():
    go_back_menu = True
    while go_back_menu == True:
       print ("""Menu
               1. Calculadora
               2. Conversor de moedas
               3. Lista de tarefas
               4. Jogo do número aleatório
               """)
       op = int (input("Escolha uma opção. "))
    match op:
        case 1:
            calculator()
            go_back_menu = return_menu()
        case 2:
            money_convertor()
            go_back_menu = return_menu()
        case 3:
            task_list()
            go_back_menu = return_menu()
        case 4:
            print ("ta pronto n bb")
            go_back_menu = return_menu()
        case _:
            print ("Opção inválida")
