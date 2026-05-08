from abc import ABC, abstractmethod
from datetime import datetime, date


class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: date,
        endereco: str,
    ):
        super().__init__(endereco)

        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._numero = numero
        self._cliente = cliente

        self._saldo = 0.0
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False

        if self._saldo < valor:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        print("Saque realizado com sucesso!")
        return True

    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False

        self._saldo += valor
        print("Depósito realizado com sucesso!")
        return True


class ContaCorrente(Conta):
    def __init__(
        self,
        numero: int,
        cliente: Cliente,
        limite: float = 500,
        limite_saques: int = 3,
    ):
        super().__init__(numero, cliente)

        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor: float):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == "Saque"
            ]
        )

        if valor > self.limite:
            print("Valor do saque excede o limite.")
            return False

        if numero_saques >= self.limite_saques:
            print("Número máximo de saques excedido.")
            return False

        return super().sacar(valor)


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
