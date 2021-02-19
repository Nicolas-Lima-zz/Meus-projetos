quantosdias = 0
print('=' * 20, '{}Calculadora de consumo em kWh de um aparelho eletrônico{}'.format('\033[1;34m', '\033[m'), '=' * 20)
print('=' * 97)
print('\n''{}Para calcular o consumo mensal de um aparelho, precisamos saber quanto custa 1 kWh em sua região{}!'.format('\033[1;34m', '\033[m'))
custokwh = float(input('Digite o custo de 1 kwh em sua região [{}SE NÃO SOUBER DIGITE{} 999] R$'.format('\033[1;31m', '\033[m')))
if custokwh == 999:
    naosabe = float(input('Valor da conta de energia: R$'))
    naosaber = int(input('Consumo total de kWh: '))
    custokwh = naosabe / naosaber
    print(f'Custo de 1 kWh : {custokwh:.2f}')
aparelho = str(input('Nome do aparelho: ')).title().strip()
potencia = int(input('Digite a potência de seu aparelho: '))
tempo = float(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
while tempo > 24:
    tempo = float(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
dias = str(input('Voce usa o aparelho todos os dias? [S / N ] ')).upper().strip()
while dias != 'S' and dias != 'N':
    dias = str(input('Voce usa o aparelho todos os dias? [S / N ] ')).upper().strip()
if dias == 'S':
    consumo = (potencia / 1000) * tempo * 30 * custokwh
    print('=' * 83, '\n ')
    print('Nome do aparelho: ',aparelho)
    print('O custo mensal de seu aparelho ligado por {:.0f} horas por dia, vai ser de {}R${:.2f}{}\n'.format(tempo, '\033[1;32m', consumo, '\033[m'))
    print('=' * 83)
elif dias == 'N':
   quantosdias = int(input('Quantos dias por mês você usa o aparelho? '))
   consumo = (potencia * tempo * quantosdias * custokwh / 1000)
   while quantosdias > 31:
       quantosdias = int(input('Quantos dias por mês você usa o aparelho? '))
   print('=' * 79, '\n ')
   print('O custo de seu aparelho ligado por {:.0f} horas por {} dias vai ser de {}R${:.2f}{}\n'.format(tempo, quantosdias, '\033[1;32m', consumo, '\033[m'))
   print('=' * 79)
continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
while continuar != 'S' and continuar != 'N':
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
while continuar == 'S':
    calcular = str(input('Você deseja calcular um novo preço para 1 kWh? Se sim, digite S. Se não, digite N: ')).upper().strip()
    if calcular == 'S':
        naosabe = float(input('Valor da conta de energia: R$'))
        naosaber = int(input('Consumo total de kWh: '))
        custokwh = naosabe / naosaber
        print(f'Custo de 1 kWh : {custokwh:.2f}')
    elif calcular == 'N':
        print(f'Custo de 1 kWh : {custokwh:.2f}')
    potencia = int(input('Digite a potência de seu aparelho: '))
    tempo = float(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
    while tempo > 24:
        tempo = float(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
    dias = str(input('Voce usa o aparelho todos os dias? [S / N ] ')).upper().strip()
    while dias != 'S' and dias != 'N':
        dias = str(input('Voce usa o aparelho todos os dias? [S / N ] ')).upper().strip()
    if dias == 'S':
        consumo = (potencia / 1000) * tempo * 30 * custokwh
        print('=' * 83, '\n ')
        print('O custo mensal de seu aparelho ligado por {:.0f} horas por dia, vai ser de {}R${:.2f}{}\n'.format(tempo, '\033[1;32m', consumo, '\033[m'))
        print('=' * 83)
    elif dias == 'N':
        quantosdias = int(input('Quantos dias por mês você usa o aparelho? '))
        consumo = (potencia * tempo * quantosdias * custokwh / 1000)
        while quantosdias > 31:
            quantosdias = int(input('Quantos dias por mês você usa o aparelho? '))
        print('=' * 79, '\n ')
        print('O custo de seu aparelho ligado por {:.0f} horas por {} dias vai ser de {}R${:.2f}{}\n'.format(tempo, quantosdias, '\033[1;32m', consumo, '\033[m'))
        print('=' * 79)
    if continuar == 'N':
        break
print('FIM DO PROGRAMA!')
