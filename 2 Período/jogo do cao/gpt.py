class Dog: 
    def __init__(self, name):
        self.is_on = False
        self.name = name
        self.hunger = 0
        self.tire = 0

    def wake_up(self):
        if not self.is_on:
            self.is_on = True
            print(f"Você acordou o {self.name}! Ele está pronto para brincar.")
        else: 
            print(f"Você já acordou o {self.name}.")

    def play_dog(self):
        if self.is_on:
            option_play = int(input(f"O {self.name} quer brincar! Pressione 1: "))
            if option_play == 1:
                print(f"Você jogou a bola e o {self.name} buscou para você.") 
                self.hunger += 1
                self.tire += 1                  
                if self.hunger >= 6:
                    print("FIM DE JOGO")
                    print(f"O {self.name} ficou com muita fome e morreu :(")
                elif self.hunger == 4:
                    print(f"Seu pet está começando a ficar com fome! Alimente ele para não morrer.")
                if self.tire >= 5:
                    print(f"O {self.name} cansou muito e dormiu.") 
                    self.tire = 0        
        else: 
            print(f"O {self.name} está dormindo, acorde ele para brincar!") 

    def food(self):
        fooding = int(input("Pressione 1 para dar um petisco para seu pet: "))
        if fooding == 1:
            print(f"Você alimentou o {self.name}.")
            self.hunger = max(0, self.hunger - 2)  # Previna fome abaixo de 0

def return_back_menu():
    return_menu = input("Deseja voltar ao menu? (s/n): ").upper()
    if return_menu in {"S", "SIM"}:
        return True
    elif return_menu in {"N", "NÃO", "NAO"}:
        print("Obrigado por jogar o Jogo do cão!")
        return False
    else:
        print("Opção inválida, voltando ao menu.")
        return True

def menu():
    dog1 = None
    menu_loop = True
    while menu_loop:
        print("""
Bem vindo ao jogo do cão!
1. Regras e dicas
2. Crie seu pet
3. Acordar seu pet
4. Brincar com seu pet
5. Alimentar seu pet 
6. Sair
        """)
        option = int(input("Escolha uma opção: "))
        match option:
            case 1:
                print("""
Leia as regras com atenção!
1. Você precisa dar um nome e indicar a raça do cachorro para poder jogar.
2. Fique atento com a fome do seu cachorro; brincar aumenta a fome até ele morrer.
3. Evite a morte do seu cachorro alimentando-o regularmente.
                """)
            case 2:
                dog1 = Dog(input("Digite o nome do seu cachorro: "))
            case 3: 
                if dog1:
                    dog1.wake_up()
                else:
                    print("Você precisa criar um cachorro primeiro.") 
            case 4:
                if dog1:
                    dog1.play_dog()
                    menu_loop = return_back_menu()
                else:
                    print("Você precisa criar um cachorro primeiro.") 
            case 5: 
                if dog1:
                    dog1.food()
                    menu_loop = return_back_menu()
                else:
                    print("Você precisa criar um cachorro primeiro.") 
            case 6: 
                print("Obrigado por jogar o Jogo do Cão!")
                menu_loop = False
            case _:
                print("Opção inválida.")

# Inicia o jogo
menu()
