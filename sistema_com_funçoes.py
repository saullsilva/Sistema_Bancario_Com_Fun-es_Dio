menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova conta
[5] Criar Usuario
[6] Sair


=> """

saldo = 0
limite = 500
exibir_extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []

def conta_usuario():
    cpf = input("Registre o CPF: ")
    if cpf in lista_usuarios:
        print("CPF já em uso!")
        return
    
    nome = input("Registre o nome: ")
    nascimento = input("Registre a data de nascimento: ")
    estado = input("Informe o estado: ")

    lista_usuarios.append(cpf)
    print("Usuário registado com sucesso!")

def nova_conta():
    aumento_conta = 0
    numero_agencia = [1000]
    
    if not lista_usuarios: 
        print("Sem Utilizadores para conectar contas!")
        return

    print("Qual CPF deseja usar?")
    for indice, cpfusavel in enumerate(lista_usuarios):
        print(f"{indice} - {cpfusavel}")  
    
    escolha_cpf = input("")

    if escolha_cpf not in lista_usuarios:
        print("Nenhum CPF escolhido!")
        return
    else:
        aumento_conta += 1
        print("Conexão Feita!")
        print(f"Número da conta: {aumento_conta} ")
        print(f"Número da agência: {numero_agencia[0]}")


def depositar(saldo, exibir_extrato, /):
    valor = float(input("Informe o valor do depósito: \n"))
    if valor > 0:
        saldo = valor + saldo
        exibir_extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print(f"O valor {valor} é inválido para esta operação!")

    return saldo, exibir_extrato


def sacar(*, saldo, exibir_extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("Atingiu o limite de saques diários!")
        return saldo, exibir_extrato, numero_saques

    retirado = float(input("Quanto você deseja retirar? (MÁXIMO R$500.00) \n"))
    
    if retirado > limite:
        print("Falha! O valor do saque excede o limite de R$ 500,00.")
    elif retirado > saldo:
        print("Falha! Não tem saldo suficiente.")
    elif retirado > 0:
        saldo -= retirado
        exibir_extrato += f"Saque: R$ {retirado:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, exibir_extrato, numero_saques


def extrato(saldo, /, *, exibir_extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not exibir_extrato else exibir_extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


while True:
    
    opcao = input(menu)

    if opcao == "1":
        saldo, exibir_extrato = depositar(saldo, exibir_extrato)

    elif opcao == "2":
        saldo, exibir_extrato, numero_saques = sacar(saldo=saldo, exibir_extrato=exibir_extrato, numero_saques=numero_saques)
    
    elif opcao == "3":
        extrato(saldo, exibir_extrato=exibir_extrato)

    elif opcao == "4":
        nova_conta()

    elif opcao == "5":
        conta_usuario()

    elif opcao == "6":
        print("Fim da operação!")
        break
    
    else:
        print("Não digitou nenhuma das opções válidas!")