import os

def limpa_tela():
    limpa = os.system('Clear')
    return limpa

def retorna_ao_menu():
    from app import main
    input(f'digite uma tecla para retornar ao menu principal')
    main()

def exibir_subTitulos(texto):
    limpa_tela()
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'\n{texto}\n')
    print(f'{linha}\n')
