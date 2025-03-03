def movimentacao(transacao, valor_adicionado, nivelador_extrato):
    transacao.append(valor_adicionado)
    nivelador_extrato.append(0)
    return transacao
 
recepcao = '''Olá, seja bem-vindo ao Sistema Bancário Valjr-py!
-------------------------------------------------
Selecione as ações a fazer:
[S]aque
[D]epósito
[E]xtrato
[F]inalizar
'''

saques = []
depositos = []
saque_diario = 3
LIMITE_SAQUE = 500

while True:
    saldo_da_conta = float(sum(depositos))-float(sum(saques))

    acao_usuario = input(f'{recepcao}\n').lower()

    if acao_usuario == 's':
        if saque_diario <= 0:
            print('Você excedeu o limite de saques diários. Tente novamente amanhã.\n')
            continue

        while True:
        
            valor = input('Saldo a ser sacado: ')
            try:
                valor = float(valor)
            except ValueError:
                print('Informe um saque válido.')
                continue
            if saldo_da_conta - valor < 0:
                print('Você não tem saldo suficiente.')
                continue
            elif valor > LIMITE_SAQUE:
                print('Você só pode fazer saques de até R$ 500,00.')
                continue
            elif valor < 0:
                print('Saque um valor positivo.')
                continue
            movimentacao(transacao=saques, valor_adicionado=valor, nivelador_extrato=depositos)
            print(f'Você sacou R$ {valor:.2f} da conta.\n')
            saque_diario -= 1
            break

    elif acao_usuario == 'd':
        while True:
            valor = input('Saldo a ser depositado: ')
            try:
                valor = float(valor)
            except ValueError:
                print('Informe um depósito válido.')
                continue
            if valor < 0:
                print('Deposite um valor positivo.')
                continue
            movimentacao(transacao=depositos, valor_adicionado=valor, nivelador_extrato=saques)
            print(f'Você depositou R$ {valor:.2f} na conta.\n')
            break

    
    elif acao_usuario == 'e':
        print('   SAÍDAS     |    ENTRADAS')
        i = 0
        for historico in range(max(len(saques), len(depositos))):
            print(f'{i+1}. R$ {saques[i]:.2f}        R$ {depositos[i]:.2f}')
            i += 1
        print(f'\nSaldo da conta: R$ {saldo_da_conta}\n')
        print('\n')

    elif acao_usuario == 'f':
        break

    else:
        print('Informe uma opção válida.\n')
        continue

    # coloquei a recepção dentro do input
    # limitei a não depositar valores negativos
    # removi uma variável desnecessária
    # mudei a posição do tratamento de exceção, caso o usuário digite algum dígito diferente de um número na variável valor
    # deixei os parâmetros das funções mais descritivos
    # limitei a não sacar valores negativos