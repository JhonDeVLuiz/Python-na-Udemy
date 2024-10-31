while True:
    print('-------Calculadora--------')
    n1 = input('Digite um número:')
    n2 = input('Digite outro número:')
    operador = input('Digite o operador (+-/*):')

    numeros_validos = None
    try:
       num_1_float = float(n1)
       num_2_float = float(n2)
       numeros_validos = True
          
    except :
       numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operadores inválidos')
        continue 

    if len(operador) > 1:
        print("Só pode haver um operador")
        continue
    
    sair = input('Quer sair [S]im:').lower().startswith('s')
    if sair:
        break
