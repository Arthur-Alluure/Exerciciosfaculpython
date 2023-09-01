import random


def validaint (pergunta,min,max) :
    try:
        x = int(input(pergunta))
        while (x<min) or (x>max) :
            print('Você digitou uma jogada inválida, tente novamente')
            print('')
            x = int(input(pergunta))
        return x
    except ValueError:
        print('Digite a jogada em forma númerica')
        print('')

def vencedor(jogador1,jogador2) :
    global empate,v1,v2
    if (jogador1 == 1): #Pedra
        if (jogador2 == 1): #Pedra
            empate +=1
        elif(jogador2 == 2): #Papel
            v2 +=1
        elif (jogador2 == 3): # Tesoura
            v1 +=1

    elif (jogador1 == 2): #Papel
        if (jogador2 == 1):  # Pedra
            v1 +=1
        elif (jogador2 == 2):  # Papel
            empate +=1
        elif (jogador2 == 3):  # Tesoura
            v2 +=1

    elif (jogador1 == 3): # Tesoura
        if (jogador2 == 1):  # Pedra
            v2 +=1
        elif (jogador2 == 2):  # Papel
            v1 +=1
        elif (jogador2 == 3):  # Tesoura
            empate +=1
    resultados = [v1,v2,empate]
    return resultados





print('JOKENPO')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('0 - Sair')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = validaint('Informe sua jogada: ', 0, 3)
    if j1 == 0:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1,j2])
    resultados = vencedor(j1,j2)

    for jogada in jogadas:
        for dado in jogada :
            print(dado,end=' ')
        print()

print('Números de vitórias do jogador 1 : {}'.format(resultados[0]))
print('Números de vitórias do jogador 2 : {}'.format(resultados[1]))
print('Números de empates : {}'.format(resultados[2]))