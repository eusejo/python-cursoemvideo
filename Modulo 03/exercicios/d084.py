print('===== DESAFIO 084 =====')

lista = []
dados = []
pessoas = 0
mai = men = 0
while True:
    dados.append(str(input('digite o seu nome: ')))
    pessoas += 1
    dados.append(float(input('digite o seu peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    f = str(input('vc quer continuar [S N] '))
    if f in 'Nn':
        break
print(f'{pessoas} foram cadastradas.')
print(f'o maior peso foi de {mai} kilos. peso de ',end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]}',end='')
print(f'o menor peso foi de {men} kilos. peso de ',end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}',end='')