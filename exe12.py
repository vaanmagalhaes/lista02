#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
import math

#ENTRADA
valor_hora = float(input('Digite quanto você ganha por hora:'))
horastrab = float(input('Digite quantas horas você trabalhou este mês:'))

#PROCESSAMENTO
salariobruto = valor_hora * horastrab
INSS = salariobruto * (10 / 100)
SIND = salariobruto * (3 / 100)
FGTS = salariobruto * (11 / 100)

if salariobruto < 900:
    IR = salariobruto * 0
    perc = 'isento'

elif salariobruto > 900 and salariobruto < 1500:
    IR = salariobruto * (5/100)
    perc = '(5%)'
    
elif salariobruto > 1500 and salariobruto < 2500:
    IR = salariobruto * (10/100)
    perc = '(10%)'

else:
    IR = salariobruto * (20/100)
    perc = '(20%)'
    
descontos = IR + INSS + SIND
salarioliquido = salariobruto - descontos

#SAÍDA
print('Salário Bruto: R$:', salariobruto)
print('(-) IR', perc, 'R$:', IR)
print('(-) Sindicato (3%) R$:', SIND)
print('(-) INSS (10%) R$:', INSS)
print('FGTS (11%) R$:', FGTS)
print('O total de descontos é de R$:', descontos)
print('Salário Líquido R$:', salarioliquido)