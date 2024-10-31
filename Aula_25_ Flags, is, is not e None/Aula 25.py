condicao = False
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Fasa algo')
else:
   
    print('Não faça nada')
# print(passou_no_if,passou_no_if is None)
# print(passou_no_if,passou_no_if is not None)
if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')