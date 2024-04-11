class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques_diarios = 0

    def deposito(self, valor):
        if valor < 0:
            print("Operação não permitida. O valor informado é invalido.")
        else:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
            self.extrato()

    def saque(self, valor):
        if self.saques_diarios < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques_diarios += 1
            print(f"Saque de R${valor} realizado com sucesso.")
            self.extrato()
        elif self.saldo < valor:
            print("Operção não realizada. Saldo insuficiente.")
        else:
            print("Operação não realizada. Valor do saque excede o limite,  ou numero maximo de saques diarios exedidos.")

    def extrato(self):
        print(f"Saldo disponível: R${self.saldo}")
        print(f"Saques realizados hoje: {self.saques_diarios}")


conta = ContaBancaria()
conta.deposito(2000)
conta.saque(500)
conta.saque(500)
conta.saque(300)
conta.saque(200)
