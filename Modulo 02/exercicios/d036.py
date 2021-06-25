print('===== DESAFIO 036 =====')

casa = float(input('quanto custa a casa: '))
salario = float(input('qual o seu salario: '))
tempo = int(input('por quanto tempo vc vai pagar: '))
prestacao = casa / (tempo * 12)

print(f'vc vai pagar R${prestacao} por mes em {tempo} ano')

if (prestacao > (salario * 30 / 100)):
    print('mas vc não vai conseguir pagar')
else:
    print('trato feito')
