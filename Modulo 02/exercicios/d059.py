print('===== DESAFIO 059 =====')

from time import sleep 

n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
op = 0

while op != 5:
    print('-='*20)
    print('''ESCOLHA OQ VC QUER FAZER
    [1] SOMAR    [2] MULTIPLICAR
    [3] MAIOR    [4] NOVOS NUMEROS
       [5] SAIR DO PROGRAMA''')
    print('-='*20)
    op = int(input('=> '))
    if op == 1:
        print(f'a soma entre {n1} e {n2} é {n1+n2}')
    elif op == 2:
        print(f'{n1} X {n2} é {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é o maior')
        else:
            print(f'{n2} é o maior')
    elif op == 4:
        print('==== sugerindo novo numeros ====')
        n1 = float(input('digite um novo numero: '))
        n2 = float(input('digite outro novo numero: '))
    elif op == 5:
        print('SAINDO')
        sleep(1)
        op = 5
    sleep(1)