print('Calculadora')
print(' + Adição')
print(' - Subtração')
print(' * Multiplicação')
print(' / Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer: ')

if (op != '+') and (op != '-') and (op != '*') and  ( op != '/') :
   print('Operação inválida!')
else:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    if (op == '+') :
        calculo = n1 + n2
        print('Resultado: {} + {} = {}'.format(n1,n2,calculo))
    elif (op == '-') :
        calculo = n1 - n2
        print('Resultado: {} - {} = {}'.format(n1, n2, calculo))
    elif (op == '*') :
        calculo = n1 * n2
        print('Resultado: {} * {} = {}'.format(n1, n2, calculo))
    elif (op == '/') :
        calculo = n1 / n2
        print('Resultado: {} / {} = {}'.format(n1, n2, calculo))

print('Encerrando o programa...')
