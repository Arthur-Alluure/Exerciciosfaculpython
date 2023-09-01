palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')
 #acha as vogais das palavras nas tuplas

for count in palavras:
    print('\nPalavra: {}. Vogais: '.format(count.upper()),end='')
    for count2 in count:
        if count2.lower() in 'aeiou' :
            print(count2.upper(), end=' ')