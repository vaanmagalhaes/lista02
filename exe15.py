#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
import math

#ENTRADA
lado1 = float(input('Digite o primeiro lado do triângulo:'))
lado2 = float(input('Digite o segundo lado do triângulo:'))
lado3 = float(input('Digite o terceiro lado do triângulo:'))

#PROCESSAMENTO
if lado1 > (lado2+lado3) or lado2 > (lado1+lado3) or lado3 > (lado1+lado2):
    resposta = 'Não é um triângulo.'
elif lado1 == lado2 == lado3:
    resposta = 'Triângulo Equilátero'
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    resposta = 'Triângulo Isósceles'
else:
    resposta = 'Triângulo Escaleno'
    
#SAÍDA
print(resposta)