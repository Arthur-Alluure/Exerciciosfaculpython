l1 = int(input('Digite o 1 lado : '))
l2 = int(input('Digite o 2 lado : '))
l3 = int(input('Digite o 3 lado : '))

if (l1>0) and (l2>0) and (l3>0) :
    if (l1+l2>l3) and (l1+l3>l2) and (l3+l2>l1) :
        if (l1!=l2) and (l1!=l3) and (l2!=l3) :
            print('Triangulo Escaleno!')
        else:
            if (l1==l2) and (l1==l3) and (l3==l2) :
                print('Triangulo Equilatero!')
            else:
                print('Triangulo Isósceles!')
    else :
        print('Algum dos lados não formam um triangulo')
else :
    print('Algum dos lados não formam um triangulo')