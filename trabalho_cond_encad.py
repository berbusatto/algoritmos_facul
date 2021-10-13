# SENAC PR
# ADS - 1º PERÍODO
# BERNARDO SAAD GERBAN BUSATTO


# EXERCÍCIO 1
# Faça um algoritmo que lê uma data informada pelo usuário (ano, mês e dia) e informe qual o dia da
# semana  dessa  data  (Segunda,  Terça,  Quarta,  Quinta,  Sexta,  Sábado  ou  Domingo).

# dia = int(input('Dia: '))
# mes = int(input('Mes: '))
# ano = int(input('Ano: '))
#
# if 0 < dia < 32 and 0 < mes < 13 and 1900 < ano <= 2021:
#     passaram = ano - 1900
#     bissextos = passaram // 4
#     codmes = 0
#
# # DEVERIA SER UM SWITCH
#     if mes == 1 or mes == 10:
#         codmes = 0
#     elif mes == 2 or mes == 3 or mes == 11:
#         codmes = 3
#     elif mes == 4 or mes == 7:
#         codmes = 6
#     elif mes == 5:
#         codmes = 1
#     elif mes == 6:
#         codmes = 4
#     elif mes == 8:
#         codmes = 2
#     else:
#         codmes = 5
#
#     res = passaram + bissextos + dia + codmes
#     diasemana = res % 7
#
# # TAMBÉM DEVERIA SER UM SWITCH
#     if diasemana == 0:
#         print(f'Domingo')
#     elif diasemana == 1:
#         print('Segunda')
#     elif diasemana == 2:
#         print('Terça')
#     elif diasemana == 3:
#         print('Quarta')
#     elif diasemana == 4:
#         print('Quinta')
#     elif diasemana == 5:
#         print('Sexta')
#     elif diasemana == 6:
#         print('Sábado')
# else:
#     print('Um dos valores está inválido')

# EXERCICIO 2
# No Brasil existe o CPF (Cadastro de Pessoas Físicas) que serve para identificar cada indivíduo no
# país. O número do CPF é composto de 11 dígitos, sendo os dois últimos os dígitos de verificação.
# Faça um algoritmo que leia cada um dos 11 dígitos de um CPF, onde cada dígito é armazenado em
# uma variável diferente. Depois, seguindo a fórmula abaixo que valida o CPF, informar se o CPF é
# Válido ou Inválido.
#

cpf = input('Digite, um CPF para ver se ele é valido:  ')
cpflista = []

# print(cpf)
for x in cpf:
    cpflista.append(int(x))
# print(cpflista)

soma = (cpflista[0] * 10) + (cpflista[1] * 9) + (cpflista[2] * 8) + (cpflista[3] * 7) + (cpflista[4] * 6) + \
       (cpflista[5] * 5) + (cpflista[6] * 4) + (cpflista[7] * 3) + (cpflista[8] * 2)

# print(soma)
valor = (soma // 11) * 11
# print(valor)
resultado = soma - valor
# print(resultado)

# DEFININDO O PRIMEIRO DÍGITO VERIFICADOR
if resultado == 0 or resultado == 1:
    primdigito = 0
else:
    primdigito = 11 - resultado
# print(f'O primeiro dígito deve ser {primdigito}')

somab: int = (cpflista[0] * 11) + (cpflista[1] * 10) + (cpflista[2] * 9) + (cpflista[3] * 8) + (cpflista[4] * 7) + \
             (cpflista[5] * 6) + (cpflista[6] * 5) + (cpflista[7] * 4) + (cpflista[8] * 3) + + (primdigito * 2)

# print(somab)
valorb = (somab // 11) * 11
# print(valorb)
resultadob = somab - valorb
# print(resultadob)

# DEFININDO O SEGUNDO DÍGITO VERIFICADOR
if resultadob == 0 or resultadob == 1:
    segdigito = 0
else:
    segdigito = 11 - resultadob
# print(f'O segundo digito deve ser {segdigito}')

# VALIDANDO O CPF
if primdigito == cpflista[9] and segdigito == cpflista[10]:
    print('CPF válido.')
else:
    print('CPF inválido')
