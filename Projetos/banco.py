print(f'{" Banco ":-^40}')
saque = float(input('Digite a quantia a ser sacado: R$'))
total = saque
ced = 100
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont == 1:
            nomeced = 'cédula'
        else:
            nomeced = 'cédulas'
        if ced == 1:
            nomereal = 'real'
        else:
            nomereal = 'reais'
        if cont > 0:
            print(f'{cont} {nomeced} de {ced} {nomereal}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0