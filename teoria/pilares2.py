# Exemplo de encapsulamento
print("\nExemplo de encapsulamento:")


class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print("conta: ")
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=2000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

print()

conta_do_zezinho = ContaBancaria(saldo=50)
print("conta do zezinho: ")
print(f"Saldo da conta bancária: {conta_do_zezinho.consultar_saldo()}")
