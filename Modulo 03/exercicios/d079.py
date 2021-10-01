print('===== DESAFIO 079 =====')

lista = []

while True:
    i = int(input('digite um numero: '))
    if i not in lista:
        lista.append(i)
        print('valor adicionado com sucesso')
    else:
        print('valor duplicado, não vou adicionar')
    f = str(input('vc deseja continuar: [S/N] '))
    if f in 'Nn':
        break
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'vc digitou os valores {lista}')