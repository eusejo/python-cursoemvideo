print('===== DESAFIO 081 =====')

alarme = 0
lista = []
while True:
    i = int(input('digite um numero: '))
    if i == 5:
        alarme = 1
    lista.append(i)
    f = str(input('vc deseja continuar: [S/N] '))
    if f in 'Nn':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'foram digitados {len(lista)} numeros')
print(f'a lista em forma decrescente {lista}')
if alarme == 1:
    print('o 5 foi digitado e esta na lista')
else:
    print('o 5 não esta na lista')