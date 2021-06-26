print('===== DESAFIO 044 =====')

preco = float(input('qual o preço do produto: '))
print('''Escolha uma forma de pagamento
[1] a vista dinheiro/cheque
[2] a vista no cartão
[3] em ate 2x no cartão
[4] 3x ou mais no cartão''')
pagamento = int(input('qual a forma de pagamento: '))

if (pagamento == 1 ):
    desconto = (preco * (10/100))
    print(f'vc ira pagar {preco - desconto}')
elif (pagamento == 2):
    desconto = (preco * (5/100))
    print(f'vc ira pagar {preco - desconto}')
elif (pagamento == 3):
    print(f'vc ira pagar {preco}')
elif (pagamento == 4):
    juros = preco + (preco * (20/100))
    totalparc = int(input('quantas parcelas? '))
    parcelas = juros / totalparc
    print(f'sua compra sera parcelada em {totalparc} de {parcelas} com juros')
    print(f'vc vai pagar {juros}')
else:
    print('opção invalida')