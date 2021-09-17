print('===== DESAFIO 078 =====')

lista = []
for c in range(0, 5):
    lista.append(int(input(f'digite um valor para a posição {c}: ')))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'vc digitou os valores {lista}')
print(f'o maior valor digitado foi o {max(lista)} na posição {lista.index(max(lista))}')
print(f'o menor valor digitado foi o {min(lista)} na posição {lista.index(min(lista))}')