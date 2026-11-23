from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class cliente:
    nome: str
    idade: int
    telefone: str
    endereco: str

    def registro(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')

    def informar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')

    def marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')

lista_cliente = []

print('\n SOLICITANDO DADOS')

for i in range(1):
    dados_cliente = cliente(
    nome = input('\nDigite seu nome: '),
    idade = float(input('Digite sua idade: ')),
    telefone = str(input('Digite seu telefone: ')),
    endereco = str(input('Digite seu endereço: ')))

    lista_cliente.append(dados_cliente)

print('\nRegistro')
for cliente in lista_cliente:
    cliente.registro()

print('\nInformar')
for cliente in lista_cliente:
    cliente.informar()

print('\nMarketing')
for cliente in lista_cliente:
    cliente.marketing()