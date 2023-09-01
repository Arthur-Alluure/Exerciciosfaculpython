notas = [9,7,7,10,3,9,6,6,2]

print(notas.count(7)) #contando quantas notas 7 são:

notas[-1] = 4 #trocando a última nota por 4
print('')
print(notas)

notas.sort() #organizando a lista
print(notas)


maiornota = 0
somanota = 0
nnotas = 0
for i in notas:
    somanota +=i
    nnotas +=1
    if (i>maiornota) :
        maiornota = i
media = somanota/nnotas
print('')
print(maiornota)
print(somanota)
print(media)

#encontrando a maior nota, a soma de todas as notas e a média das mesmas.