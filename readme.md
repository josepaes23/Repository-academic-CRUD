Cofre de senhas - CRUD

IDEIA:

Programa rodado em terminal com o objetivo de criar, ver, modificar e deletar senhas.


ESBOÇO:

Onde os dados serão guardados?

--> Constantes:

    - senhaAlfabeto --> Alfabeto completo, incluindo maiúsculas e minúsculas
    - senhaNumero --> Numeros inteiros de 1 a 9
    - senhaSimbolo --> Caracteres especiais (Ainda não estão sendo usados no programa)

--> Variáveis de identidade:

    - cofreSenha --> Dicionário que guarda o título e a senha correspondente
    - senhaTitulo --> Chave do dicionário do tipo inteiro que guarda o título da senha
    - senhaCaractere --> variável do tipo inteiro que guarda a quantidade de caracteres da senha

--> Variáveis de fluxo do programa:

    - opcao --> Variável do tipo integer que guarda o número do evento que o usuário deseja acessar, as quais são: 1. Criar senha; 2. Ver senhas criadas; 3 Modificar senha; 4. Deletar senha; 5. Sair. 
    - respostaLetras --> Variável do tipo string que armazena a resposta 'S' ou 'N' para inserir ou não letras na senha.
    - respostaNumero --> Variável do tipo string que armazena a resposta 'S' ou 'N' para inserir ou não números na senha.

Como o app tomará decisões de fluxo?

--> Escolher as funcionalidades do programa:
    - Estrutura de repetição While, usada para perguntar ao usuário qual funcionalidade ele deseja acessar e repetindo essa ação até que o usuário esolha a opção "5. Sair"
    - Estrutura de decisão if/else, usada para acessar cada opção que o usuário escolher, exceto a opção 5, já definida como condição na estrutura While

--> Criar senha?

    - Estrutura de decisão if/else, usada para criar a senha com base nas preferências de usuário em relação a quantidade de caracteres e inserção de letras e/ou números, baseada na resposta 'S' ou 'N'

--> Ver senhas criadas:

    - Estrutura de decisão if/else, usada para olhar o dicionário cofreSenha, e se não tiver valor no dicionário, imprimir "Nenhuma senha criada!"

--> Modificar senhas:

    - Estrutura de decisão if/else, usada para seguir o fluxo de atualização do dicionário cofreSenha, de acordo com as preferências do usuário em relação a quantidade de caracteres e inserção de letras e/ou números, baseada na resposta 'S' ou 'N'
    - Se não houver o título correspondente a senha no dicionário, o programa imprime "Erro. Essa senha não existe."

--> Deletar senhas:

    - Estrutura de decisão if/else  usada para seguir o fluxo de deletar o título e senha correspondente, usando o pop() para deletar a chave do dicionário


Bibliotecas:

--> Biblioteca string:

    - Usada para inserir o alfabeto, os números e os caracteres especiais no programa, de acordo com a ASCII
    - Comandos: string.ascii_letters, string.digits, string.punctuation

--> Biblioteca secrets:
    - Usada para criar senhas de forma mais segura
    - comando: secrets.choice(preferências definidas pelo usuário)
    - Método .join() foi usado para juntar os caracteres criados para a senha em uma estrutura de repetição for, que vai de 0 até a quantidade de caracteres - 1