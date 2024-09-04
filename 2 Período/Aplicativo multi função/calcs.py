def calculator():

    print("Escolha a operação 1. SOMA 2. SUBTRAÇÃO 3. MULTIPLICAÇÃO 4. DIVISÃO ")
    op = int (input("Selecione a operação"))

    match op :
        case 1:
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (n1 + n2) 
        case 2: 
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (n1 - n2) 
        case 3:
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (n1 * n2) 
        case 4:
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (n1 / n2) 

def money_convertor():

    (print("""MENU
            1. Para converter em dólar
            2. Para converter em euro
            """)) 
    option = int (input("Escolha uma opção."))
    match option :
                case 1 :
                    brazilian_coin = float (input("Quantos reais você tem? "))
                    print(f"sua conversao é {brazilian_coin / 5.65} USD")
                case 2 :
                    brazilian_coin = float (input("Quantos reais você tem? "))
                    print(f"sua conversao é {brazilian_coin / 6.23} EU")

def task_list ():
    
    tasks = []
    tasks.append (input("Digite as suas tarefas"))
    print (tasks)
    add_task = True
    while add_task == True:
        adc = float (input("Deseja adicionar mais um elemento?"))
        match adc:
            case 1:
                tasks.append (input("Digite as suas tarefas"))
                print (tasks)
            case 2: 
                print ("Obrigado por usar o sistema de lista")
                add_task = False

def secretNumber():
    import random

    number = random.randint(1, 100)
    attempts = 0
    
    print("Bem-vindo ao jogo do Número Secreto!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")
    
    while True:
        guess = int(input("Digite o seu palpite: "))
        attempts += 1
        
        if guess < number:
            print("Muito baixo! Tente novamente.")
        elif guess > number:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número secreto {number} em {attempts} tentativas.")
            break
