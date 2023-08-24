mulheres = 0
homens100 = 0
mediamulher = 0
maiorhomem = 0
for c in range(0,4):
  sexo = input('Qual seu sexo: ')
  peso = int(input('Qual seu peso: '))
  if (sexo=='F') :
    mediamulher+=peso
    mulheres+=1
  elif(sexo=='M'):
    if(peso>100) :
      homens100+=1
    if(peso>maiorhomem) :
      maiorhomem = peso
  mediamulher/=8
print('Mulheres cadastrada: {}'.format(mulheres))
print('Homens que pesam mais de 100: {}'.format(homens100))
print('Média de peso mulheres: {}'.format(mediamulher))
print('Maior peso entre homens: {}'.format(maiorhomem))

