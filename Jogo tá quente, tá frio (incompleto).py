import random
x  =  random.randint (1, 101)
print (x)
t = 200
i = 0
print ('Decolagem!')
while (t !=x):
    t= int (input('Digite um número: '))
    i+=1
    print (f'quantidade de tentativas: {i}' )
    if (t - 20 < x):
        print ('Tá quente')
    else:
        print ('Ta frio')
