# Colocar palavras em uma tupla e mostrar as vogais presentes em cada uma delas
                    #Código SIMPLIFICADO a partir da LINHA 14

palavras = ('BOLA', 'PATO', 'PIPA', 'LUA', 'ESCOLA');
vogais = ('A', 'E', 'I', 'O', 'U');

for palavra in palavras:
    print(f'\nA palavra {palavra} tem as vogais: ', end='');
    for letras in range(0, len(palavra)):
        for vogal in range(0, len(vogais)):
            if palavra[letras] == vogais[vogal]:
                print(vogais[vogal], end=' ');

''' CÓDIGO SIMPLIFICADO (GUANABARA)
for p in palavras:
    print(f'\n Na palavra {p} temos: ', end='');
    for letra in p:
        if letra in 'aeiou': 
        print(letra, end='');
        
'''


