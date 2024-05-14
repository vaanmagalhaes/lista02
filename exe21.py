#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
import math

#ENTRADA
valor = int(input('Digite o valor a ser sacado:'))

#PROCESSAMENTO
if valor<10 or valor>600:
    print('Valor indisponível. Digite um valor maior que R$10,00 e menor que R$600,00.')
    
else:
    notacem = valor // 100
    valor -= notacem * 100
    notacinquenta = valor // 50
    valor -= notacinquenta * 50
    notadez = valor // 10
    valor -= notadez * 10
    notacinco = valor // 5
    valor -= notacinco * 5
    notaum = valor
    if notacem == 1:
        print(int(notacem), "Nota de R$100,00")
    elif notacem > 1:
        print(int(notacem), "Notas de R$100,00")
    if notacinquenta == 1:
        print(int(notacinquenta), "Nota de R$50,00")
    elif notacinquinta > 1:
        print(int(notacinquenta), "Notas de R$50,00")
    if notadez == 1:
        print(int(notadez), "Nota de R$10,00")
    elif notadez > 1:
        print(int(notadez), "Notas de R$10,00")
    if notacinco == 1:
        print(int(notacinco), "Nota de R$5,00")
    elif notacinco > 1:
        print(int(notacinco), "Notas de R$5,00")
    if notaum == 1:
        print(int(notaum), "Nota de R$50,00")
    elif notaum > 1:
        print(int(notaum), "Notas de R$50,00")