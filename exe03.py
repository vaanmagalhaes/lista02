# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# .capitalize (torna a primeira letra em maiusculo automaticamente)
# .upper (torna todas as letras em maiusculo)

# ENTRADA
gen = input('Qual o seu gênero?')

#PROCESSAMENTO/SAÍDA
if gen in ['F', 'f']:
    print('Sexo feminino')
elif gen in ['M', 'm']:
    print('Sexo masculino')
else:
    print('Sexo inválido')