def mostrar_menu():
    print("Menu:")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Editar Usuário")
    print("4. Remover Usuário")
    print("5. Sair")

def adicionar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    if nome in usuarios:  # Verifica se o nome já existe
        print("Usuário já existe. Tente outro nome.")
        return
    idade = input("Digite a idade do usuário: ")
    if not idade.isdigit():  # Verifica se a idade é um número
        print("Idade deve ser um número.")
        return
    usuarios[nome] = idade  # Adiciona o usuário ao dicionário
    print("Usuário adicionado com sucesso!")

def listar_usuarios(usuarios):
    if not usuarios:  # Verifica se há usuários cadastrados
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for nome, idade in usuarios.items():  # Itera sobre o dicionário para listar usuários
        print(f"Nome: {nome}, Idade: {idade}")

def editar_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja editar: ")
    if nome not in usuarios:  # Verifica se o usuário existe
        print("Usuário não encontrado!")
        return
    nova_idade = input("Digite a nova idade: ")
    if not nova_idade.isdigit():  # Verifica se a nova idade é um número
        print("Idade deve ser um número.")
        return
    usuarios[nome] = nova_idade  # Atualiza a idade do usuário
    print("Usuário atualizado com sucesso!")

def remover_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja remover: ")
    if nome in usuarios:  # Verifica se o usuário existe
        usuarios.pop(nome)  # Remove o usuário do dicionário
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado!")

def main():
    usuarios = {}  # Dicionário para armazenar os usuários
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if not opcao.isdigit():  # Verifica se a opção é um número
            print("Opção inválida! Por favor, digite um número.")
            continue
        opcao = int(opcao)
        if opcao == 5:  # Sai do sistema
            print("Saindo do sistema...")
            break
        elif opcao == 1:
            adicionar_usuario(usuarios)
        elif opcao == 2:
            listar_usuarios(usuarios)
        elif opcao == 3:
            editar_usuario(usuarios)
        elif opcao == 4:
            remover_usuario(usuarios)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

''' Liste os erros encontrados:
# erro troquei "[]" por "{}""
# erro: faltou o ":"
# erro: tinha um "not"
# erro: faltao o "else"
#erro de escrita
# mudei a forma listar
#adicionei um else
# erro: tirei o not
# Erro linha 60: saida estava com opção 0 no inicio ao invez de 5 no final
# Erro linha 42: usuários[nome] = nova_idade procura índice por string
# Erro linha 49: Pop não faz sentido
# Erro linha 76: Main faltando
# Error linha 49: adicionado o loop
# erro: trazendo a opçãoo certa, erro: trocando por elif
'''
# Quantidade de erros encontrados:14
# Tempo gasto: 1 hora e 28 minutos
# O codigo funciona perfeitamente? +/-

