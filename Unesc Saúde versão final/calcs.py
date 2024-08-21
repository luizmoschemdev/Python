def calcular_imc (peso_do_paciente, altura_do_paciente):
        calcular_imc = peso_do_paciente / (altura_do_paciente * altura_do_paciente)
        print (f"seu imc é {calcular_imc:2f}")


def calcular_taxa_basal (peso_do_paciente, altura_em_centimetros, idade_do_paciente, genero_biologico) :
        match genero_biologico:
                case "M" | "m":
                        tmb = 66 + (13.7 * peso_do_paciente) + (5 * altura_em_centimetros) - (6.8 * idade_do_paciente) 
                        print(f"Sua Taxa Metabólica Basal é {tmb} calorias.") 
                case "F" | "f":
                        tmb = 665 + (9.6 * peso_do_paciente) + (1.8 * altura_em_centimetros) - (4.7 * idade_do_paciente)
                        print(f"Sua Taxa Metabólica Basal é {tmb} calorias.")