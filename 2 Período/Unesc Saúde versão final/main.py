from menu import boas_vindas, mostrar_menu, coletar_dados


def main():
    boas_vindas()
    dados_paciente = coletar_dados()
    mostrar_menu()
if __name__ == "__main__":
    main()