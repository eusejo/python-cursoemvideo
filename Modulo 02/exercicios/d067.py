print('===== DESAFIO 067 =====')

count = 0

while True:
    n = int(input('quer ver a tabuada de qual valor: '))
    if n < 0:
        print('programa tabuada encerrado...volte sempre')
        break
    count = 0
    print('-='*30)
    while count <= 9:
        count += 1
        print(f'{n} + {count} = {n+count}')
    print('-='*30)