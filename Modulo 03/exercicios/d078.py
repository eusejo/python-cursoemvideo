print('===== DESAFIO 078 =====')

lista = []
menor = maior = 0
for c in range(0, 5):
    lista.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'vc digitou os valores {lista}')
print(f'o maior valor digitado foi o {maior} nad posições',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'o menor valor digitado foi o {menor} nas posições',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ',end='')
print()