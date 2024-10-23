import os

class Car: 
    def __init__(self, model, brand, maxspeed): #toda classe cmc com def __init__
        self.model = model
        self.brand = brand
        self.maxspeed = maxspeed
        self.is_on = False
        self.speed = 0 

    def turn_on(self):
        if not self.is_on: #caso self.is_on nao for true
            self.is_on = True
            print(f"Você ligou o {self.brand} {self.model}")
        else : 
            print(f"O {self.brand} {self.model} já está ligado.")

    def turn_off(self):
        if self.is_on == True:
            if self.speed > 0:
                print(f"O {self.brand} {self.model} está em movimento, não é possível desligar.")
            else:
                self.is_on = False
                print(f"Você desligou o {self.brand} {self.model}")          
        else:
            print(f"O {self.brand} {self.model} já está desligado.")

    def SpeedUp(self):
        if self.is_on == True:
            if self.speed < 200:
                self.speed += 10
                print(f"Acelerando o {self.brand} {self.model} esta a {self.speed} km/h.")
            else:
                print(f"O {self.brand} {self.model} está na sua velocidade máxima.")
        else:
            (f"O {self.brand} {self.model} está desligado.") 

    def SpeedDown(self):
        if self.is_on == True:
            if self.speed > 0:
                self.speed -= 10
                print(f"Freou o {self.brand} {self.model}, Agora ele está a {self.speed} km/h")
            else:
                print(f"O {self.brand} {self.model} está parado.")
        else:
            print(f"O {self.brand} {self.model} está desligado.") 

carro1 = Car("Hillux", "Toyota", 200)

def show_menu():
    print(""" 
          1. Ligar o carro
          2. Desligar o carro 
          3. Acelerar o carro
          4. Frear o carro
        """)
while True:
    show_menu()

    option = int (input("Escolha uma opção: "))
    
    match option: 
        case 1: 
            os.system('cls') #limpa o console
            carro1.turn_on()
        case 2:
            os.system('cls')
            carro1.turn_off()
        case 3:
            os.system('cls') 
            carro1.SpeedUp()
        case 4:
            os.system('cls') 
            carro1.SpeedDown()
        case _:
            print("Digite uma opção válida.")