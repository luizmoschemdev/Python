n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva um número: '))
n3 = int(input('Escreva um número: '))

if (n1>n2 and n1>n3 and n2>n3):
    print ('%d %d %d '%(n1, n2, n3))
if (n1>n2 and n1>n3 and n3>n2):
    print ('%d %d %d '%(n1, n2, n3))
if (n1>n3 and n1>n2 and n3>n1):
    print ('%d %d %d '%(n1, n2, n3))
if (n1>n3 and n1>n2 and n3>n2):
    print ('%d %d %d '%(n1, n2, n3))
if (n3>n1 and n3>n2 and n2>n1):
     print ('%d %d %d '%(n1, n2, n3))
if (n3>n1 and n3>n2 and n1>n2):
     print ('%d %d %d '%(n1, n2, n3))