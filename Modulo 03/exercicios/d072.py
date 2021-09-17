print('===== DESAFIO 072 =====')

numeros = ('zero', 'um', 'dois'
    'tres', 'quatro', 'cinco',
    'seis', 'sete', 'oito',
    'nove', 'dez', 'onze',
    'doze', 'treze', 'quatorze',
    'quinze', 'dezeses', 'dezesete',
    'dezoito', 'dezenove', 'vinte'
)

while True:
    num = int(input('digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'vc digitou o numero {numeros[num-1]}')
        break
    else:
        print('tente novamente')