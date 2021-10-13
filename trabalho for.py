# SENAC PORTÃO
# ADS PRIMEIRO PERÍODO

# BERNARDO SAAD GEBRAN BUSATTO

# TRABALHO COMANDO PARA

# Calcule  o  imposto  de  renda  a  ser  pago  por  cada  um  dos  10  contribuintes  informados
# pelo cliente, considerando que os dados de cada contribuinte são: número do CPF e renda mensal.
# Faça o cálculo do imposto com base na tabela abaixo:
#
# Base de Cálculo Mensal Alíquota Parcela a deduzir
# Até 1.903,98 Isento -
# De 1.903,99 até 2.826,65 7,5 % R$ 142,80
# De 2.826,66 até 3.751,05 15 % R$ 354,80
# De 3.751,06 até 4.664,68 22,5 % R$ 636,13
# Acima de 4.664,68 27,5 % R$ 869,36
#
# Além  do  imposto,  mostre  também  o  salário  liquido  a  ser  recebido  pelo  contribuinte.
# Ao final da leitura dos 10 contribuintes, informar a quantidade TOTAL de impostos pago e a
# média do imposto pago pelos contribuintes.

imposto = []
for x in range(3):
    cpf = input('Digite o CPF: ')
    renda = float(input('Renda mensal: '))
    if renda >= 4664.68:
        pago = renda * 0.275
        print(f'O imposto pago pelo CPF {cpf} foi de R${pago:.2f}')
        imposto.append(pago)
        liquido = renda - 869.36
        print(f'Seu salário líquido é de R${liquido:.2f}')
    elif renda >= 3751.06:
        pago = renda * 0.225
        imposto.append(pago)
        print(f'O imposto pago pelo CPF {cpf} foi de R${pago:.2f}')
        liquido = renda - 636.13
        print(f'Seu salário líquido é de R${liquido:.2f}')
    elif renda >= 2826.66:
        pago = renda * 0.15
        imposto.append(pago)
        print(f'O imposto pago pelo CPF {cpf} foi de R${pago:.2f}')
        liquido = renda - 354.80
        print(f'Seu salário líquido é de R${liquido:.2f}')
    elif renda >= 1903.99:
        pago = renda * 0.075
        imposto.append(pago)
        print(f'O imposto pago pelo CPF {cpf} foi de R${pago:.2f}')
        liquido = renda - 142.80
        print(f'Seu salário líquido é de R${liquido:.2f}')
    else:
        pago = 0
        imposto.append(0)
        print(f'O CPF {cpf} é isento de pagar imposto')
        liquido = renda - 0
        print(f'Seu salário líquido é de R${liquido:.2f}')

print('---------------------------------')
totalimpostos = sum(imposto)
mediaimpostos = sum(imposto) / len(imposto)
print(f'O total de impostos pagos foi de R${totalimpostos:.2f}')
print(f'A média dos impostos pagos foi de R${mediaimpostos:.2f}')


print(imposto)
