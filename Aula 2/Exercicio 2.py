produto = float(input('Informe o preço do produto: '))
desconto = float(input('Informe qual o percentual do desconto : '))

vldesconto= desconto/100*(produto)
vlfinal= produto-vldesconto


msg= 'O valor do desconto foi de {}R$\n''Seu produto irá custar {}R$'.format(vldesconto,vlfinal)

print(msg)