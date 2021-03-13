print('=' * 20, 'REGISTROS DE ITENS', '=' * 20, '\n')
vermelho = '\033[1;31m'
verde = '\033[1;32m'
final = '\033[m'
preto = '\033[0;30m'
listanome = []
listapreco = []
listadata = []
cont = 0
while True:
    nomedoitem = str(input('Nome do item: ')).title().strip()
    listanome.append(nomedoitem)
    cont += 1
    precodoitem = float(input(f'Custo: {verde}R${final}'))
    listapreco.append(precodoitem)
    datadacompra = str(input(f'Data da compra ( {vermelho}NAO{final} para não colocar uma data ) : ')).upper().strip()
    if datadacompra[0] == 'N':
        datadacompra = 'Sem data de compra'
    print('')
    listadata.append(datadacompra)
    print('=' * 60, '\n')
    adicionar = str(input('Quer adicionar mais algum item? [S/N]: ')).upper().strip()[0]
    while adicionar not in 'SN':
        adicionar = str(input('Quer adicionar mais algum item? [S/N]: ')).upper().strip()[0]
    print('')
    print('=' * 60, '\n')
    if adicionar == 'N':
        break
for c in range(0, cont):
    print(f'Nome do item: {listanome[c]} {preto}/{final} Preço: {verde}R${listapreco[c]:.2f}{final} {preto}/{final}'
          f' Data da compra: {listadata[c]}')
    print('')
print('=' * 60)

