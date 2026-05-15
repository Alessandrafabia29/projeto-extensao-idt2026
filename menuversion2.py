

sair = False
while not sair == True:
    print('\033[32m-='*10,'MENU','-='*10)
    print('\033[m1 - CADASTRAR')
    print('2 - CADASTRAR OPÇÕES AVANÇADAS')
    print('3 - MOSTRAR CADASTRO')
    print('4 - MOSTRAR CADASTRO OPÇÕES AVANÇADAS')
    print('5 - SAIR')
    opcao = int(input('OPÇÃO:'))
    if opcao == 1:
        nome = str(input('Digite o nome do aluno:'))
        sobreNome = str(input('Digite o sobrenome do aluno:'))
        matricula = int(input('Digite a matrícula do aluno:'))
        disciplinaVinc = str(input('Disciplina Vinculada: '))
        monitor = str(input('Monitor: '))
        oficina = str(input('Digite a oficina do aluno voluntário :'))
        dataInicio = str(input('Informe a data de início da oficina:'))
        dataTermino = str(input('Informe a data de término da oficina:'))
    if opcao == 2:
        cadastroProg = str(input('Cadastrar Programas: OPÇÕES:[1]PROGRAMAS DE EXTENSÃO [2]PROGAMAS LABOT [3]PROGAMAS EDUCACIONAIS--'))
        cadastroAcoes = str(input('Cadastrar Ações:[1]AÇÃO VOLUNTÁRIA [2]AÇÃO VINCULADA À PROJETO--'))
        voluntario = str(input('Nome do voluntário:'))
        periodoInicio = int(input('data início: '))
        periodoTermino = int(input('data término:'))
        temas = str(input('Escolha de temas-OPÇÃO: [1]VINCULADO À DISCIPLINA [2]ATUAIS [3]DISCIPLINARES [4]SOCIAIS--'))
    elif opcao == 3:
        print('Cadastro:')
        print('Aluno(a): ',nome,sobreNome)
        print('Matrícula:',matricula)
        print('Disciplina Vinculada : ',disciplinaVinc)
        print('Monitor: ' , monitor)
        print('Oficina:',oficina)
        print('Início:',dataInicio)
        print('Final: ' ,dataTermino)
    elif opcao == 4:
        print('CADASTRO OPÇÕES AVANÇADAS:')
        print('CADASTRAR PROGRAMAS: ',cadastroProg)
        print('CADASTRAR AÇÕES: ', cadastroAcoes)
        print('VOLUNTÁRIO: ',voluntario)
        print('período inicial:',periodoInicio)
        print('período final: ' , periodoTermino)
        print('Temas: ' , temas)
    elif opcao == 5:
        sair = True
        print('\033[32m-='*10,'FIM DO PROGRAMA','-='*10)
    
