custokwh = consumo = diascont = diaserradocont = quantosdias = 0
cont = 1
aparelhocont = []
potenciacont = []
precocont = []
tempocont = []
diascontador = []
verde = '\033[0;32m'
vermelho = '\033[0;31m'
acaba = '\033[m'
print('=' * 20, f'{verde}Calculadora de Consumo de Energia Elétrica{acaba}', '=' * 20)
print('=' * 84)
while True:
    if cont < 2:
        custokwh = float(input('\n' f'Digite o custo do kWh em sua região [DIGITE 999 PARA CALCULAR PELA CONTA DE ENERGIA] {verde}R${acaba}'))
        if custokwh == 999:
            valorconta = float(input('Valor da conta de energia: R$'))
            totalkwh = int(input('Consumo total de kWh: '))
            custokwh = valorconta / totalkwh
            print(f'Custo do kWh : {verde}R${custokwh:.2f}{acaba}')
    aparelho = str(input('\n''Nome do aparelho: ')).title().strip()
    aparelhocont.append(aparelho)
    contadoraparelho = len(aparelhocont)
    potencia = input('Digite a potência do seu aparelho: ')
    while not potencia.isdigit():
        potencia = input('Digite a potência do seu aparelho: ')
    else:
        potencia = int(potencia)
    potenciacont.append(potencia)
    tempo = ''
    cont += 1
    while not tempo.isdigit():
        tempo = (input('Digite o tempo de funcionamento diário do aparelho em horas: '))
    else:
        tempo = int(tempo)
    while tempo > 24:
        tempo = int(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
    tempocont.append(tempo)
    dias = ' '
    while dias not in 'SN' or not dias.isalpha():
        dias = str(input('Você usa o aparelho todos os dias? [S / N ] ')).upper().strip()
    if dias == 'S':
        diascont = 30
        consumo = (potencia / 1000) * tempo * 30 * custokwh
    elif dias == 'N':
        quantosdias = input('Quantos dias por mês você usa o aparelho? ')
        while not quantosdias.isdigit():
            quantosdias = input('Quantos dias por mês você usa o aparelho? ')
        else:
            quantosdias = int(quantosdias)
        diascont = quantosdias
        while quantosdias > 31:
            quantosdias = int(input('Quantos dias por mês você usa o aparelho? '))
        if quantosdias > 31:
            quantosdias = 0
        if quantosdias <= 31:
            diascont = quantosdias
        consumo = (potencia * tempo * diascont * custokwh / 1000)
    diascontador.append(diascont)
    precocont.append(consumo)
    print('')
    print('=' * 94)
    continuar = ' '
    while continuar not in 'SN' or not continuar.isalpha():
        continuar = str(input('\n''Quer calcular o consumo de outro aparelho? [S/N]: ')).upper().strip()
    else:
        continuar = str(continuar)
        print('')
        print('=' * 94)
    if continuar == 'N':
        break
for c in range(0, cont - 1):
    print(f'\nO aparelho {vermelho}{aparelhocont[c]}{acaba} com uma potência de {potenciacont[c]} watts ligado {tempocont[c]:.0f} horas por {diascontador[c]:.0f} dias vai sair por {verde}R${precocont[c]:.2f}{acaba}\n')
print('=' * 94)
