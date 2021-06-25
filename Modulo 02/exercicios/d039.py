print('===== DESAFIO 039 =====')

data = int(input('qual a sua data de nascimento: '))
idade = 2021 - data

if idade < 18:
    print('vc ainda não tem idade para se alistar')
    print(f'ainda faltam {18 - idade} anos')
elif idade == 18:
    print('um bora se alistar meu fi')
else:
    print('ja passou da hora c ta vei ja')
    print(f'ta atrasado {idade - 18} anos')
   
