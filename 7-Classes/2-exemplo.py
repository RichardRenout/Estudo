from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

 

@dataclass
class cliente:
    nome = str
    telefone = str
    email = str

lista_cliente = []

print('\n SOLICITANDO DADOS DE CLIENTE')

for i in range(2):
    dados_cliente = cliente(
    nome = input('\nDigite seu nome: '),
    telefone = input('Digite seu telefone: '),
    email = input('Digite seu E-mail'))
    lista_cliente.append(dados_cliente)

print('\n Exibindo Dados')
print(f'Nome: {cliente.nome}')
print(f'Nome: {cliente.telefone}')
print(f'Nome: {cliente.email}')
print('='*15)

