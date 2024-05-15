# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
import math

# ENTRADA
valor_a = 1.90
valor_g = 2.50
adescontomin = 3/100
adescontomax = 5/100
gdescontomin = 4/100
gdescontomax = 6/100
combustivel = input('Tipo de combustível: A - Álcool e G - Gasolina?')
combustivel = combustivel.capitalize()
litros = float(input('Quantos litros foram vendidos?'))

# PROCESSAMENTO
if combustivel == 'A':
    preco = litros*valor_a
    preco = round(preco,2)
elif combustivel == 'G':
    preco = litros*valor_g
    preco = round(preco,2)
else:
    print('ERRO. Dado inválido.')

if combustivel == 'A' and litros<=20:
    precofinal = preco*adescontomin
    precofinal = round(precofinal,2)
    print('O total é R$:', (preco-precofinal))

elif combustivel == 'A' and litros>20:
    precofinal = preco*adescontomax
    precofinal = round(precofinal,2)
    print('O total é R$:', (preco - precofinal))

elif combustivel == 'G' and litros<=20:
    precofinal = preco*gdescontomin
    precofinal = round(precofinal,2)
    print('O total é R$:', (preco-precofinal))

elif combustivel == 'G' and litros>20:
    precofinal = preco*gdescontomax
    precofinal = round(precofinal,2)
    print('O total é R$:', (preco-precofinal))
