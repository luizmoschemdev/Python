from calcs import calc_square, calc_circle, calc_trangle, calc_cilinder

def welcome ():
    print("""Bem vindo ao Unesc App!
          """)

def return_menu ():
    back__menu = input("Deseja retornar ao menu principal? (S/N): ").upper()
    match back__menu:
        case "S" | "s":
            return True
        case "N" | "n":
            print ("Obrigado por usar o Unesc app!")
            return False
        

def show_menu (): 
    go_back_menu = True
    while go_back_menu == True :  
        print ("""MENU
                1 - Calcular área de um quadrado
                2 - Calcular área de um círculo
                3 - Calcular área de um triângulo
                4 - Calcular área de um cilindro
                5 - Sair""")
        option = int (input("Escolha uma opção. "))

        match option:
            case 1: 
                calc_square()
                go_back_menu = return_menu()
            case 2:
                calc_circle()
                go_back_menu = return_menu()
            case 3:
                calc_trangle()
                go_back_menu = return_menu()
            case 4: 
                calc_cilinder()
                go_back_menu = return_menu()
            case 5:
                print ("Obrigado por usar o Unesc app!")
                go_back_menu = False
            case _:
                  print ("Opção inválida.")             
                
            

            
      