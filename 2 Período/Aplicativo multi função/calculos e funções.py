def calculator():

    op = int (input("Escolha a operação 1. SOMA 2. SUBTRAÇÃO 3. MULTIPLICAÇÃO 4. DIVISÃO "))
    match op:
        case 1:
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (f" A soma é: {n1 + n2}") 
        case 2: 
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (f"A subtração é: {n1 - n2}") 
        case 3:
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (f"A multiplicaçãop é: {n1 * n2}") 
        case 4:
            n1 = float (input("Digite um número: "))
            n2 = float (input("Digite um número: "))
            print (f"A divisão é: {n1 / n2}") 

def money_convertor():

    option = int (print("""1. para dolar
                    2. para euro
                """))   
    match option :
            case 1 :
                brazilian_coin = float ("quantos reais você tem?")
                print(f"sua conversao é {brazilian_coin / 5.65}")
            case 2 :
                  brazilian_coin = float ("quantos reais você tem?")
                  print(f"sua conversao é {brazilian_coin / 6.23}")

def task_list ():
    tasks = []
    tasks.append (input(print("digite as suas tarefas")))
    print (tasks)
    add_task = True
    while add_task == True:
        adc = float (input(print ("deseja adicionar mais um elemento?")))
        match adc:
            case 1:
                tasks.append (input(print("digite as suas tarefas")))
                print (tasks)
            case 2: 
                print ("Obrigado por usar o sistema de lista")
                add_task = False


