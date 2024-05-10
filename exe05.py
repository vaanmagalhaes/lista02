# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# ENTRADA
nota1 = float(input('Nota do 1º bim:'))
nota2 = float(input('Nota do 2ª bim:'))
nota3 = float(input('Nota do 3ª bim:'))
nota4 = float(input('Nota do 4º bim:'))

# PROCESSAMENTO
media = (nota1 + nota2 + nota3 + nota4) / 4

# SAÍDA
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')