import os
os.system('cls')

def logo_senai():
    print('\n')
    print('='*15)
    print(' SENAI - BAHIA   ')
    print('='*15)

def mostrar_dados(nome,email,telefone):
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Telefone: {telefone}')

logo_senai()

nome = str(input('Digite seu nome:'))

logo_senai()
email = input('Digite seu email:').lower()

logo_senai()
telefone = int(input('Digite seu telefone:'))

mostrar_dados(nome,email,telefone)