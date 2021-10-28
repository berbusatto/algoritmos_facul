# EXERCÍCIO 1
# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor  e  dos  impostos.  Supondo  que  a  percentagem  do  distribuidor  seja  de  28%  (sobre  o
# custo  de  fábrica)  e  os  impostos  de  45%  (aplicados  ao  custo  de  fábrica),  escrever  um  algoritmo
# que  leia  o  custo  de  fábrica  de  um  carro  comprado  pelo  distribuidor  e  escreva  o  custo  final  ao
# consumidor.  O  programa  deve  fazer  esse  cálculo  para  um  conjunto  de  carros,  sendo  encerrado
# quando o custo informado for 0 (zero). Ao final, deve-se mostrar o número de carros avaliados, a
# soma total do custo final e a média do valor dos automóveis.

# custo_fabrica = float(input('Digite o custo de fábrica do carro: '))
# custo_unitario = 0
# custo_final = 0
# cont_carros = 0
# while custo_fabrica != 0:
#     distribuidor = custo_fabrica * 0.28
#     imposto = custo_fabrica * 0.45
#     custo_unitario = custo_fabrica + distribuidor + imposto
#     print(f'Este veículo custará R${custo_unitario}')
#     custo_final += custo_unitario
#     cont_carros += 1
#     custo_fabrica = float(input('Digite o custo de fábrica do carro: '))
#
# custo_medio = custo_final / cont_carros
# print(f'Foram avaliados {cont_carros} carros.')
# print(f'O valor total dos veículos é R${custo_final:.2f}.')
# print(f'O custo médio foi R${custo_medio:.2f}.')

##########################################
# EXERCÍCIO 2
# Elabore um algoritmo que dada a idade de um grupo de nadadores, classifique-os em uma das
# seguintes categorias:
#
# Categoria Idade
# infantil A 5 - 7 anos
# infantil B 8-10 anos
# juvenil A 11-13 anos
# juvenil B 14-17 anos
# adulto maiores de 18 anos
# O programa deve encerrar quando a idade do nadador for igual a zero. Antes de encerrar, deve-se
# mostrar a quantidade de nadadores classificados por categoria e total.

# ia_cont = 0
# ib_cont = 0
# ja_cont = 0
# jb_cont = 0
# ad_cont = 0
#
# idade = int(input('Digite a idade do nadador: '))
# while idade != 0:
#     if idade >= 5:
#         if idade <= 7:
#             ia_cont += 1
#         elif idade <= 10:
#             ib_cont += 1
#         elif idade <= 13:
#             ja_cont += 1
#         elif idade <= 17:
#             jb_cont += 1
#         else:
#             ad_cont += 1
#     idade = int(input('Digite a idade do nadador: '))
#
# total = ia_cont + ib_cont + ja_cont + jb_cont + ad_cont
# print('Quantidade de classificados por categoria')
# print(f'Infantil A: {ia_cont}')
# print(f'Infantil B: {ib_cont}')
# print(f'Juvenil A: {ja_cont}')
# print(f'Juvenil B: {jb_cont}')
# print(f'Adulto: {ad_cont}')
# print(f'O total atletas classificados foi: {total}')

##########################################
# EXERCÍCIO 3
# Elabore um algoritmo que  receba o  nome e a idade de um  conjunto de jogadores de  futebol
# de uma determinada  competição. Ao final do algoritmo informe a quantidade de jogadores lidos
# juntamente  com  a  média  de  idade.  A  idade  do  jogador  mais  velho  e  do  jogador  mais  novo
# também  deve  ser  mostrada  no  final.  O  algoritmo  deve  encerrar  a  leitura  de  jogadores  quando  a
# idade informada ser igual a 0 (zero).

# nomes = []
# idades = []
# idade = int(input('Digite a idade do jogador: '))
# while idade != 0:
#     nomes.append(input('Digite o nome do jogador: '))
#     idades.append(idade)
#     idade = int(input('Digite a idade do jogador: '))
#
# print(nomes)
# print(idades)
# qtd = len(nomes)
# print(f'A quantidade de jogadores cadastrados foi de {qtd}.')
# print(f'A média de idade dos jogadores é de {int(sum(idades) / len(nomes))}')  # len(nomes) pq idades[] recebe o ultimo 0
# print(f'O jogador com maior idade tem {max(idades)} anos.')
# print(f'O jogador com menor idade tem {min(idades)} anos.')
#
##########################################
# EXERCÍCIO 4
# O cardápio de uma lanchonete é o seguinte:
#
# Especificação Código  Preço
# Cachorro quente 100 R$ 1,20
# Bauru simples 101 R$ 1,30
# Bauru com ovo 102 R$ 1,50
# Hambúrguer 103 R$ 1,30
# Cheeseburguer 104 R$ 1,30
# Refrigerante 105 R$ 1,00
#
# Escrever  um  algoritmo  que  leia  o  código  do  item  pedido,  a  quantidade  e  calcule  o  valor  a  ser
# pago  por  aquele  lanche.  Considere  que  a  cada  execução  somente  será  calculado  um  item.  O
# programa irá ler os pedidos enquanto o código do produto não for 999. Quando o cliente informar
# 999, o algoritmo deve informar a quantidade de pedidos realizada, a quantidade de itens vendido
# e o valor total arrecadado.

valor_total = 0
qtd_pedidos = 0
qtd_cont = 0
cod = input('Código: ')

while cod != '999':
    qtd = int(input('Quantidade: '))
    if cod == '100':
        valor_total += (qtd * 1.20)
    elif cod == '101':
        valor_total += (qtd * 1.30)
    elif cod == '102':
        valor_total += (qtd * 1.50)
    elif cod == '103':
        valor_total += (qtd * 1.30)
    elif cod == '104':
        valor_total += (qtd * 1.30)
    elif cod == '105':
        valor_total += (qtd * 1.00)
    print(f'{valor_total:.2f}')
    qtd_cont += qtd
    qtd_pedidos += 1
    cod = input('Código: ')

print(f'Foram realizados {qtd_pedidos} pedidos.')
print(f'{qtd_cont} itens foram vendidos.')
print(f'Totalizando R${valor_total:.2f}.')

##########################################
# EXERCÍCIO 5
#Faça um algoritmo que mostre na tela as tabuadas de 2 a 10. Utilizar o comando ENQUANTO.
#Dica (Comando ENQUANTO encadeado)












