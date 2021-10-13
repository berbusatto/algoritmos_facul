# nome = input('Digite o nome: ')
# salario = float(input('Digite o Salário: '))
#
# if salario <= 1903.98:
#     imposto = 0.00
#     liquido = salario
# elif salario <= 2826.65:
#     imposto = (salario * 0.075) - 142.80
#     liquido = salario -imposto
# elif salario <= 3751.05:
#     imposto = (salario * 0.15) - 354.80
#     liquido = salario - imposto
# elif salario <= 4664.68:
#     imposto = (salario * 0.225) - 636.13
#     liquido = salario - imposto
# else:
#     imposto = (salario * 0.275) - 869.36
#     liquido = salario - imposto
# print(f'O funcionário {nome} recebe R${salario:.2f} por mês, paga R${imposto:.2f} em IR e recebe um salário líquido de R${liquido:.2f}.')
#

num1 = float(input('Digite um número: '))
op = input('Digite uma operação matemática: ')
num2 = float(input('Digite um número: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num1 == 0 or num2 == 0:
        print('Impossível dividir por zero')
        pass
    else:
        print(num1 / num2)
else:
    print('Digite um operador válido + - * / ')
