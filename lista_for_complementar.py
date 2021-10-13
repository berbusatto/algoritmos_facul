# EXERCÍCIO 1
# Escreva  um  algoritmo  que  determine  todos  os  divisores  de  um  número  N  informado
# pelo usuário.
#
# num = int(input('Digite um numero: '))
# for x in range(num + 1):
#     if x != 0:
#         if (num % x) == 0:
#             print(x)

# EXERCÍCIO 2
# Escreva  um  algoritmo  que  leia  200  números  inteiros  e  imprima  quantos  são  pares  e
# quantos são ímpares.

# par = 0
# impar = 0
# for x in range(200):
#     num = int(input('Digite um número inteiro: '))
#     if num % 2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f'Dos números digitados, {par} são pares e {impar} são ímpares.')

# EXERCÍCIO 3
# Escreva um algoritmo que leia um conjunto de 50 fichas, cada uma contendo a altura e o
# sexo de uma pessoa (1 = masculino e 2 = feminino), e calcule e imprima:
#  A maior e a menor altura da turma;
#  A média de altura da mulheres;
#  A média de altura da turma.

# maioraltura = 0
# menoraltura = 300
# soma = 0
# somamulheres = 0
# contmulheres = 0
# cont = 0
#
# for x in range(50):
#     altura = int(input('Altura em centímentros: '))
#     sexo = input('Digite 1 para masculino e 2 para feminino: ')
#     soma += altura
#     cont += 1
#     if altura > maioraltura:
#         maioraltura = altura
#     elif altura < menoraltura:
#         menoraltura = altura
#     if sexo == '2':
#         somamulheres += altura
#         contmulheres += 1
# print(f'A maior altura da turma é {maioraltura}')
# print(f'A menor altura da turma é {menoraltura}')
# print(f'A média de altura das mulheres é {somamulheres / contmulheres}')
# print(f'A média de altura da turma é {soma / cont}')


# EXERCÍCIO 4
# Em  um  prédio,  com  50  moradores,  há  três  elevadores  denominados  A,  B  e  C.  Para
# otimizar o sistema de controle dos elevadores, foi realizado um levantamento no qual cada
# usuário respondia:
#  O elevador que utilizava com mais freqüência;
#  O período que utilizava o elevador, entre:
# o‘M’ – matutino;
# o‘V’ – vespertino;
# o‘N’ – noturno;
# Construa um algoritmo que calcule e imprima:
#  qual é o elevador mais freqüentado e em que período se concentra o
# maior fluxo;
#  qual o período mais utilizado.
#
# TENTATIVA 2



# TENTATIVA 1
# contA = 0
# contB = 0
# contC = 0
# contM = 0
# contV = 0
# contN = 0
# for m in range(5):
#     elevador = input('Qual elevador você usa com mais frequência? A, B ou C ')
#     horario = input('Qual período você mais usa o elevador? M, V, N ')
#     if elevador == 'A':
#         contA += 1
#     elif elevador == 'B':
#         contB += 1
#     elif elevador == 'C':
#         contC += 1
#     elif horario == 'M':
#         contM += 1
#     elif horario == 'V':
#         contV += 1
#     elif horario == 'N':
#         contN += 1
# ecomp = contA
# if contB > contA:
#     ecomp = contB
# elif contC > ecomp:
#     ecomp = contC
# print(f'O elevador mais utilizado é {ecomp}')
# hcomp = contM
# if contV > contM:
#     hcomp = contV
# elif contN > hcomp:
#     hcomp = contN
# print(f'O horário mais utilizado é {hcomp}')
