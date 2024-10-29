#programa de devisao
try:
    a = float (input("Digite um numero:"))
    b = float (input("Digite um numero:"))
    c = a/b
    print(f"seu resultado é {c}")
except KeyboardInterrupt:
    print ("Tu não quis digitar número mané")
except (ValueError, TypeError):
    print("Digita um numero normal porra")
except Exception as erro:
    print(f"o erro encontrado foi {erro.__cause__}")
except ZeroDivisionError:
    print ("Nois n divide zero nao animal")
finally:
    print ("Valeu por usar o programa")

def obter_nome():
    while True:
        nome = input("Digite seu nome: ")
        if nome.isalpha():
            return nome
        else:
            print("Nome inválido. Digite apenas letras.")

nome_usuario = obter_nome()
print("Olá,", nome_usuario + "!")