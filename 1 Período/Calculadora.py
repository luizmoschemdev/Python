#calculadora em python#

op = int(input("Escolha a operação 1. SOMA 2. SUBTRAÇÃO 3. MULTIPLICAÇÃO 4. DIVISÃO 5. PORCENTAGEM "))

if op == 1:
    n1 = float (input("Digite um número: "))
    n2 = float (input("Digite um número: "))
    print (n1 + n2) 
    
if op == 2:
    n1 = float (input("Digite um número: "))
    n2 = float (input("Digite um número: "))
    print (n1 - n2) 

if op == 3:
    n1 = float (input("Digite um número: "))
    n2 = float (input("Digite um número: "))
    print (n1 * n2) 

if op == 4:
    n1 = float (input("Digite um número: "))
    n2 = float (input("Digite um número: "))
    print (n1 / n2) 
if op == 5:
    n1 = float (input("Digite um número: "))
    n2 = float (input("Digite a porcentagem: "))
    print (n1 * n2 / 100) 

