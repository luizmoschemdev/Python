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

def return_back_menu():
    return_menu = input("Deseja voltar ao menu? (S/N)").upper()
    match return_menu:
        case "s" | "S" | "Sim" | "sIm" | "siM":
            return True
        case "n" | "N" | "Não" | "Nao" | "nao" | "nÃo" | "nÂo":
            print("Obrigado por jogar o Jogo do cão!")
            return False
        case _:
            print("Opção inválida, voltando ao menu.")
            return True