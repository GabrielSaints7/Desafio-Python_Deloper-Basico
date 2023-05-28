""" Sistemas de Banco
    - Saque:
        - 3 saques diarios, com limite de R$500
        - caso saldo negativo, informar ao usuário,
        - 'todos os saques devem ser armazenados em variavel uma variavel e informar na operação extrato
    - Deposito:
        - valor positivo
        - salvar quantidade e valor deposito
    - Saldo:
        - Listar todos as operações na conta
        - e no final da listagem informar o saldo atual da conta
        - deve ser exibidos no formato R$ xxx.xx
"""

# Operação de deposito
saldo_conta = 0
extrato = []
opcao = -1

quantidade_saque_dia = 0

while opcao != 0:
    opcao = int(input('''
    Escolha uma opcao:
    - 1 para depositar
    - 2 para sacar
    - 3 para extrato
    - 0 para sair
    
    opcao desejada: '''))
    if opcao == 1:
        deposito = int(input('Digite o valor de deposito: '))
        if deposito > 0:
            saldo_conta += deposito
            extrato.append(f'Deposito: + R${deposito}')
        else:
            print('Digite um valor válido\n')
    elif opcao == 2:

        saque = int(input('Digite o valor de saque: '))
        if ((saque < 500) and (quantidade_saque_dia < 3) and (saque > 0)):
            if saldo_conta < 0:
                print('Sem saldo em conta!\n')
            else:
                saldo_conta -= saque
                quantidade_saque_dia += 1
                extrato.append(f'Saque: - R${saque}')
        elif saque >= 500:
            print('Valor maior que limite por saque!\n')

        elif saque > saldo_conta:
            print('Valor maior que saldo em conta!\n')

        elif quantidade_saque_dia == 3:
            print('3 saque diarios atingido! Retorne amanhã\n')
        else:
            print('Digite um valor válido!\n')

    elif opcao == 3:
        print('extrato'.center(15,'_'))
        for num in extrato:
            print(num)
        print(f'\nSaldo atual R${saldo_conta:.2f}')
        print('_'.center(15,'_'))
    
    else:
        print('Digite um valor de opcao válido!')