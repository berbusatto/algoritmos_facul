sexo_cliente = input('sexo: ')
sexo_cliente.lower()
tempo_cliente = int(input('quanto tempo é cliente: '))
valor_compra = float(input('valor da compra: '))

if sexo_cliente == 'm':
    if valor_compra > 300.00:
        if tempo_cliente > 5:
            print('30%')
        else:
            print('20%')
    else:
        print('10%')
else:
    if valor_compra > 450.00:
        if tempo_cliente > 5:
            print('35%')
        else:
            print('25%')
    else:
        print('15%')