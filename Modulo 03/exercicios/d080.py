print('===== DESAFIO 080 =====')

lista = []
for c in range(0, 5):
    i = int(input('digite um numero: '))
    if c == 0 or i > lista[-1]:
        lista.append(i)
    else:
        pos = 0
        while pos < len(lista):
            if i <= lista[pos]:
                lista.insert(pos, i)
                break
            pos += 1
print('-='*30)
print(f'os valores em ordem foram {lista}')