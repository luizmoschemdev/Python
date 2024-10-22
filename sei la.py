def capeta():
    retorno = int (input(print("Deseja volat pro menu")))
    match retorno:
        case 1:
            return True
        case 2:
            return False
    


retorn= True
while retorn == True:
    opcao = int (input(print ("""MENU
        1. TASKMANEGER
        2. OOOOOOOO
        Selecione uma opção.""")))

    match opcao:
        case 1:
            task = ["cachoro", "cavalo"]
            task.append (input("digite um elemento"))
            task.insert (0, "bosta")
            task[1] = "pinto"
            del task[2]
            print (task)
            retorn = capeta()

