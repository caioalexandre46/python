import os

motos = [{'nome':'Honda CB 500F', 'categoria':'Naked', 'ativo':False}, 
         {'nome':'Yamaha MT-07', 'categoria':'Naked', 'ativo':True},
         {'nome':'Kawasaki Ninja 400', 'categoria':'Esportiva', 'ativo':False}]

def exibirNomePrograma():
    print('SISTEMA DE FROTAS DE MOTOCICLETAS 1.0')

def exibirOpcoes():
    print('1. Cadastrar motocicleta')
    print('2. Listar motocicletas')
    print('3. Alternar estado de uma motocicleta')
    print('4. Sair\n')

def finalizar():
    exibirSubtitulo('Finalizar app')

def voltarMenuPrincipal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcaoInvalida():
    print('Opção inválida!\n')
    voltarMenuPrincipal()

def exibirSubtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrarMotocicleta():
    exibirSubtitulo('Cadastro de novas motocicletas')
    nomeMotocicleta = input('Digite o nome da motocicleta a ser cadastrada: ')
    categoria = input(f'Digite a categoria da motocicleta {nomeMotocicleta}: ')
    dadosMotocicleta = {'nome':nomeMotocicleta, 'categoria':categoria, 'ativo':False}
    motos.append(dadosMotocicleta)
    print(f'A motocicleta {nomeMotocicleta} foi cadastrada com sucesso!')
    voltarMenuPrincipal()

def listarMotocicleta():
    exibirSubtitulo('Listagem de motocicletas')
    print(f'{"Nome da motocicleta".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for moto in motos:
        nomeMotocicleta = moto['nome']
        categoria = moto['categoria']
        ativo = 'ativada' if moto['ativo'] else 'desativada'
        print(f'- {nomeMotocicleta.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltarMenuPrincipal()

def alterarMotocicleta():
    exibirSubtitulo('Alterar estado da motocicleta')
    nomeMotocicleta = input('Digite o nome da motocicleta que deseja alterar o status: ')
    motocicletaEncontrada = False

    for moto in motos:
        if nomeMotocicleta == moto['nome']:
            motocicletaEncontrada = True
            moto['ativo'] = not moto['ativo']
            mensagem = f'A motocicleta {nomeMotocicleta} foi ativada com sucesso' if moto['ativo'] else f'A motocicleta {nomeMotocicleta} foi desativada com sucesso'
            print(mensagem)
            
    if not motocicletaEncontrada:
        print('A motocicleta não foi encontrada')
            
    voltarMenuPrincipal()

def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: 
            cadastrarMotocicleta()
        elif opcaoEscolhida == 2: 
            listarMotocicleta()
        elif opcaoEscolhida == 3: 
            alterarMotocicleta()
        elif opcaoEscolhida == 4: 
            finalizar()
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == '__main__':
    main()
