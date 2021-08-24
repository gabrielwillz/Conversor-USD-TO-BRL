import requests
import json
import time


def main():
    def titulo():
        print('''\033[1;91m	
            █░█ ▄▀▀ █▀▄     ▀█▀ ▄▀▄     █▀▄ █▀▀▄ █░░ 
            █░█ ░▀▄ █░█     ░█░ █░█     █▀█ █▐█▀ █░▄ 
            ░▀░ ▀▀░ ▀▀░     ░▀░ ░▀░     ▀▀░ ▀░▀▀ ▀▀▀ 
                \033[0;0m''')

    def api():
        contacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        contacao = contacao.json()
        contacao_dolar = contacao['USDBRL']['bid']
        return float(contacao_dolar)

    def calculo(a, b):
        conver = a * b
        print('Valor final: \033[1;31m{:.2f}\033[0;0m'.format(conver))

    def modelo():
        cont = api()
        print()
        print('----------------------------------------------')
        print()
        print(f'CONTAÇÃO ATUAL DO DÓLAR: {cont} |||| VALOR INSERIDO: {valor_inserido}')
        print()
        print('----------------------------------------------')
        print()

    titulo()
    print()
    valor_inserido = float(input('QUANTOS VOCÊ QUER CONVERTER?: '))
    modelo()
    calculo(valor_inserido, api())
    print()

    option = int(input('Quer fazer outro cálculo?\n 1. SIM\n 2. NÃO\n'))

    if option == 1:
        main()
    else:
        print('Saindo.......')


main()
if __name__ == '__main__':
    main()