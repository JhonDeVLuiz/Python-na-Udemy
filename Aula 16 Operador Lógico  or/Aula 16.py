entrada = input('[E]ntrada [S]air:')
senha_digitada = input('Senha:')

senha_permitida = 'Jhon'

if( entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Sair')

    