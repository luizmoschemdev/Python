def calculator():

    op = int(input("Escolha a operação 1. SOMA 2. SUBTRAÇÃO 3. MULTIPLICAÇÃO 4. DIVISÃO "))
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

    