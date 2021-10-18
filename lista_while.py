# EXERCÍCIO 1
# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor  e  dos  impostos.  Supondo  que  a  percentagem  do  distribuidor  seja  de  28%  (sobre  o
# custo  de  fábrica)  e  os  impostos  de  45%  (aplicados  ao  custo  de  fábrica),  escrever  um  algoritmo
# que  leia  o  custo  de  fábrica  de  um  carro  comprado  pelo  distribuidor  e  escreva  o  custo  final  ao
# consumidor.  O  programa  deve  fazer  esse  cálculo  para  um  conjunto  de  carros,  sendo  encerrado
# quando o custo informado for 0 (zero). Ao final, deve-se mostrar o número de carros avaliados, a
# soma total do custo final e a média do valor dos automóveis.

custo_fabrica = float(input('Digite o custo de fábrica do carro: '))
custo_unitario = 0
custo_final = 0
cont_carros = 0
while custo_fabrica != 0:
    distribuidor = custo_fabrica * 0.28
    imposto = custo_fabrica * 0.45
    custo_unitario = custo_fabrica + distribuidor + imposto
    print(f'Este veículo custará R${custo_unitario}')
    custo_final += custo_unitario
    cont_carros += 1
    custo_fabrica = float(input('Digite o custo de fábrica do carro: '))

custo_medio = custo_final / cont_carros
print(f'Foram avaliados {cont_carros} carros.')
print(f'O valor total dos veículos é R${custo_final:.2f}.')
print(f'O custo médio foi R${custo_medio:.2f}.')




