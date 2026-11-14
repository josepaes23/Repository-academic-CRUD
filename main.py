import string
import secrets

opcao = 0
senha = ""
senhaTitulo = ""
senhaTituloAntiga = ""
senhaAlfabeto = string.ascii_letters
senhaNumero = string.digits
senhaSimbolo = string.punctuation


while opcao != 5:
    pass
    print("""1. Criar senha
2. Ver senhas criadas
3. Modificar senha
4. Deletar senha
5. Sair
    """)
    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        opcaoSenha = 0
        senhaTituloAntiga = senhaTitulo
        senhaTitulo = input("Digite o titulo da senha: ")
        quantidadeCaractere = int(input("Digite a quantidade de caracteres da senha: "))
        print("""
1. Somente números
2. Somente letras
3. Somente símbolos
4. Números e letras
5. números e símbolos
6. Letras e símbolos
7. Números, letras e símbolos
""")
        opcaoSenha = int(input("Digite a opção desejada: "))
        match opcaoSenha:
            case 1:
                senha = ''.join(secrets.choice(senhaNumero) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue
            case 2:
                senha = ''.join(secrets.choice(senhaAlfabeto) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue
            case 3:
                senha = ''.join(secrets.choice(senhaSimbolo) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue
            case 4:
                senha = ''.join(secrets.choice(senhaNumero + senhaAlfabeto) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue   
            case 5:
                senha = ''.join(secrets.choice(senhaNumero + senhaSimbolo) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue
            case 6:
                senha = ''.join(secrets.choice(senhaSimbolo + senhaAlfabeto) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue
            case 7:
                senha = ''.join(secrets.choice(senhaNumero  + senhaAlfabeto + senhaSimbolo) for i in range(quantidadeCaractere))
                print("\nSenha criada com sucesso!\n")
                continue
            case default:
                print("ERRO! Opção incorreta. ")
                senhaTitulo = senhaTituloAntiga

        

    elif opcao == 2:

        if senha != "":
            print("Senhas criadas: \n")
            print("Título: ", senhaTitulo)
            print("Senha: ", senha)
            print("\n\n")
        else:
            print("\nNenhuma senha criada!\n")

        

    elif opcao == 3:
        opcaoSenha = 0
        senhaTituloAntiga = senhaTitulo
        senhaTitulo = input("Digite o titulo da senha que voce quer modificar: ")

        if senhaTitulo != senhaTituloAntiga:
            print("Erro. Essa senha não existe.")
            senhaTitulo = senhaTituloAntiga
            continue
        elif senha == "":
            print("Não existe senha criada")
            senhaTitulo = senhaTituloAntiga
            continue

        quantidadeCaractere = int(input("Digite a quantidade de caracteres da senha: "))
        print("""
1. Somente números
2. Somente letras
3. Somente símbolos
4. Números e letras
5. números e símbolos
6. Letras e símbolos
7. Números, letras e símbolos
""")
        opcaoSenha = int(input("Digite a opção desejada: "))
        match opcaoSenha:
            case 1:
                senha = ''.join(secrets.choice(senhaNumero) for i in range(quantidadeCaractere))
                print("Senha modificada!")
                continue
            case 2:
                senha = ''.join(secrets.choice(senhaAlfabeto) for i in range(quantidadeCaractere))
                print("Senha modificada!")
                continue
            case 3:
                senha = ''.join(secrets.choice(senhaSimbolo) for i in range(quantidadeCaractere))
                print("Senha modificada!")                
                continue
            case 4:
                senha = ''.join(secrets.choice(senhaNumero + senhaAlfabeto) for i in range(quantidadeCaractere))
                print("Senha modificada!")                
                continue   
            case 5:
                senha = ''.join(secrets.choice(senhaNumero + senhaSimbolo) for i in range(quantidadeCaractere))
                print("Senha modificada!")                
                continue
            case 6:
                senha = ''.join(secrets.choice(senhaSimbolo + senhaAlfabeto) for i in range(quantidadeCaractere))
                print("Senha modificada!")
                continue
            case 7:
                senha = ''.join(secrets.choice(senhaNumero  + senhaAlfabeto + senhaSimbolo) for i in range(quantidadeCaractere))
                print("Senha modificada!")
                continue
            case default:
                print("ERRO! Opção incorreta. ")
                senhaTitulo = senhaTituloAntiga

    elif opcao == 4:
        senhaTituloAntiga = senhaTitulo
        senhaTitulo = input("Digite o titulo da senha que voce quer deletar: ")

        if senhaTitulo != senhaTituloAntiga:
            print("Essa senha nao existe!")
            senhaTitulo = senhaTituloAntiga
            continue
        elif senha == "":
            print("Não existe senha criada")
            senhaTitulo = senhaTituloAntiga
            continue

        senha = ""
        print("\nSenha excluida com sucesso!\n")

        




