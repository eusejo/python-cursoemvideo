print('===== DESAFIO 082 =====')

lista = list()
par = []
impar = []
while True:
    num = int(input('digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    elif not num % 2 == 0:
        impar.append(num)
    f = str(input('vc quer continuar [S N]'))
    if f in 'Nn':
        break
print(lista)
print(par)
print(impar)