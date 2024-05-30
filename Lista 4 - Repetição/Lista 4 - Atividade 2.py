turmas = int(input("Digite quantas turmas tem: "))
media = 0
for i in range(turmas):
    while True:
        alunos = int(input(f"Digite quantos alunos tem na turma {i + 1}: "))
        if alunos <= 40:
            media = ((media * i) + alunos) / (i + 1)
print(f"A media de alunos por turma é {media}")