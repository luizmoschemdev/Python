from menu import boas_vindas, mostrar_menu, coletar_dados


def main():
    boas_vindas()
    dados_pacientes = coletar_dados()
    mostrar_menu(*dados_pacientes)

if __name__ == "__main__":
    main()