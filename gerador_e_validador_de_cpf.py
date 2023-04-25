import re, random

def verificador_cpf():
    while True:

        cpf = input("Digite o seu CPF")
        #Faz com que apenas números sejam alocados na variável
        cpf = re.sub(r'[^0-9]', '', cpf)
        
        # Verificador para saber se o CPF enviado pelo usuário tem 11 números. Se conter 11, ele
        # continua o código, caso contrário ele reinicia o loop
        if len(cpf) != 11:
            print("Digite um cpf com os 11 dígitos!")
            continue

        # Verificador para saber se o CPF enviado pelo usuário tem o mesmo número repetido várias vezes.
        verif_caracteres_rep = cpf[0] * len(cpf)

        if verif_caracteres_rep == cpf:
            print("Não é permitido enviar um CPF com todos os dígitos iguais.")
        else:
            return cpf

def buscar_menu():
    while True:
        print("----------------------")
        print("| Digite uma opção   |")
        print("| [1] Validar CPF    |")
        print("| [2] Gerador CPF    |")
        print("----------------------")

        opcao = input("Digite uma opção")
        
        if opcao == '1' or opcao == '2':
            return opcao
        else:
            print("Digite uma opção válida.")
            

def encontra_1_digito(cpf_enviado):
    cpf_enviado_reduzido = cpf_enviado[:9]

    numero_a_subtrair = 10
    soma_total = 0
    for num in cpf_enviado_reduzido:
        
        mult_contagem = int(num) * numero_a_subtrair

        soma_total += mult_contagem

        numero_a_subtrair -= 1
        
    resto_da_mult_por_10 = (soma_total * 10) % 11

    if resto_da_mult_por_10 > 9:
        primeiro_digito = 0

    else:
        primeiro_digito = resto_da_mult_por_10

    return primeiro_digito

def encontra_segundo_digito(cpf_enviado_e_1_dig):


    sub_2 = 11
    soma_total_2 = 0
    for numero in cpf_enviado_e_1_dig:
        mult_contagem_2 = int(numero) * sub_2
        soma_total_2 += mult_contagem_2
        sub_2 -= 1

    resto_da_mult_por_11 = (soma_total_2 * 10) % 11

    if resto_da_mult_por_11 > 9:
        segundo_digito = 0
    else:
        segundo_digito = resto_da_mult_por_11

    return segundo_digito

def mostra_cpf(cpf_concluido, dig_1, dig_2, cpf_enviado):

    cpf_montado = (f'{cpf_concluido[0:3]}.{cpf_concluido[3:6]}.{cpf_concluido[6:9]}-{str(dig_1) + str(dig_2)}')

    if opcao_escolhida == '1':
        if cpf_enviado == cpf_concluido:
            return f'O CPF: {cpf_montado} é válido. '
        else:
            return f'O CPF: {cpf_montado} é inválido. '
    
    if opcao_escolhida == '2':
        return f'CPF GERADO: {cpf_montado} '

#Programa

while True:

    opcao_escolhida = buscar_menu()

    if opcao_escolhida == '1':

        cpf_input_usuario = verificador_cpf()
        digito_1 = encontra_1_digito(cpf_input_usuario)    
        digito_2 = encontra_segundo_digito(cpf_input_usuario[:9] + str(digito_1))
        cpf_completo = cpf_input_usuario[:9] + str(digito_1) + str(digito_2)
        cpf_validacao = print(mostra_cpf(cpf_enviado = cpf_input_usuario, dig_1 = digito_1, dig_2 = digito_2, cpf_concluido = cpf_completo))

    if opcao_escolhida == '2':
        cpf_input_usuario = ''

        for i in range(0,9):
            numero_gerado = str(random.randint(0, 9))
            cpf_input_usuario += str(numero_gerado)
        
        digito_1 = encontra_1_digito(cpf_input_usuario)    
        digito_2 = encontra_segundo_digito(cpf_input_usuario[:9] + str(digito_1))
        cpf_completo = cpf_input_usuario[:9] + str(digito_1) + str(digito_2)
        cpf_validacao = print(mostra_cpf(cpf_enviado = cpf_input_usuario, dig_1 = digito_1, dig_2 = digito_2, cpf_concluido = cpf_completo))

    while True:
        opcao_nao = ['não', 'n', 'nao']
        opcao_sim = ['sim', 's', 'ss']
        continuar = input("Deseja continuar? [Não/Sim]").lower()


        if continuar in opcao_nao:
            break
        elif continuar in opcao_sim:
            break
        else:
            print("Digite uma opção válida")

    if continuar in opcao_nao:
        break