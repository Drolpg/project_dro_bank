saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque_efetuado = 0
quat_saque = 0
quant_deposito = 0
menu = """
Bem Vindo ao Dro Bank... 

digite a opção desejada:
[1] - Saldo
[2] - Saque
[3] - Deposito
[4] - Extrato
[0] - Finalizar sessão

"""


while True:
    opcao = input(menu)
    if opcao == "1":
        print(f"Saldo: {saldo:.2f}")

    elif opcao == "2":
        if saque_efetuado <= LIMITE_SAQUES:
            print(
                f"Você ja efetuo {saque_efetuado} Hoje... O Limite é de 3 saques diarios")
            valor_saque = int(input("Digite o valor desejado: "))
            if valor_saque > saldo:
                print(
                    f"Operação não realizada saldo insuficiente... Saldo atual: {saldo:.2f}")
            else:
                saldo = saldo - valor_saque
                saque_efetuado = saque_efetuado + 1
                print(
                    f"Operação realizada com SUCESSO... Saque efetuado no valor de {valor_saque:.2f} Saldo atial: {saldo:.2f}")
                quat_saque = quat_saque + 1
        else:
            print("Limite de saque atingido... tente novamente amanha.")

    elif opcao == "3":
        print("Deposito")
        valor_deposito = int(input("Digite o valor que deseja depositar: "))
        saldo = saldo + valor_deposito
        print(
            f"Operação realizada com SUCESSO... Deposito efetuado no valor de {valor_deposito:.2f} Saldo atial: {saldo:.2f}")
        quant_deposito = quant_deposito = + 1

    elif opcao == "4":
        print(
            f"Extrato... - Quantidade de saque: {quat_saque} - Quantidade de depositos: {quant_deposito} - Saldo atual: {saldo:.2f}")

    elif opcao == "0":
        print("Finalizando o Sistema...")
        saque_efetuado = 0
        break

    else:
        print("!Operação invalida, por favor selecione novamente a operação desejada.")
