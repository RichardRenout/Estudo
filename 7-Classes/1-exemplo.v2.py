from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int

#Solicitando dados de um cliente
cliente1 = Cliente('Marta', 30)

#Solicitando dados de outro cliente
cliente2 = Cliente('José', 40)

print(f'Nome: {cliente1.nome}')
print(f'Idade: {cliente1.idade}')

print(f'Nome: {cliente2.nome}')
print(f'Idade: {cliente2.idade}')