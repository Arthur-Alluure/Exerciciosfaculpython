numero = int(input('De qual número você quer saber a taboada : '))

count = 0
while (count<10) :
    count = count+1
    taboada = numero*count
    print('{} * {} = {}'.format(numero,count,taboada))