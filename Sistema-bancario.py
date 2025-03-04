import datetime

def movimentacao(transacao, valor_adicionado, hora):
    transacao.append(valor_adicionado)
    hora.append(str(datetime.datetime.now().strftime('%d/%m/%y %H:%M')))
    return transacao

def extrato(transacoes, hora):
    i = 0
    print('\n',21*'=', 'EXTRATO', 21*'=')
    historico = ''
    for movimento in transacoes:
        historico += f'{hora[i]}\tSaque: R$ {(transacoes[i]*-1):.2f}' if transacoes[i] < 0 else f'{hora[i]}\tDepósito: R$ {transacoes[i]:.2f}\n'
        i += 1
    return historico

def saque(limite_diario, saque_diario, limite_saque):
        while True:
            if saque_diario <= 0:
                print('Você excedeu o limite de saques diários. Tente novamente amanhã.\n')
                continue

            while limite_diario > 0:
            
                valor = input('valor a ser sacado: ')
                try:
                    valor = float(valor)
                except ValueError:
                    print('Informe um saque válido.')
                    continue
                if saldo_da_conta - valor < 0:
                    print('Você não tem saldo suficiente.')
                    continue
                elif valor > limite_saque:
                    print('Você só pode fazer saques de até R$ 500,00.')
                    continue
                elif valor < 0:
                    print('Saque um valor positivo.')
                    continue
                movimentacao(transacao=transacoes, valor_adicionado=valor*(-1), hora=hora)
                print(f'Você sacou R$ {valor:.2f} da conta.\n')
                saque_diario -= 1
                limite_diario -= 1
                break
            return valor

def deposito(limite_diario):
    while limite_diario > 0:
        valor = input('Valor a ser depositado: ')
        try:
            valor = float(valor)
        except ValueError:
            print('Informe um depósito válido.')
            continue
        if valor < 0:
            print('Deposite um valor positivo.')
            continue
        movimentacao(transacao=transacoes, valor_adicionado=valor, hora=hora)
        print(f'Você depositou R$ {valor:.2f} na conta.\n')
        limite_diario -= 1
        break
    return valor

def criar_usuario(usuarios):
    CPF = input('Informe seu CPF:\n=> ')
    usuario = filtro_usuario(CPF, usuarios)
    
    if usuario:
        print('!!! CPF já cadastrado com outro usuário !!!\n')
        return
    nome = input('Informe seu nome completo:\n=> ')
    data_de_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa):\n=> ')
    endereco = input('Informe o seu endereço (logradouro, nº - bairro - cidade/UF):\n=> ')
    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': CPF, 'endereco': endereco}) 
    print('O usuário foi criado com sucesso.\n')

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtro_usuario(cpf,usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_da_conta': numero_da_conta, 'usuario': usuario} 
    print('!!! Usuário não encontrado !!!')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência: \t{conta['agencia']}
            C/c:\t{conta['numero_da_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print(linha)

recepcao = '''Olá, seja bem-vindo ao Sistema Bancário Valjr-py!
-------------------------------------------------
Selecione as ações a fazer:
[S]aque
[D]epósito
[E]xtrato
[C]riar usuário
[G]erar conta
[L]istar contas
[F]inalizar
'''
usuarios = []
transacoes = []
hora = []
contas = []
saque_diario = 3
LIMITE_SAQUE = 500
AGENCIA = '0001'
limite_transacoes_diaria = 10

while True:
    saldo_da_conta = float(sum(transacoes))
    acao_usuario = input(f'{recepcao}\n=> ').lower()

    if limite_transacoes_diaria < 1:
        print('Você não pode mais fazer transações. Tente  novamente amanhã.')
        continue

    if acao_usuario == 's':
        saque(limite_transacoes_diaria, limite_transacoes_diaria , LIMITE_SAQUE)

    elif acao_usuario == 'd':
        deposito(limite_diario=limite_transacoes_diaria)

    elif acao_usuario == 'e':
        if not transacoes:
            print(f'Você não fez nenhuma movimentação ainda.\n')
        else:
            print(extrato(transacoes=transacoes, hora=hora))
            print(f'\nSaldo: R$ {saldo_da_conta:.2f}\n',51*'=','\n')
    
    elif acao_usuario == 'c':
        criar_usuario(usuarios)

    elif acao_usuario == 'g':
        numero_da_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_da_conta, usuarios)
        if conta:
            contas.append(conta)

    elif acao_usuario == 'l':
        listar_contas(contas)
    
    elif acao_usuario == 'f':
        break

    else:
        print('Informe uma opção válida.\n')
        continue