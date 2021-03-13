preto = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
ciano = '\033[1;36m'
final = '\033[m'
cont = custokwh = 0
listaaparelho = []
listapotencia = []
listatempo = []
listadias = []
listaconsumo = []
barra = f'{preto}/{final}'
print(f'{f" {ciano}Calculadora de Consumo de Energia Elétrica{final} ":-^84}\n')
while True:
    if cont == 0:
        while True:
            try:
                    custokwh = float(input(f'Digite o custo de {vermelho}1 kWh{final} em sua região: {verde}R${final}'))
                    print()
                    break
            except ValueError:
                pass
    cont += 1
    while True:
        try:
            potencia = int(input('Digite a potência do aparelho: '))
            break
        except ValueError:
            pass
    listapotencia.append(potencia)
    while True:
        try:
            tempo = int(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
            if tempo <= 24:
                break
        except ValueError:
            pass
    listatempo.append(tempo)
    while True:
        try:
            dias = int(input('Dias de uso: '))
            break
        except ValueError:
            pass
    listadias.append(dias)
    consumo = (potencia * tempo * dias * custokwh / 1000)
    listaconsumo.append(consumo)
    print()
    continuar = str(input('Quer calcular o consumo de outro aparelho? [S/N]: ')).upper().strip()
    while not continuar[0] in 'SN':
        continuar = str(input('Quer calcular o consumo de outro aparelho? [S/N]: ')).upper().strip()
    if continuar[0] == 'N':
        break
    print()
for c in range(0, cont):
    if c == 0:
        print()
    print(f'{c + 1}° aparelho: Potência:  {listapotencia[c]} watts {barra} Tempo de uso por dia: '
          f'{listatempo[c]} horas {barra} Dias de uso: {listadias[c]} dias {barra} Custo: {verde}'
          f'R${listaconsumo[c]:.2f}{final}')
