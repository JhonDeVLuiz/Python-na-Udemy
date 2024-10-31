# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  J H O N
# -6-5-4-3-2-1
nome = 'Jhon'
print(nome[2])
print(nome[-3])
print('h' in nome)
print('hon' not in nome)


nome = input("Digite o seu nome:")

encontra = input('Que palavara você que encontrar:')
if encontra in nome:
    print(f'{encontra} está em {nome}')
else:
    print(f'{encontra} não está em {nome}')