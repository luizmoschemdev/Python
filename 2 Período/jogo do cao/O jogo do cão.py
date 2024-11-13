import os

class Dog: 
    def __init__(self, name, breed):
        self.is_on = False
        self.name = name
        self.breed = breed
        self.hunger = 0
        self.tire = 0

    def dog_creation(self):
                self.name = input("Digite o nome do seu cachorro:")
                self.breed= input("Qual a raça do seu cachorro? ")     

    def wake_up(self):
        if not self.is_on:
            self.is_on = True
            print (f"Você acordou o {self.name}! e ele está pronto para brincar")
        else: 
            print (f"Você já acordou o {self.name}")

    def play_dog (self):
        try:
            if self.is_on:
                option_play = int (input(f"O {self.name} quer brincar! Pressione 1"))
                if option_play == 1:
                    print (f"Você jogou a bola e o {self.name} buscou para você.") 
                    self.hunger += 1
                    self.tire += 1                  
                    if self.hunger == 6:
                        print ("FIM DE JOGO")
                        print (f"O {self.name} ficou com muita fome e morreu :(")
                    elif self.hunger == 4:
                        print (f"Seu pet está começando a ficar com fome! Alimente ele para não morrer.")
                    if self.tire == 5:
                        print (f"O {self.name} cansou muito e dormiu.") 
                        self.tire = 0        
            else: 
                print (f"O {self.name} está dormindo, acorde ele para brincar!") 
        except ValueError:
            print ("Caracteres inválidos, digite um caractere válido.")      

    def food(self):
        try:
            fooding = int (input("Pressione 1 para poder dar um petisco para seu pet"))
            if fooding == 1:
                print(f"Você alimentou o {self.name}.")
                self.hunger -= 2
                self.hunger = max(0, self.hunger - 2) #isso previne que a fome caia abaixo de 0
        except ValueError:
            print ("Caracteres inválidos, digite um caráctere válido.")  

    def show_stat(self):
        print(f""" 
        Nome: {self.name} 
        Raça: {self.breed}
        Fome: {self.hunger} 
        Cansaço: {self.tire}
        """)          
                

def return_back_menu():
    input("Pressione Enter para voltar ao menu...")
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
6. Estatisticas 
7. Sair
        """)
        option = int (input("Escolha uma opção: "))
        match option:
            case 1:
                os.system('cls')
                print ("""
Leia as regras com atenção!
1. Você precisa de dar um nome e indicar a raça do cachorro para poder jogar, use o menu de criação.
2. Fique atento com a fome do seu cachorro, cada vez que você brinca ele vai ficando faminto até chegar o ponto de morrer.
3. Você pode evitar a morte do seu cachorro alimentando ele na seção de alimentação.
                """)
                menu_loop = return_back_menu()
            case 2:
                dog_creation()
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
                    os.system('cls')   
            case 7: 
                print("Obrigado por jogar o Jogo do Cão!")
                menu_loop = False
            case _:
                print ("Opção inválida.")               
menu()

                        


