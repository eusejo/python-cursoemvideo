print('===== DESAFIO 064 =====')

n = 0
c = 0
s = 0

while n != 999:
    n = int(input('digite um valor: '))
    
    if n != 999:
        c += 1 
        s += n
print(f'a quantidade de numeros digitados foi de {c}')
print(f'a soma de todos os numeros foi de {s}')