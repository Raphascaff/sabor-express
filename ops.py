from utils import limpa_tela, retorna_ao_menu, exibir_subTitulos
from crud_restaurante import cadastrar_restaurante, listar_restaurantes

def exibir_nome_programa():
    print('Sabor Express')


def exibir_opcoes():

    ## ----- Menu ------ ##
    ### ----- 1. Cadastrar: Restaurante ------ ###
    ### ----- 2. Listar: Restaurante ------ ###
    ### ----- 3. Ativar: Restaurante ------ ###
    ### ----- 4. Sair: Restaurante ------ ###

    op = ['1. Cadastrar: Restaurante', '2. Listar: Restaurante', '3. Ativar: Restaurante', '4. Sair']

    print(op[0])
    print(op[1])
    print(op[2])
    print(op[3])
    return op

    
    

def escolhe_opcao():
    exibir_opcoes()
### ---- Verifica opção escolhida ----- ###
        ### Por match -> >=3.10 ###
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                exibir_subTitulos('Ativar restaurante')
            case 4:
                exibir_subTitulos('Finalizando o app')
            case _:
                exibir_subTitulos('Opção inválida')
                limpa_tela()
                retorna_ao_menu()
    except ValueError:
        exibir_subTitulos('Opção inválida')
        limpa_tela()
        retorna_ao_menu()

       