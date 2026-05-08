# Sistema Bancário - Modelo de Classes

## 1. Cliente
Representa um cliente do banco.

### Atributos
- endereco: str
- contas: list[Conta]

### Métodos
- realizar_transacao(conta: Conta, transacao: Transacao)
- adicionar_conta(conta: Conta)

---

## 2. PessoaFisica (herda de Cliente)
Representa um cliente pessoa física.

### Atributos
- cpf: str
- nome: str
- data_nascimento: date

---

## 3. Conta
Representa uma conta bancária.

### Atributos
- saldo: float
- numero: int
- agencia: str
- cliente: Cliente
- historico: Historico

### Métodos
- saldo(): float
- nova_conta(cliente: Cliente, numero: int): Conta
- sacar(valor: float): bool
- depositar(valor: float): bool

---

## 4. ContaCorrente (herda de Conta)
Conta com regras específicas de corrente.

### Atributos
- limite: float
- limite_saques: int

---

## 5. Historico
Armazena transações da conta.

### Atributos
- transacoes: list[Transacao]

### Métodos
- adicionar_transacao(transacao: Transacao)

---

## 6. Interface Transacao
Define comportamento de uma transação bancária.

### Métodos
- registrar(conta: Conta)

---

## 7. Deposito (implementa Transacao)
### Atributos
- valor: float

---

## 8. Saque (implementa Transacao)
### Atributos
- valor: float

---

# Relacionamentos principais

- Cliente possui 1..* Conta
- Conta pertence a 1 Cliente
- Conta possui 1 Historico
- Historico contém várias Transacoes
- Deposito e Saque implementam Transacao
- PessoaFisica herda de Cliente
- ContaCorrente herda de Conta
