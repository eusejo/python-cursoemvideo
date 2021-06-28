print('===== DESAFIO 049 =====')

n = int(input('digite um valor: '))

print('''Escolha uma operação
[0] Adição    [2] Multiplicação
[1] Subtração [3] Divisão''')

opcao = int(input('-> '))

if opcao == 0:
    # adição
    for c in range(1, 11):
        print(f'{n} + {c} = {n+c}')
elif opcao == 1:
    # subtração
    for c in range(1, 11):
        print(f'{n} - {c} = {n-c}')
elif opcao == 2:
    # multiplicação
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
elif opcao == 3:
    # Divisão
    for c in range(1, 11):
        print(f'{n} / {c} = {n / c}')
else:
    print('opção invalida!!')