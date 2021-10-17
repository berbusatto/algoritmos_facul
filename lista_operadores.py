####################################
# EXERCÍCIO 1
# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem
# do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do
# distribuidor seja de 28% e os impostos de 45%, escrever um programa em Python para ler o
# custo de fábrica de um carro, calcular e escrever o custo final ao consumidor

# custo_fabrica = float(input('Qual é o custo de fábrica do veículo? '))
# distrib = 28/100
# imposto = 45/100
# custo_total = custo_fabrica + (custo_fabrica * distrib) + (custo_fabrica * imposto)
# print(f'R${custo_total:.2f}')

####################################
# EXERCÍCIO 2
# Escreva um programa em Python para ler uma temperatura em graus Fahrenheit, calcular e
# escrever o valor correspondente em graus Celsius:
# C / 5 = (F-32) / 9 (fração)
# C * 9 = (F-32) * 5
# C = (F-32) * 5 / 9

# fah = int(input('Digite uma temperatura em Fahrenheit: '))
# cel = (fah - 32) * 5 / 9
# print(cel)

####################################
# EXERCÍCIO 3
# As  maçãs  custam  R$  1,30  cada  se  forem  compradas  menos  de  uma  dúzia,  e  R$  1,00  se
# forem  compradas  pelo  menos  12.  Escreva  um  programa  em  Python  que  leia  o  número  de
# maçãs compradas, calcule e escreva o custo total da compra.

# macas_comp = int(input('Quantidade de maçãs compradas: '))
# sem_desc = 1.30
# com_desc = 1.00
# if macas_comp < 12:
#     valor_comp = macas_comp * sem_desc
# else:
#     valor_comp = macas_comp * com_desc
# print(f'R${valor_comp:.2f}')

####################################
# EXERCÍCIO 4
# O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde
# para dar uma indicação sobre a condição de peso de uma pessoa adulta.
# A fórmula é IMC = peso / ( altura )2
# Elabore  um  programa  em  Python  que  leia  o  peso  e  a  altura  de  um  adulto  e  mostre  sua
# condição de acordo  com a tabela abaixo.
# Abaixo de 18,5  - Abaixo do peso
# Entre 18,5 e 25  - Peso normal
# Entre 25 e 30     - Acima do peso
# Acima de 30      - obeso
#
# peso = float(input('Digite o peso em quilos: '))
# altura = float(input('Digite a altura em metros: '))
# imc = peso / (altura ** 2)
# res = ""
# # print(imc)
# if imc < 18.5:
#     res = 'Abaixo do peso'
# elif imc < 25:
#     res = 'Peso normal'
# elif imc < 30:
#     res = 'Acima do peso'
# else:
#     res = 'Obeso'
# print(res)








#####################################

