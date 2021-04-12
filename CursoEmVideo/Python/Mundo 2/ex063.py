#Calcular a sequência de Fibonacci e mostrar quantos termos o usuário desejar

termos = int(input("Quantos termos você quer mostrar? "));
t1 = 0;
t2 = 1;
print(t1, t2, end=' ');

t3 = t1 + t2;
print(t3, end=' ');
cont = 3;

while cont < termos:
    t1 = t2;
    t2 = t3;
    t3 = t1 + t2;
    print(t3, end=' ');
    cont += 1;










