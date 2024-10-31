numero_str = input('Vou dobra o número que você digitar:')

# print(numero_str.isdigit())
# if numero_str.isdigit():

#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número inteiro!')

try:
    print('STR:',numero_str)
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
  print('Isso não é um número!')
  