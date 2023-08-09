menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

valor_deposito = 0
valor_saque = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Qual o valor para depósito?"))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Valor inválido")

    elif opcao == "s":
       
        while numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Informe o valor do saque:"))
            
            if valor_saque <= saldo and valor_saque <= limite and valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print("Sacando...")
                break
            
            elif valor_saque > saldo or valor_saque > limite:
                print("Saldo ou limite insuficiente!")
                break

            else:
                print("Operação falhou! O valor é inválido!")
                break
        
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu seu limite de saques diários.")
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")