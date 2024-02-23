from utils import limpa_tela, retorna_ao_menu, exibir_subTitulos



restaurantes = [{'nome':'Pizza', 'categoria':'Pizza', 'status':False}]

def cadastrar_restaurante():
    '''Essa função cadastra novo restaurante'''

    exibir_subTitulos('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante: {nome_restaurante} -> ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'status':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante cadastrado com sucesso: {nome_restaurante}')
    retorna_ao_menu()

def listar_restaurantes():
    '''Essa função lista restaurantes'''
    
    exibir_subTitulos('Lisar restaurantes')

    print(f'{'Nome Restaurante'.ljust(22)} | {'Categoria do Restaurante'.ljust(22)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativado' if restaurante['status'] else 'Inativo' # Ternário
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}')
    
    retorna_ao_menu()

def alternar_estado_restaurante():
    '''Essa função ativa/inativa restaurantes'''
    ''' - Inputs: Nome Restaurante'''
    ''' - Outputs: Status alterado - Inativo para Ativo ou Ativo para Inativo'''

    exibir_subTitulos('Alterando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = (f'O restaurante {nome_restaurante} foi ativado com sucesso' 
                        if restaurante['status'] 
                        else f'O restaurante {nome_restaurante} foi desativado com sucesso')
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    retorna_ao_menu()