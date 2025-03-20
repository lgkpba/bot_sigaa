def menu():
    
    print("----------------------------------------")
    print("Primeiro vamos salvar suas informações!")
    matricula = input("Digite sua matrícula: ")
    cpf = input("Digite seu cpf: ")
    dataNascimento = input("Digite sua data de nascimento (dd/mm/aaa): ")
    senha = input("Digite sua senha: ")
    print("----------------------------------------")
    materia = input("Em que matéria vc deseja se matricular?")
    print("----------------------------------------")
    print("Caso não deseje preencher algum(ns) dos campos a seguir, deixe-o(s) em branco")
    professor = input("Informe o professor: ")
    horario = input("Informe o horario (seguindo o padrão do sigaa): ")
        
    dadosPessoais = [matricula, cpf, dataNascimento, senha]
    dadosMateria = [materia, (professor,horario)]
    
    return [dadosPessoais, dadosMateria]
    
print(menu()) 
