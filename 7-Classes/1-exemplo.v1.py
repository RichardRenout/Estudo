from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Client:
    # Nome da variável : tipo da variável
    nome: str
    idade: int

#Solicitando dados de um cliente
nome = 'Marta'
idade = 30

#Solicitando dados de outro cliente
nome = 'José'
idade = 40

print(f'Nome: {nome}')
print(f'Idade: {idade}')