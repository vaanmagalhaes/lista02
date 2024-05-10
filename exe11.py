#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
import math

#ENTRADA
salario = float(input('Digite o salário do funcionário:'))

#PROCESSAMENTO
if salario <= 280:
    perc = '20%'
    salarioajustado = salario * 1.20
    valor_ajuste = salarioajustado - salario
    
elif salario > 280 and salario < 700:
    perc = '15%'
    salarioajustado = salario * 1.15
    valor_ajuste = salarioajustado - salario
    
elif salario > 700 and salario < 1500:
    perc = '10%'
    salarioajustado = salario * 1.10
    valor_ajuste = salarioajustado - salario
    
else:
    perc = '5%'
    salarioajustado = salario * 1.05
    valor_ajuste = salarioajustado - salario
    
print('Salário antes do reajuste:', salario)
print('Percentual do aumento:', perc)
print('Valor do aumento:', math.ceil(valor_ajuste))
print('Novo salário:', math.ceil(salarioajustado))