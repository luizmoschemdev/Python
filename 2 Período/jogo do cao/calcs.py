def wake_up(self):
        if not self.is_on:
            self.is_on = True
            print (f"Você acordou o {self.name}! e ele está pronto para brincar")
        else: 
            print (f"Você já acordou o {self.name}")

def play_dog (self):
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

def food(self):
    fooding = int (input("Pressione 1 para poder dar um petisco para seu pet"))
    if fooding == 1:
        print(f"Você alimentou o {self.name}.")
        self.hunger -= 2
        self.hunger = max(0, self.hunger - 2) #isso previne que a fome caia abaixo de 0
