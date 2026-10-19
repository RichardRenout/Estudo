import os
os.system('cls')

senha_salva = senha
login_salvo = login
numeros = []
QUANTIDADE = 5

while True:
    login = str (input('Digite seu login: '))
    senha = float(input('Digite sua senha: '))

    for i in range(QUANTIDADE):
        numero = int(input('Digite um número: '))
    numeros.append(numero)

print(f'Exibindo Dados: {numeros}')
