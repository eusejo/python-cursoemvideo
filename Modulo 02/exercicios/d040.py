print('===== DESAFIO 040 =====')

nota1 = float(input('digite a sua primeira nota: '))
nota2 = float(input('digite a sua segunda nota: '))
m = (nota1 + nota2) / 2

print(f'a sua media final é de {m}')

if m < 5:
    print('vc esta reprovado')
elif m > 5 and m < 6.9:
    print('vc esta de recuperação')
elif m >= 7:
    print('vc foi aprovado')
