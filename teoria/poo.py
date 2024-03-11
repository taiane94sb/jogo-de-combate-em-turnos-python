# POO

# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos


pessoa1 = Pessoa("Taiane", 29)
print("Nome: ", pessoa1.nome)
print("Idade: ", pessoa1.idade)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Matheus", 24)
print("Nome: ", pessoa2.nome)
print("Idade: ", pessoa2.idade)
mensagem = pessoa1.saudacao()
print(mensagem)
