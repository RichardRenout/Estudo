from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int
    altura = float
    peso = float

lista_clientes = []

print('SOLICITANDO DADOS DE DOIS CLIENTES.')
for i in range(2):
    dados_do_cliente = cliente(
        nome = input('\nDigite seu nome: '),
        idade = int(input('Digite sua idade: ')),
        altura = float(input('Digite sua altura: ')),
        peso = float(input('Digite seu peso: '))
    )
    lista_clientes.append(dados_do_cliente)

print('\NEXIBINDO DADOS')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print(f'Peso: {cliente.peso}')
    print('='*15)