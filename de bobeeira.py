def media():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    resultado = (nota1+nota2)/2
    print('Sua média foi de: {}'.format(resultado))
    situacao(resultado)
def situacao(status) :
    if (status>=7) :
        print('Aprovado')
    else :
        print('Reprovado')

media()
