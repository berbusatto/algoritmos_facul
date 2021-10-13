# EXERCICIO 1
# Considere as seguintes classificações de estabelecimentos tendo em conta a sua área :
#  0 a 49 m2      – Mercearia
#  50 a  399 m2   - Livre Serviço
#  400 a 999 m2   - Super Pequeno
#  1000 a 2499 m2 - Super Grande
#  >=2500 m2      - Hipermercado
# Escreva  um  programa  que,  dada  a  área  de  um  estabelecimento,  o  classifique  segundo  o  critério
# referido

area = float(input('Digite a área: '))

if area <= 49:
    print('mercearia')
elif area <= 399:
    print('Livre serviço')
elif area <= 999:
    print('Super pequeno')
elif area <= 2499:
    print('Super grande')
else:
    print('hipermercado')

# EXERCÍCIO 2
# Escreva um algoritmo que leia três números e os imprima em ordem crescente.

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
num_3 = int(input('Digite mais um número: '))
lista = [num_1, num_2, num_3]
lista_ordenada = sorted(lista)
print(lista_ordenada)

# EXERCÍCIO 3
# Escrever  um  algoritmo  para  ler  três  números.  Se  o  primeiro  for  positivo,  imprimir  sua  raiz
# quadrada, caso contrário, imprimir o seu quadrado;
# se o segundo número for maior que 10 e menor que 100, imprimir a mensagem: “Número está entre 10 e 100 –
# intervalo permitido”;
# se o terceiro número  for  menor  que  o  segundo,  calcular  e  imprimir  a  diferença  entre  eles,
# caso  contrário imprimir o terceiro número adicionado de 1

import math

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
num_3 = int(input('Digite mais um número: '))

if num_1 >= 0:
    print(math.sqrt(num_1))
else:
    print(num_1 * num_1)
if 10 <= num_2 <= 100:
    print('número está entre 10 e 100 - intervalo permitido')
if num_3 < num_2:
    res = num_3 - num_2
    print(f'Como o {num_3} é menor do que {num_2} a sua subtração resulta em {res}')
else:
    print(num_3 + 1)

# EXERCÍCIO 4
#  Elabore  um  algoritmo  que,  dada  a  idade  de  um  nadador,  classifique-o  em  uma  das  seguintes
    # categorias: Infantil A: 5 a 7 anos;
    #  Infantil B: 8 a 10 anos;
    #  Juvenil A: 11 a 13 anos;
    #  Juvenil B: 14 a 17 anos;
    #  Sênior: maiores de 18 anos;

idade = int(input('Qual é a idade do(a) nadador(a)? '))

if idade >= 5:
   if idade in [5, 6, 7]:
       print('Infantil A')
   elif idade in [8, 9, 10]:
       print('Infantil B')
   elif idade in [11, 12, 13]:
       print('Juvenil A')
   elif idade in [14, 15, 16, 17]:
       print('Juvenil B')
   elif idade > 18:
       print('Sênior')
else:
   print('Não tem idade para os torneios')

# EXERCÍCIO 5
# Faça um algoritmo que leia duas notas obtidas por um aluno na disciplina de Cálculo, o número
# de aulas ministradas e o número de aulas assistidas por este aluno nesta disciplina. Calcule e mostre
# a média final deste aluno e diga se ele foi aprovado ou reprovado. Considere que para um aluno ser
# aprovado ele deve obter média final igual ou maior a 6 e ter no mínimo 75% de freqüência.

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

qtd_aulas = int(input('Quantas aulas foram ministradas? '))
aulas_assistidas = int(input('Quantas aulas o aluno assistiu? '))
media = (nota_1 + nota_2) / 2

if aulas_assistidas >= (qtd_aulas * 0.75) and media >= 7:
    print(f'O aluno tem média {media} e foi aprovado por frequência')
else:
    print(f'O aluno está reprovado')

#  EXERCÍCIO 6
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
# rendimento  diário  do  seu  trabalho.  Toda  vez  que  ele  traz  um  peso  de  peixes  maior  que  o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
# de R$ 4,00 por quilo excedente.
# João  precisa  que  faça  um  algoritmo  que  verifique  se  há  excesso.  Se  houver,  definir  a  multa  a  ser
# paga.

peso_peixes = float(input('Qual é a soma total do peso dos peixes em kg? '))
excesso = peso_peixes - 50

if peso_peixes > 50:
    multa = excesso * 4.00
    print(f'João terá que pagar {multa:.2f} reais como multa')
else:
    print('João não precisa pagar multa pois não excedeu o limite')

