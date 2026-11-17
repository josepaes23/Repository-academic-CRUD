import string
import secrets

opcao = "0"
cofreSenha = dict()
senhaAlfabeto = string.ascii_letters
senhaNumero = string.digits
senhaSimbolo = string.punctuation


while opcao != "5":
    pass
    print("""1. Criar senha
2. Ver senhas criadas
3. Modificar senha
4. Deletar senha
5. Sair
    """)
    opcao = input("Escolha a opção: ")

    if opcao == "1":
        senhaTitulo = input("Digite o titulo da senha: ")
        
        if senhaTitulo.strip() in cofreSenha:
            print("Erro. Essa senha existe.\n")
            continue
        
        quantidadeCaractere = input("Digite a quantidade de caracteres da senha: ")

        if quantidadeCaractere.isdigit() == False:
            print("ERRO: a quantidade de caracteres precisa ser um numero inteiro positivo.\n")
            continue
        
        print("""
        1. Somente números
        2. Somente letras
        3. Somente símbolos
        4. Números e letras
        5. números e símbolos
        6. Letras e símbolos
        7. Números, letras e símbolos
        """)
        opcaoSenha = input("Digite a opção desejada: ")
        match opcaoSenha:
            case "1":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero) for i in range(int(int(quantidadeCaractere))))
                print("Senha criada com sucesso!\n")
                continue
            case "2":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaAlfabeto) for i in range(int(quantidadeCaractere)))
                print("Senha criada com sucesso!\n")
                continue
            case "3":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaSimbolo) for i in range(int(quantidadeCaractere)))
                print("Senha criada com sucesso!\n")                
                continue
            case "4":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero + senhaAlfabeto) for i in range(int(quantidadeCaractere)))
                print("Senha criada com sucesso!\n")                
                continue   
            case "5":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero + senhaSimbolo) for i in range(int(quantidadeCaractere)))
                print("Senha criada com sucesso!\n")                
                continue
            case "6":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaSimbolo + senhaAlfabeto) for i in range(int(quantidadeCaractere)))
                print("Senha criada com sucesso!\n")
                continue
            case "7":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero  + senhaAlfabeto + senhaSimbolo) for i in range(int(quantidadeCaractere)))
                print("Senha criada com sucesso!\n")
                continue
            case default:
                print("ERRO! Opção incorreta.\n")

    elif opcao == "2":

        if cofreSenha != {}:
            print("Senhas criadas: \n")
            print(cofreSenha)
            print("\n\n")
        else:
            print("\nNenhuma senha criada!\n")

        

    elif opcao == "3":
        senhaTitulo = input("Digite o titulo da senha que voce quer modificar: ")

        if senhaTitulo.strip() not in cofreSenha:
            print("Erro. Essa senha não existe.\n")
            continue

        quantidadeCaractere = input("Digite a quantidade de caracteres da senha: ")

        if quantidadeCaractere.isdigit() == False:
            print("ERRO: a quantidade de caracteres precisa ser um numero inteiro positivo.\n")
            continue

        print("""
        1. Somente números
        2. Somente letras
        3. Somente símbolos
        4. Números e letras
        5. números e símbolos
        6. Letras e símbolos
        7. Números, letras e símbolos
        """)
        opcaoSenha = input("Digite a opção desejada: ")
        match opcaoSenha:
            case "1":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero) for i in range(int(int(quantidadeCaractere))))
                print("Senha modificada com sucesso!\n")
                continue
            case "2":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaAlfabeto) for i in range(int(quantidadeCaractere)))
                print("Senha modificada com sucesso!\n")
                continue
            case "3":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaSimbolo) for i in range(int(quantidadeCaractere)))
                print("Senha modificada com sucesso!\n")                
                continue
            case "4":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero + senhaAlfabeto) for i in range(int(quantidadeCaractere)))
                print("Senha modificada com sucesso!\n")                
                continue   
            case "5":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero + senhaSimbolo) for i in range(int(quantidadeCaractere)))
                print("Senha modificada com sucesso!\n")                
                continue
            case "6":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaSimbolo + senhaAlfabeto) for i in range(int(quantidadeCaractere)))
                print("Senha modificada com sucesso!\n")
                continue
            case "7":
                cofreSenha[senhaTitulo.strip()] = ''.join(secrets.choice(senhaNumero  + senhaAlfabeto + senhaSimbolo) for i in range(int(quantidadeCaractere)))
                print("Senha modificada com sucesso!\n")
                continue
            case default:
                print("ERRO! Opção incorreta.\n")

    elif opcao == "4":
        senhaTitulo = input("Digite o titulo da senha que voce quer deletar: ")

        if senhaTitulo.strip() not in cofreSenha:
            print("Essa senha nao existe!\n")
            continue

        cofreSenha.pop(senhaTitulo.strip())
        print("\nSenha excluida com sucesso!\n")

    elif opcao == "5":
        print("Saindo...")

    else:
        print("ERRO: Tente novamente!\n")

        




