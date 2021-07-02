print('===== DESAFIO 053 =====')

nome = str(input('digite uma palavra: ')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1,- 1, -1):
    inverso += junto[letra]
print(f'o inverso de {junto} é {inverso}')

if inverso == junto:
    print('a frase digita é um palindromo')
else:
    print('a frase digitada não é um palindromo')
