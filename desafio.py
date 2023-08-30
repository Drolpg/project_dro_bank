saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
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
        print("Saldo")

    elif opcao == "2":
        print("Saque")

    elif opcao == "3":
        print("Deposito")
    
    elif opcao == "4":
        print("Extrato")

    elif opcao == "0":
        print("Finalizando o Sistema...")
        break

    else:
        print("!Operação invalida, por favor selecione novamente a operação desejada.")