cursos = ["Adminstração", "Fisioterapia", "Fisioterapia", "Psicologia", "Medicina"]
cursos[1] = "Sistemas de informação"
cursos.append("Punheta guiada")
cursos.insert (2, "Engenharia Civil")
del cursos[3]
print (cursos)

for curso in cursos:
    print (curso)

print(f"o segundo curso é: {cursos[1]}")

