# EXERCÍCIO 1
# Escreva um algoritmo para calcular e escrever o valor da soma S:
# S = (1/1) + (2/4) + (3/9) + (4/16) + (5/25) + (6/36) + .... (10/100)

# soma = 0
# for x in range(11):
#     if x > 0:
#         soma = soma + (x / (x * x))
#
# print(soma)

# EXERCÍCIO 2
# Escreva um algoritmo que leia o código e o salário de 100 funcionários de uma empresa.
# Ao final, o algoritmo deve determinar o total da folha de pagamento da empresa e sua
# média salarial.
#
# media = 0
# soma = 0
# for x in range(3):
#     salario = float(input('Salário '))
#     codigo = int(input('Código ')) # NÃO SEI POR QUE ESTÁ AQUI SENDO QUE NÃO FOI UTILIZADO
#     soma = salario + soma
#     media = soma / (x + 1)
# print(f'O total da folha de pagamento é de {soma:.2f}')
# print(f'A média salarial é de {media} reais')

# EXERCÍCIO 3
# Criar um algoritmo para ler o nome e a idade de um grupo de pessoas, sendo o número
# desse grupo determinado pelo cliente.
# Ao final, o programa deverá imprimir o nome e a idade da pessoa mais idosa e o nome e a
# idade da pessoa mais jovem.

# nome = []
# idade = []
# selec = int(input('Quantas pessoas? '))
# for x in range(selec):
#     nome.insert(x, input('Nome: '))
#     idade.insert(x, int(input('Idade: ')))
# # print(nome, idade)
# indice_maior = idade.index(max(idade))
# indice_menor = idade.index(min(idade))
# print(f'A pessoa com maior idade é: {nome[indice_maior]}.')
# print(f'A pessoa com menor idade é: {nome[indice_menor]}.')

# RESOLUÇÃO DO KIKO
# pessoas = []
# n_pessoas = int(input('Quantas pessoas? '))
# for x in range(n_pessoas):
#     nome = input('Nome: ')
#     idade = int(input('Idade: '))
#     pessoa = (nome, idade)
#     pessoas.append(pessoa)
#
# pessoas = sorted(pessoas, key=lambda p: p[1]) # orderna a lista por idade, p[1] é a idade na tupla (nome, idade)
# nome_mais_velha = pessoas[-1][0] # o indice [-1] retorna o ultimo elemento da lista, o [0] extrai o nome da tupla (nome, idade)
# nome_mais_nova = pessoas[0][0]
#
# print(f'A pessoa com maior idade é: {nome_mais_velha}.')
# print(f'A pessoa com menor idade é: {nome_mais_nova}.')


# EXERCÍCIO 4
# Crie um programa que efetue o cálculo da fatorial de um número. Por exemplo, o
# fatorial de 5 é 120.
# Desta forma 5 ! = 5 * 4 * 3 * 2 * 1 ou 1 * 2 * 3 * 4 * 5

# num = int(input('Digite um número para descobrir o seu fatorial: '))
# res = 1
# for i in range(num + 1):
#     if i > 0:
#         res = res * i
# print(res)

# EXERCÍCIO 5
# Uma máquina comprada por R$ 28.000,00 se deprecia com uma taxa de R$ 4.000,00
# por ano em sete anos. Escreva um algoritmo que calcula e mostre a tabela de depreciação
# para esses sete anos. A tabela deve ter a forma abaixo.


# valor_maquina = 28000.00
# taxa = 4000.00
# dep_acum = 0.00
# for i in range(8):
#     if i == 0:
#         print(f'Ano', 'Depreciação', 'Valor no final do Ano', 'Depreciação Acumulada')
#     else:
#         valor_maquina -= taxa
#         dep_acum += taxa
#         linha = [i, taxa, valor_maquina, dep_acum]
#         print(linha)

# OU

# from prettytable import PrettyTable
#
# lista = PrettyTable(['Ano', 'Depreciação', 'Valor final do ano', 'Depreciação acumulada'])
# lista.align["Ano"] = "c"  # c para centralizar, r pra direita, l pra esquerda
# lista.align['Depreciação'] = "c"
# lista.align['Valor final do ano'] = 'c'
# lista.align['Depreciação acumulada'] = 'c'
# lista.padding_width = 1
# lista.float_format = '.2'
#
# valor_maquina = 28000.00
# taxa = 4000.00
# dep_acum = 0.00
# for i in range(8):
#     if i > 0:
#         valor_maquina -= taxa
#         dep_acum += taxa
#         lista.add_row([i, taxa, valor_maquina, dep_acum])
# print(lista)

# EXERCÍCIO 6
# Para  realizar  a  totalização  dos  votos  de  uma  eleição  para  um  cargo  majoritário  com  3
# candidatos  (Antonio,  Pedro  e  José),  leia  os  votos  da  10  seções  que  compõem  o  colégio
# eleitoras. Para cada seção, são informados: o número de votos de cada candidato, o número
# de votos brancos e o número de votos nulos. A partir dessas informações determine:
# a. o número de votantes;
# b. o total de voto de cada candidato;
# c. o total de votos brancos e nulos;
# d. o total de votos válidos;
# e. O candidato com maior votação;
# f. Se a eleição for válida. Para isso, o total de votos brancos mais votos nulos deve ser
# menor que o total de votos válidos

# antonio = 0
# pedro = 0
# jose = 0
# brancos = 0
# nulos = 0

# for i in range(2):
#     antonio += int(input('Votos Antonio: '))
#     pedro += int(input('Votos Pedro: '))
#     jose += int(input('Votos Jose: '))
#     brancos += int(input('Brancos: '))
#     nulos += int(input('Nulos: '))
#
# total = antonio + pedro + jose + brancos + nulos
# invalidos = brancos + nulos
# validos = antonio + pedro + jose
# valida = (antonio + pedro + jose) > (brancos + nulos)
#
# print(f'O total de votos foi de: {total}')
# print(f'O total de brancos e nulos foi de: {invalidos}')
# print(f'O total de votos válidos foi de: {validos}')
#
# if valida:
#     if pedro > antonio and pedro > jose:
#         print(f'Pedro foi eleito com {pedro} votos')
#     elif antonio > pedro and antonio > jose:
#         print(f'Antonio foi eleito com {antonio} votos')
#     else:
#         print(f'Jose foi eleito com {jose} votos')
# print(f'Eleição válida? {valida}')

# EXERCÍCIO 7
# Faça um algoritmo que leia o nome, a idade e o sexo (‘M’ para masculino e ‘F’ para
# feminino) de um grupo de 200 estudantes e determine?
# a) quantos são do sexo feminino e maior de 21 anos;
# b) quantos são do sexo masculino e maio de 18 anos
# c) qual a média de idade de pessoas do sexo masculino;
# d) qual a média de idade de pessoas do sexo feminino;

# PRIMEIRAS TENTATIVAS, LEVEI O DIA INTEIRO PARA TENTAR RESOLVER COM LISTAS E
# TUPLAS MAS NÃO CONSEGUI.
# DEPOIS DE UMA BOA NOITE DE SONO RESOLVI EM MEIA HORA HEHEHEH

# mulheres = []
# homens = []
# qtd_pessoas = 5
# cont_mul21 = 0
# cont_hom18 = 0
# idade_hom = 0
# idade_mul = 0
# cont_m = 0
# cont_h = 0
#
# for x in range(qtd_pessoas):
#     nome = input('nome: ')
#     idade = int(input('idade: '))
#     sexo = input('sexo: ').lower()
#     pessoa = (nome, idade, sexo)
#     if sexo == 'f':
#         # mulheres.append(pessoa)
#         idade_mul = idade_mul + idade
#         cont_m = cont_m + 1
#         if idade > 21:
#             cont_mul21 = cont_mul21 + 1
#     elif sexo == 'm':
#         # homens.append(pessoa)
#         idade_hom = idade_hom + idade
#         cont_h = cont_h + 1
#         if idade > 18:
#             cont_hom18 = cont_hom18 + 1
#     else:
#         print('sexo inválido')
#
# print(cont_mul21)
# print(cont_hom18)
# if cont_m > 0:
#     media_mul = idade_mul / cont_m
#     print(media_mul)
# if cont_h > 0:
#     media_hom = idade_hom / cont_h
#     print(media_hom)

# SEGUNDA TENTATIVA

# pessoas = []
# sum_h = []
# sum_m = []
# idade_m = []
# idade_h = []
# for x in range(2):
#         nome = (input('nome: '))
#         idade = (int(input('idade: ')))
#         sexo = (input('sexo: ').lower())
#         pessoa = (nome, idade, sexo)
#         pessoas.append(pessoa)
#
#         if sexo == 'f':
#             # mulheres.append(pessoa)
#             idade_m.append(idade_m + idade)
#             sum_m.append(sum_m + 1)
#
#         elif sexo == 'm':
#             # homens.append(pessoa)
#             idade_h = idade_h + idade
#             cont_h = cont_h + 1
#             if idade > 18:
#                 cont_hom18 = cont_hom18 + 1
#
#
# media_h = sum(sum_h) / len(sum_h)
# print(media)

# EXERCÍCIO 8
# Faça um algoritmo que apresente na tela as tabuadas de 2 à 8, como mostrado abaixo
#
# modo n00b
# num = 2
# res = 0
# for x in range(11):
#     res = num * x
#     print(f'{x} X {num} = {res}')
#     if x >= 10:
#         num = num + 1
#         for y in range(11):
#             res = num * y
#             print(f'{y} X {num} = {res}')
#             if y >= 10:
#                 num = num + 1
#                 for z in range(11):
#                     res = num * z
#                     print(f'{z} X {num} = {res}')
#                     if z >= 10:
#                         num = num + 1
#                         for a in range(11):
#                             res = num * a
#                             print(f'{a} X {num} = {res}')
#                             if a >= 10:
#                                 num = num + 1
#                                 for b in range(11):
#                                     res = num * b
#                                     print(f'{b} X {num} = {res}')
#                                     if b >= 10:
#                                         num = num + 1
#                                         for c in range(11):
#                                             res = num * c
#                                             print(f'{c} X {num} = {res}')
#                                             if c >= 10:
#                                                 num = num + 1
#                                                 for d in range(11):
#                                                     res = num * d
#                                                     print(f'{d} X {num} = {res}')

# MODO PRO
# for x in range(2, 9):
#     for y in range(11):
#         res = x * y
#         print(f'{x} X {y} = {res}')

# EXERCÍCIO 9

# Código Especificação Preço
# 100 Cachorro quente 1.20
# 101 Bauru Simples 1.30
# 102 Bauru com ovo 1.50
# 103 Hambúrguer 1.70
# 201 Refrigerante 1.00
# 202 Suco 1.50
# 203 Água Mineral 0.70
# Escreva um algoritmo que leia o código de um sanduíche e de uma bebida de 100 pedidos
# e imprima o valor arrecadado com lanches, bebidas e o total arrecadado. Assuma entradas
# corretas.

#
# lanches = []
# bebidas = []
# for x in range(100):
#     cod_lanche = int(input('Digite o código do lanche: '))
#     cod_bebidas = int(input('Digite o código da bebida: '))
#     if cod_lanche == 100:
#         lanches.append(1.20)
#     elif cod_lanche == 101:
#         lanches.append(1.30)
#     elif cod_lanche == 102:
#         lanches.append(1.50)
#     elif cod_lanche == 103:
#         lanches.append(1.70)
#     else:
#         print('Código inválido')
#
#     if cod_bebidas == 201:
#         bebidas.append(1.00)
#     elif cod_bebidas == 202:
#         bebidas.append(1.50)
#     elif cod_bebidas == 203:
#         bebidas.append(0.70)
#     else:
#         print('Código inválido')
#
# total_lanches = sum(lanches)
# total_bebidas = sum(bebidas)
# total = total_lanches + total_bebidas
#
# print(f'O total arrecadado com lanches foi de: {total_lanches:.2f}')
# print(f'O total arrecadado com bebidas foi de: {total_bebidas:.2f}')
# print(f'O valor total arrecadado foi de: {total:.2f}')

# EXERCÍCIO 10
# Escreva um algoritmo que leia o número de identificação e as 3 notas obtidas por uma
# turma  de  30  alunos  nas  3  avaliações.  Calcule  a  média  de  cada  aluno.  A  atribuição  dos
# conceitos  obedece  a  tabela  abaixo.  O  algoritmo  deve  escrever  o  número  do  aluno,  suas
# notas, a média,  o conceito correspondente e a mensagem ‘Aprovado’ se o conceito for A,
# B ou C e ‘Reprovado’ se o conceito for D ou E.
# Posteriormente, informar quantos alunos alcançaram o Conceito A, B, C, D e o E
# Média de aproveitamento Conceito
# >= 90 A
# >= 75  e  < 90 B
# >= 60  e  < 75 C
# >= 40  e  < 60 D
# < 40 E

alunos = []
nota1 = []
nota2 = []
nota3 = []
media = []
conceito = []
resultado = []

for x in range(30):
    alunos.append(input('Digite o código do aluno: '))
    nota1.append(int(input('Digite a primeira nota: ')))
    nota2.append(int(input('Digite a segunda nota: ')))
    nota3.append(int(input('Digite a terceira nota: ')))
    media.append(float(nota1[x] + nota2[x] + nota3[x]) / 3)

    if media[x] >= 90:
        conceito.append('A')
    elif media[x] >= 75:
        conceito.append('B')
    elif media[x] >= 60:
        conceito.append('C')
    elif media[x] >= 40:
        conceito.append('D')
    else:
        conceito.append('E')
    if conceito[x] == 'A' or conceito[x] == 'B' or conceito[x] == 'C':
        resultado.append('Aprovado!')
    else:
        resultado.append('Reprovado!')

for x in range(30):
    print(f'O aluno de código {alunos[x]}, tem como primeira nota {nota1[x]}, como segunda nota {nota2[x]}, '
          f'e como terceira nota {nota3[x]}. Sua média é {media[x]}, o conceito alcançado foi {conceito[x]}, '
          f'e o resultado final é {resultado[x]}')
