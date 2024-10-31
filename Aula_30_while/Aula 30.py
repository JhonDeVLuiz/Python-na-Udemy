condicao = True

while condicao:
    nome = input('Digite o seu nome')
    print(f'O seu nome é {nome}')

    if nome == 'sair':
        break
   
print('Acabou')