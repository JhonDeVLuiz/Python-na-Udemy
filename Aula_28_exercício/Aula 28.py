nome = input('Digite o seu nome:')

num_caractere = len(nome)
if num_caractere  > 1:
    print('Digite mais letras')
    if num_caractere <= 4:
        print('O seu nome é curto')
    elif num_caractere <= 5:
        print('O seu nome é normal')
    elif num_caractere <= 6:
        print('O seu nome é muito grande')
else:
    print('Digite mais de um letra')