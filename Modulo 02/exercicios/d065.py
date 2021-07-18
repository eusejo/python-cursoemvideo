print('===== DESAFIO 065 =====')

op = ''
count = 0
media = 0
maior = menor = 0

while op != 'n':
    num = int(input('digite um valor: '))
    count += 1
    media += num
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    op = str(input('vc deseja continuar: '))
print(f'a media dos numeros foi de {media/count}')
print(f'o maior numero foi {maior} e o menor foi {menor}')
