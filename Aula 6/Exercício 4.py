cadastro = {'Nome':[],'Nascimento':[],'Sexo':[]}

total = 0
somaidade = 0
media = 0
print('-'*10,'Central de cadastros','-'*10)
print('')
while True:
    res = input('Deseja cadastrar alguém: [S/N]')
    if res in 'Nn':  # dava pra usar if res.upper() in 'N' filtrava igual
        break
    if res not in 'Ss':   #filtrar possiveis respostas erradas do usuário
        print('Digite para S para continuar o cadastro')
        continue
    nome = input('Insira o nome: ').upper()
    ano = int(input('Digite o ano de nascimento: '))
    genero = input('Sexo: (M/F)  ').upper()
    idade = 2023-ano
    somaidade +=idade
    total +=1
    cadastro['Nome'].append(nome)
    cadastro['Nascimento'].append(ano)
    cadastro['Sexo'].append(genero)

    media = somaidade/total
print('Total de cadastros: {}'.format(total))
print('Média de idade: {}'.format(media))
print('')

print('Mulheres com menos de 30:')

for i in range(total):
    if cadastro['Sexo'][i] == 'F' and idade < 30:
        print('Nome: {}, Nascimento: {}'.format(cadastro['Nome'][i], cadastro['Nascimento'][i]))

print('')
print('Homens com idade acima da média:')
for i in range(total):
    if cadastro['Sexo'][i] == 'M' and idade > media:
        print('Nome: {}, Nascimento: {}'.format(cadastro['Nome'][i], cadastro['Nascimento'][i]))

