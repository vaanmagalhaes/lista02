# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# ENTRADA
letra = input('Digite uma letra:')
letra = letra.capitalize()

# PROCESSAMENTO/SAÍDA
if letra in ['A','E','I','O','U']:
    print(letra, 'é uma vogal')
elif letra in ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','W','Y','Z']:
    print(letra, 'é uma consoante')
else:
    print('Caracter inválido')