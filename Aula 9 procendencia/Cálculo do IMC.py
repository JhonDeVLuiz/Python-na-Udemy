
nome = str(input('Digite o seu nome:'))

altura = float(input('Digite  a sua altura:'))

peso = int(input('Digite o seu peso:'))

IMC = peso / (altura * altura)

print(f'Seu nome é{nome}, é sua {altura} ó IMC é :{IMC:.2f}')