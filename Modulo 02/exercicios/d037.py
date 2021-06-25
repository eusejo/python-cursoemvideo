print('===== DESAFIO 037 =====')

numero = int(input('digite um numero inteiro: '))

print('''Escolha uma das opções
[1] Converter para binario
[2] Converter para octal
[3] converter para hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINARIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Numero invalido')
