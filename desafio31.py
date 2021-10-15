dist = float(input('Entre com a distância de uma viagem em KM'))
if dist <= 200:
    preço = (dist * 0.50)
    print('Valor da sua passagem: {}'.format(preço))
else:
    preço = (dist * 0.45)
print('Valor da sua passagem: {}'.format(preço))
