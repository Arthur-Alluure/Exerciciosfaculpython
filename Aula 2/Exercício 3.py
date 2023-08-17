kmperc = float(input('Quantos km você percorreu: '))
dias = int(input('Por quantos dias você alugou: '))

preco = (dias*60) + (kmperc*0.15)

print('Você alugou o carro por: {} dias'.format(dias))
print('E percorreu: {} km'.format(kmperc))
print('Portanto deverá pagar: {}R$'.format(preco))
