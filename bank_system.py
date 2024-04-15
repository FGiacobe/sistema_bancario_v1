# Desafio de um Sistema Bancário com os cohecimentos básicos de Python.

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
Digite sua opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    option = input(menu)

    if option == "1":
        deposito = float(input("informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"\n*** Depósito de R$ {deposito:.2f} efetuado com sucesso! ***")

        else:
            print("\n*** A operação falhou, o valor informado é inválido. ***")

    elif option == "2":
        saque = float(input("informe o valor do saque: "))

        if saque > 0:

            excedeu_saldo = saque > saldo
            excedeu_limite = saque > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\n*** Saldo insuficiente na conta. ***")
            elif excedeu_limite:
                print("\n*** O valor solicitado excede o limite de saque. ***")
            elif excedeu_saques:
                print("\n*** Limite de saques diário excedido. ***")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                print(f"\n*** Saque de R$ {saque:.2f} efetuado com sucesso! ***")

        else:
            print("\n*** A operação falhou, o valor informado é inválido. ***")

    elif option == "3":
        print(" E X T R A T O ".center(40, "*"))
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(40 * "*")

    elif option == "0":
        break

    else:
        print("\n*** A operação falhou, a opção informada é inválida. ***")
