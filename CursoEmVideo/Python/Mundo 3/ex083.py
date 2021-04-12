# Ler uma expressão matemática e verificar se os parênteses estão fechados corretamente

expressao = str(input('Digite a expressão a ser analisada: '));
pilha = [];

for i in expressao:
    if i == "(":
        pilha.append('(')
    elif i == ")":
        if len(pilha) > 0:
            pilha.pop();
        elif len(pilha) == 0:
            pilha.append(')');
            break;
if len(pilha) == 0:
    print('Sua expressão é válida!');
else:
    print('Sua expressão está errada.')





