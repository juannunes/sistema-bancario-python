menu = """
-----------MENU-----------

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

--------------------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        deposito = float(input("Informe o valor do deposito :"))
        
        if deposito > 0:
           saldo+=deposito
           extrato+=f"Depósito de: R$ {deposito:.2f} \n"
           print("Depósito efetuado com sucesso!")

        else:
            print("Operação Falhou! O valor informado é invaldido.") 
             

    elif opcao == "2":
        saque = float(input("Informe o valor do saque : "))

        if saque < 0:
            print("Operação Falhou! O valor informado é invaldido.")

        elif saque <= limite:

            if numero_saques < LIMITE_SAQUES:

                if saque <= saldo:
                    extrato += f"Saque de: R$ {saque:.2f} \n"
                    saldo -= saque
                    numero_saques += 1
                    print("Saque efetuado com sucesso!")

                else:
                    print("Operação Falhou! Valor informado para saque é maior que o saldo.")

            else:
                print("Operação Falhour! A quantidade de saques por dia já foi efetuada.")

        else:
            print("Operação Falhour! O valor informado é maior que o limite por saque.")

    elif opcao == "3":
        print("\n#################### EXTRATO ####################")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo de: R$ {saldo:.2f}")
        print("###################################################")

    elif opcao == "0":
        break

    else:
        print("Opção Inválida, por favor selecione novamente a opção desejada.")