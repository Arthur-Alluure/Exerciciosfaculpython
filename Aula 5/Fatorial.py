def valida_int(pergunta,min,max) :
    x = int(input(pergunta))
    while (x<min) or (x>max) :
        '''
        função valida os dados
        '''
        x = int(input(pergunta))
    return x

def fatorial(num) :
    '''
    Calcula a fatorial
    :param num:
    :return:
    '''
    fat = 1
    if num ==0 :
        return fat

    for c in range(1,num+1):
        fat *= c
    return fat

x = valida_int('Número do fatorial: ',0,99999)
print('{}! = {}'.format(x,fatorial(x)))
