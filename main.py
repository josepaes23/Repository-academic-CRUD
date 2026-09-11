import string
import secrets

opcao = 0
cofreSenha = dict()
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
        senhaTitulo = input("Digite o titulo da senha: ")
        
        respostaNumero = input("Deseja numeros na senha (S/N)? ")
        respostaLetras = input("Deseja letras na senha (S/N)? ")
        quantidadeCaractere = int(input("Digite a quantidade de caracteres: "))
        if (respostaNumero == 'S' and respostaLetras == 'S'):
            cofreSenha[senhaTitulo] = ''.join(secrets.choice(senhaAlfabeto + senhaNumero) for i in range(quantidadeCaractere))
        elif (respostaNumero == 'S'):
            cofreSenha[senhaTitulo] = ''.join(secrets.choice(senhaNumero) for i in range(quantidadeCaractere))
        elif (respostaLetras == 'S'):
            cofreSenha[senhaTitulo] = ''.join(secrets.choice(senhaAlfabeto) for i in range(quantidadeCaractere))
        else:
            print("Erro. Digite novamente!")

        print("\nSenha criada com sucesso!\n")

    elif opcao == 2:

        if cofreSenha != []:
            print("Senhas criadas: \n")
            print(cofreSenha)
            print("\n\n")
        else:
            print("\nNenhuma senha criada!\n")

        

    elif opcao == 3:

        senhaTitulo = input("Digite o titulo da senha que voce quer modificar: ")

        if senhaTitulo not in cofreSenha:
            print("Erro. Essa senha não existe.")
            continue

        respostaNumero = input("Deseja numeros na senha (S/N)? ")
        respostaLetras = input("Deseja letras na senha (S/N)? ")
        quantidadeCaractere = int(input("Digite a quantidade de caracteres: "))

        if (respostaNumero == 'S' and respostaLetras == 'S'):
            cofreSenha[senhaTitulo] = ''.join(secrets.choice(senhaAlfabeto + senhaNumero) for i in range(quantidadeCaractere))
        elif (respostaNumero == 'S'):
            cofreSenha[senhaTitulo] = ''.join(secrets.choice(senhaNumero) for i in range(quantidadeCaractere))
        elif (respostaLetras == 'S'):
            cofreSenha[senhaTitulo] = ''.join(secrets.choice(senhaAlfabeto) for i in range(quantidadeCaractere))
        else:
            print("Erro. Tente novamente!")
        print("\nSenha alterada com sucesso!\n")

    elif opcao == 4:
        senhaTitulo = input("Digite o titulo da senha que voce quer deletar: ")

        if senhaTitulo not in cofreSenha:
            print("Essa senha nao existe!")
            continue

        cofreSenha.pop(senhaTitulo)
        print("\nSenha excluida com sucesso!\n")

        




