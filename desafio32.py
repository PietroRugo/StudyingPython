salario = float(input('Entre com o seu salario'))
if salario > 1250:
    aumento = salario + (10/100)
    print('Seu salário aumentado:{} '.format(salario/10))
else:
    aumento = salario + (15/100)
print('Seu aumento foi de {}: '.format(aumento))