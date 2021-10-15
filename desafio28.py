import random
computador = [0,1,2,5]
computadornum = random.choice(computador)
num = input('Tente adivinhar o número do computador de 0 a 5 ')
if num == computadornum:
    print("Parabéns você acertou !!")
else:
    print('Você errou. Numero do Computador: {}'.format(computadornum))
