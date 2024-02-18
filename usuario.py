nome = input('Digite seu nome completo: ').strip()
while True:
    try:
        nascimento = int(input('Digite o ano de nascimento (entre 1922 e 2021): '))
        if nascimento < 1922 or nascimento > 2021:
            raise ValueError('Ano não permitido')
        idade = 2022 - nascimento
        print(f'Olá, {nome}! Você completou {idade} anos no ano 2022.')
        break
    except ValueError:
        print('Erro: inválido. Por favor, digite novamente o seu ano de nascimento.')

