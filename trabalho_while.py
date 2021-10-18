#############################
# EXERCÍCIO 1
# Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano, e
# um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever um
# algoritmo em PORTUGOL que seja capaz de calcular  e  imprimir o tempo necessário  para
# que a população do país A ultrapasse a população do país B.

a = 5000000
b = 7000000
cont_ano = 0
while a <= b:
    a += (a * 0.03)
    b += (b * 0.02)
    cont_ano += 1
    # print(f'{cont_ano}, {a:.1f}, {b:.1f},')
    # print('-------')
print(cont_ano)

#############################
# EXERCÍCIO 2
# O cardápio de uma lanchonete é o seguinte:
#
# Especificação   |Cód| Preço
# Cachorro quente |100| R$ 1,20
# Bauru simples   |101| R$ 1,30
# Bauru com ovo   |102| R$ 1,50
# Hambúrguer      |103| R$ 1,30
# Cheeseburguer   |104| R$ 1,30
# Refrigerante    |105| R$ 1,00
#
# Escrever um  algoritmo que leia o  código do item  pedido,  a quantidade  e  calcule  o valor a
# ser  pago  por  aquele  lanche.  Considere  que  a  cada  execução  somente  será  calculado  um
# item. O programa irá ler os pedidos enquanto o código do produto não for 999.  Quando o
# cliente  informar  999,  o  algoritmo  deve  informar  a  quantidade  de  pedidos  realizada,  a
# quantidade de itens vendido e o valor total arrecadado.

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
    qtd_cont += qtd
    qtd_pedidos += 1
    cod = input('Código: ')

print(f'Foram realizados {qtd_pedidos} pedidos.')
print(f'{qtd_cont} itens foram vendidos.')
print(f'Totalizando R${valor_total:.2f}.')






