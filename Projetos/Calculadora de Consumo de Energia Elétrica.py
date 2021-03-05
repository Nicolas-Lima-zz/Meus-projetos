preto = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
ciano = '\033[1;36m'
final = '\033[m'
cont = custokwh = 0
print(f'{f" {ciano}Calculadora de Consumo de Energia Elétrica{final} ":-^84}\n')
while True:
    if cont < 1:
        custokwh = float(input(f'Digite o custo de {vermelho}1 kWh{final} em sua região: {verde}R${final}'))
        print()
    aparelho = str(input('Nome do aparelho: '))
    cont += 1
    listaaparelho = [aparelho]
    potencia = int(input('Digite a potência do aparelho: '))
    listapotencia = [potencia]
    tempo = int(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
    while tempo > 24:
        tempo = int(input('Digite o tempo de funcionamento diário do aparelho em horas: '))
    listatempo = [tempo]
    dias = int(input('Dias de uso: '))
    listadias = [dias]
    consumo = (potencia * tempo * dias * custokwh / 1000)
    listaconsumo = [consumo]
    print()
    continuar = str(input('Quer calcular o consumo de outro aparelho? [S/N]: ')).upper().strip()
    while not continuar[0] in 'SN':
        continuar = str(input('Quer calcular o consumo de outro aparelho? [S/N]: ')).upper().strip()
    if continuar.upper()[0] == 'N':
        break
    print()
for c in range(len(listapotencia)):
    print()
    print(f'O aparelho {vermelho}{listaaparelho[c]}{final} com uma potência de {listapotencia[c]} watts ligado '
          f'{listatempo[c]} horas por {listadias[c]} dias vai custar {verde}R${listaconsumo[c]:.2f}{final}')
