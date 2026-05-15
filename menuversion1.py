version1

sair = False
while not sair == True:
    print('-='*10,'MENU','-='*10)
    print('1 - CADASTRAR')
    print('2 - MOSTRAR CADASTRO')
    print('3 - SAIR')
    opcao = int(input('OPÇÃO:'))
    if opcao == 1:
        nome = str(input('Digite o nome do aluno:'))
        sobreNome = str(input('Digite o sobrenome do aluno:'))
        matricula = int(input('Digite a matrícula do aluno:'))
        oficina = str(input('Digite a oficina do aluno voluntário :'))
        dataInicio = str(input('Informe a data de início da oficina:'))
        dataTermino = str(input('Informe a data de término da oficina:'))
    elif opcao == 2:
        print('Cadastro:')
        print('Aluno(a): ',nome,sobreNome)
        print('Matrícula:',matricula)
        print('Oficina:',oficina)
        print('Início:',dataInicio)
        print('Final: ' ,dataTermino)
    elif opcao == 3:
        sair = True
        print('-='*10,'FIM DO PROGRAMA','-='*10)