print('===== DESAFIO 043 =====')

peso = float(input('qual o seu peso: '))
altura = float(input('qual a sua altura: '))
imc = peso / altura ** 2

print(f'o seu imc é de {imc}')

if imc < 18.5:
    print('vc esta abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('vc esta no peso ideal')
elif imc > 40:
    print('ovesidade morbida')
