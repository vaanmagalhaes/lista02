#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.
import math

#ENTRADA
nota1 = float(input('Digite a nota do 1º bimestre:'))
nota2 = float(input('Digite a nota do 2º bimestre:'))
nota3 = float(input('Digite a nota do 3º bimestre:'))
media = (nota1+nota2+nota3)/3

#PROCESSAMENTO/SAÍDA
if media>=7 and media<10:
    print('Aprovado! Sua média final é:', media)
elif media<7:
    print('Reprovado! Sua média final é:', media)
elif media==10:
    print('Aprovado com distinção, parabéns!')