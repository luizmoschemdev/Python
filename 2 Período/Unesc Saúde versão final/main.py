from menu import boas_vindas, mostrar_menu


def main():
    boas_vindas()
    nome_do_paciente: str = input("Digite seu nome: ")
    altura_do_paciente = float(input("Digite sua altura: "))
    peso_do_paciente = float(input("Digite seu peso: "))
    idade_do_paciente = int(input("Digite sua idade (em anos): "))
    genero_biologico = input("Digite seu gênero biológico (M/F): ").upper()#coloca todas as letra em maiusculo
    mostrar_menu(altura_do_paciente, peso_do_paciente, idade_do_paciente, genero_biologico)
if __name__ == "__main__":
    main()