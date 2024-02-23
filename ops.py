from utils import finalizar_app
import os 

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

def opcao_invalida():
    from app import main
    print('Opção inválida')
    input('Selecione uma tecla para voltar: ')
    os.system('clear')
    main()
    

def escolhe_opcao():
    op = exibir_opcoes()
### ---- Verifica opção escolhida ----- ###
        ### Por match -> >=3.10 ###
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                print('Adicionar restaurante')
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


       