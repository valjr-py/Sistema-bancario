def movimentacao(x, y):
    x.append(y)
    return x
 
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

    print(recepcao)
    acao_usuario = input().lower()

    if acao_usuario == 's':
        if saque_diario <= 0:
            print('Você excedeu o limite de saques diários. Tente novamente amanhã.\n')
            continue

        while True:
        
            valor = input('Saldo a ser sacado: ')
            try:
                valor = float(valor)
                if saldo_da_conta - valor < 0:
                    print('Você não tem saldo suficiente.')
                    continue
                if valor > LIMITE_SAQUE:
                    print('Você só pode fazer saques de até R$ 500,00.')
                    continue
            except ValueError:
                print('Informe um saque válido.')
                continue
            valor_saida = movimentacao(x=saques, y=valor)
            depositos.append(0)
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
            valor_saida = movimentacao(x=depositos, y=valor)
            saques.append(0)
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