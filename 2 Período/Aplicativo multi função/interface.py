from calcs import calculator, money_convertor, task_list, secretNumber

def welcome ():
    print ("Bem vindo ao aplicativo multitarefas.")

def return_menu():
    back_menu = input("Deseja voltar ao menu principal? S/N ").upper
    match back_menu:
        case "S" | "s":
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
        option = int (input("Escolha uma opção."))
        match option:
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
                secretNumber()
                go_back_menu = return_menu()
            case _:
                print ("Opção inválida")
