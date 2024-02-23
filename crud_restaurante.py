from utils import limpa_tela, retorna_ao_menu, exibir_subTitulos



restaurantes = []

def cadastrar_restaurante():
    exibir_subTitulos('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante cadastrado com sucesso: {nome_restaurante}')
    retorna_ao_menu()

def listar_restaurantes():
    exibir_subTitulos('Lisar restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    
    retorna_ao_menu()
