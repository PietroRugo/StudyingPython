velocidade = float(input('Velocidade atingida pelo Veiculo ' ))
if velocidade > 80:
    print('Multado, vagabundo')
    multa = (velocidade-80)*7
    print('O valor da multa é a velocidade ultrapassada x7, no seu caso seria : {:.0f}'.format(multa)+'R$')
else:
    print('Tranquilo ! Você não ultrapassou os 80KM/H')

