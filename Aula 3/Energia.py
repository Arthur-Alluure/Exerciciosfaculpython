print('-'*10,'CEMIG','-'*10)
print('Informe seu tipo de instalação: ')
print('Tecle [R] para Residências')
print('Tecle [I] para Industrias')
print('Tecle [C] para Comércios')
print('Outra tecla para sair...')
print('')
inst = input('Digite sua instalação: ')
if (inst!='R') and (inst!='I') and (inst!='C') :
    print('Operação Inválida!')
else:
    consumidos= int(input('Quantos Kwh foram consumidos : '))
    if (inst=='R') and (consumidos<=500) :
        preco = consumidos*0.40
        print('Total a pagar: {}R$'.format(preco))
    elif (inst=='R') and (consumidos>500) :
        preco = consumidos*0.65
        print('Total a pagar: {}R$'.format(preco))
    elif (inst=='C') and (consumidos<=1000) :
        preco = consumidos*0.55
        print('Total a pagar: {}R$'.format(preco))
    elif (inst=='C') and (consumidos>1000) :
        preco = consumidos*0.60
        print('Total a pagar: {}R$'.format(preco))
    elif (inst=='I') and (consumidos<=5000) :
        preco = consumidos*0.55
        print('Total a pagar: {}R$'.format(preco))
    elif (inst=='I') and (consumidos>5000) :
        preco = consumidos*0.60
        print('Total a pagar: {}R$'.format(preco))

print('Saindo do programa...')


