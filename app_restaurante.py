import os

restaurantes = []

def exibir_nome_do_programa():
    print('𝒮𝒶𝒷𝑜𝓇 𝐸𝓍𝓅𝓇𝑒𝓈𝓈𝑜\n')

def exibir_opcoes():
    """Função responsável por exibir as funções básicas da aplicação."""
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar/Desativar Restaurante")
    print("4. Sair\n")

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante.
    INPUTS:
    -Nome do restaurante.
    -Categoria.
    OUTPUT:
    -Adiciona um novo restaurante a lista dos restaurantes.
    """
    exibir_subtitulo("Cadastrar Novo Restaurante")
    nome_do_restaurante = input("Nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()

def listar_restaurantes():
    """Essa função é a responsável por listar os restaurantes."""
    exibir_subtitulo("Listando Restaurantes")
    print(f"{'Nome do Restaurante'.ljust(30)} | {'Categoria'.ljust(20)} | {'Status'.ljust(10)}")
    print("-" * 70)
    for restaurante in restaurantes:
        nome_formatado = restaurante['nome'].ljust(30)
        categoria_formatada = restaurante['categoria'].ljust(20)
        status_formatado = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f"{nome_formatado} | {categoria_formatada} | {status_formatado.ljust(20)}")

    input("\nDigite uma tecla para voltar ao menu principal.")
    main()

def alternar_estado_restaurante():
    """Essa função alterna o estado dos restaurantes.(ativa e desativa.)"""
    exibir_subtitulo("Alternando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado:")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante["nome"].lower():
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print(f"Restaurante {nome_restaurante} não encontrado.")

    input("\nDigite uma tecla para voltar ao menu principal.")
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def finalizar_app():
    exibir_subtitulo("Finalizando App")

def opcao_invalida():
    print("Opção inválida!\n")
    input("Digite uma tecla para voltar ao menu principal.")
    main()

def exibir_subtitulo(texto):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\n----- {texto} -----\n")

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    