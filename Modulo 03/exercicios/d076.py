print('===== DESAFIO 076 =====')

produtos = (
    'lapis', 1.75,
    'borracha', 2.00,
    'caderno', 15.00,
    'estojo', 25.00,
    'transferidor', 4.20,
    'compasso', 9.99,
    'mochila', 120.32,
    'canetas', 22.30,
    'livro', 34.90
)

print('-'*40)
print('\tLISTAGEM DE PREÇOS')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end="")
    else:
        print(f'R$ {produtos[pos]:>7.2f}')
print('-'*40)