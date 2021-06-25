print('===== DESAFIO 042 =====')

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

#! verificando a existencia do triangulo #
if (l1 < l2 + l3) and (l2 < l3 + l1) and (l3 < l1 + l2):
    print('o triangulo existe')
else:
    print('o triangulo não existe')

#! verificando a classificação do triangulo #
if (l1 == l2 == l3):
    print('o triangulo é equilatero')
elif (l1 == l2) or (l2 == l3) or (l3 == l1):
    print('o triangulo é isoceles')
else:
    print('o triangulo é escaleno')
