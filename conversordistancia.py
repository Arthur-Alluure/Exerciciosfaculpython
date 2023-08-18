distancia = float(input('Digite uma distância em metros: '))

km = distancia/1000
hm = distancia/100
dam = distancia/10
dm = distancia*10
cm = distancia*100
mm = distancia*1000

msg= 'A distancia de {}m corresponde a:'.format(distancia)

print(msg,'\n\t','{}km'.format(km))
print('\t'' ''{}hm'.format(hm))
print('\t'' ''{}dam'.format(dam))
print('\t'' ''{}dm'.format(dm))
print('\t'' ''{}cm'.format(cm))
print('\t'' ''{}mm'.format(mm))


