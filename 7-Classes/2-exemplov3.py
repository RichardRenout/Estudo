from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class cliente:
    nome: str
    telefone: str
    email: str

    def zap_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print('='*30)

    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print('='*30)

lista_cliente = []

print('\n SOLICITANDO DADOS DE CLIENTE')

for i in range(2):
    dados_cliente = cliente(
    nome = input('\n Digite seu nome: '),
    telefone = input('Digite seu telefone: '),
    email = input('Digite seu E-mail: ')
    )

    lista_cliente.append(dados_cliente)

print('\n Exibindo Dados')
for cliente in lista_cliente:
    cliente.mostrar_dados()

print('Email marketing')
for cliente in lista_cliente:
    cliente.email_marketing()

print('Zap marketing')
for cliente in lista_cliente:
    cliente.zap_marketing()
