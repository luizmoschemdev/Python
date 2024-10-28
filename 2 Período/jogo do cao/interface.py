import os

def return_back_menu():
    return_menu = input("Deseja voltar ao menu? (s/n)").upper()
    match return_menu:
        case "s" | "S" | "Sim" | "sIm" | "siM":
            return True
        case "n" | "N" | "Não" | "Nao" | "nao" | "nÃo" | "nÂo":
            print("Obrigado por jogar o Jogo do cão!")
            return False
        case _:
            print("Opção inválida, voltando ao menu.")
            return True
def menu():
    dog1 = None
    menu_loop = True
    while menu_loop == True:
        print ("""
Bem vindo ao jogo do cão!
1. Regras e dicas
2. Crie seu pet
3. Acordar seu pet
4. Brincar com seu pet
5. Alimentar seu pet 
6. Sair
            """)
        option = int (input("Escolha uma opção: "))
        match option:
                case 1:
                    os.system('cls')
                    print ("""
    Leia as regras com atenção!
    1. Você precisa de dar um nome e indicar a raça do cachorro para poder jogar, use o menu de criação.
    2. Fique atento com a fome do seu cachorro, cada vez que você brinca com ele, ele ganha fica com fome, ao chegar em certo ponto ele morre.
    3. Você pode evitar a morte do seu cachorro alimentando ele na seçaõ de alimentação.1
                    """)
                case 2:
                    os.system('cls')
                    dog1 = dog (input("Digite o nome do seu cachorro:"))
                case 3: 
                    os.system('cls')
                    if dog1:
                        dog1.wake_up()
                    else:
                        print("Você precisa de criar um cachorro primeiro.") 
                case 4:
                    os.system('cls')
                    if dog1:
                        dog1.play_dog()
                        menu_loop = return_back_menu()
                    else:
                        print("Você precisa de criar um cachorro primeiro.") 
                case 5: 
                    os.system('cls')
                    if dog1:
                        dog1.food()
                        menu_loop = return_back_menu()
                    else:
                        print("Você precisa de criar um cachorro primeiro.") 
                case 6: 
                    print("Obrigado por jogar o Jogo do Cão!")
                    menu_loop = False
                case _:
                    print ("Opção inválida.")               
