#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#ENTRADA

pro1 = float(input('Digite o valor do primeiro produto:'))
pro2 = float(input('Digite o valor do segundo produto:'))
pro3 = float(input('Digite o valor do terceiro produto:'))

# PROCESSAMENTO

if pro1 < pro2 and pro1 < pro3:
    print('Compre o primeiro produto.')
elif pro2 < pro1 and pro2 < pro3:
    print('Compre o segundo produto.')
else:
    print('Compre o terceiro produto.')