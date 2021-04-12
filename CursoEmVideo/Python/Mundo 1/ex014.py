#Ler a temperatura em celsius e converter para fahrenheit

celsius = float(input("Informe a temperatura em graus C°: "));
f = (1.8 * celsius) + 32;
#f= ((9 * celsius / 5) + 32;

print(f"A temperatura de \033[33m{celsius}°C\033[m equivale à \033[34m{f}°F\033[m.");
