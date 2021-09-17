print('===== DESAFIO 075 =====')

tupla = ('lapis', 'caneta',
    'senhor', 'mouse', 'teclado',
    'controle', 'televisao', 'copo'
)

for c in range(0, len(tupla)):
    if tupla[c] in 'aeiou':
        print(f'a vogais de {tupla[c]}') 