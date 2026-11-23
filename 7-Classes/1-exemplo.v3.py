from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int

lista_clientes = []

#Solicitando dados de um cliente
lista_clientes.append(Cliente(nome = 'Marta',idade = 30))
lista_clientes.append(Cliente(nome = 'José',idade = 40))

for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print('='*15)