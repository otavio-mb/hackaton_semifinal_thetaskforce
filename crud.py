# Sistema de CRUD simples com dicionário CORRIGIDO

usuarios = {} # erro troquei "[]" por "{}""

def mostrar_menu():# erro: faltou o ":"
    print("Menu:")
    print("1. Adicionar Usuário")
    print("2. Listar Usuários")
    print("3. Editar Usuário")
    print("4. Remover Usuário")
    print("5. Sair")

def adicionar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    if nome in usuarios:# erro: tinha um "not"
        print("Usuário já existe. Tente outro nome.")
        return
    else:# erro: faltao o "else"
        idade = input("Digite a idade do usuário: ")
        if not idade.isdigit():  
            print("Idade deve ser um número.")
            return
        usuarios[nome] = idade 
        print("Usuário adicionado com sucesso!")#erro de escrita

def listar_usuarios(usuarios):
    if not usuarios: 
        print("Nenhum usuário cadastrado.")
        return
    else: # mudei a forma listar
        for nome, idade in usuarios.items():                  
            print(f"{nome}_{idade}")

def editar_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja editar: ")
    if nome not in usuarios: 
        print("Usuário não encontrado!")
        return
    else:
        nova_idade = input("Digite a nova idade: ")
        if not nova_idade.isdigit():  
            print("Idade deve ser um número.")
            return
        else: #adicionei um else
            usuarios[nome] = nova_idade 
            print("Usuário atualizado com sucesso!")

def remover_usuario(usuarios):
    nome = input("Digite o nome do usuário que deseja remover: ")
    if nome in usuarios:# erro: tirei o not
        usuarios.pop(nome) 
        return True 
    else:
        print("Usuário não encontrado!")


def main():
    while True:
        mostrar_menu() 
        opcao = input("Escolha uma opção: ")
        if not opcao.isdigit():  
            print("Opção inválida! Por favor, digite um número.")
            continue
        opcao = int(opcao)  
        if opcao == 1:
            adicionar_usuario(usuarios)
        elif opcao == 2:
            listar_usuarios(usuarios)
        elif opcao == 3:
            editar_usuario(usuarios)
        elif opcao == 4:
            remover_usuario(usuarios)
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

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