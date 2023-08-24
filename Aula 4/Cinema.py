somavalor = 0
ingresso = 0
pessoas = 0
mediapessoas = 0
somaidade = 0
print('-'*10,'Bem-vindo ao Cinema','-'*10)
while True:
    idade = int(input('Digite sua idade: '))
    somaidade +=idade
    pessoas+=1
    if (idade<3) :
        print('Devido a idade da criança, ela não pagará pela entrada, aproveite!')
    elif(idade==3) or (idade<=12) :
        print('Para crianças entre 3 e 12 anos o ingresso custará apenas: 15R$')
        ingresso = 15
    elif(idade>12) :
        print('Para maiores de 12 anos o ingresso custa: 30R$')
        ingresso = 30
    somavalor+=ingresso
    resposta = input('Deseja adquirir mais ingressos para esse filme: [S] [N]  ')
    if (resposta=='N') or (resposta=='n') or (resposta=='nao') :
        break
mediapessoas = somaidade/pessoas
print('-'*50)
print('Obrigado, ao todo foram comprados: {} ingressos'.format(pessoas))
print('O valor da sua compra foi de: {}R$'.format(somavalor))
print('A média de idade das pessoas que compraram foi de: {}'.format(mediapessoas))
