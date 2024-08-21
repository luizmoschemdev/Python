numero = int(input('escreva um número'))
resultado = numero % 2

if resultado == 0:
    print ('o numero{} é par'. format (numero))
else:
    print ('o número {} é impar'. format(numero))