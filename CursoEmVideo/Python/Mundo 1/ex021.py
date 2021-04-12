# Encontrar e executar um arquivo de audio aqui
# Necessário: colar/colocar o arquivo mp3 ou o audio na pasta do projeto

from pygame import mixer

mixer.init();
# Inicia o módulo;

mixer.music.load('ex021.mp3');
# Carrega o arquivo desejado;

mixer.music.play();
# Executa a música;

input("Agora você escuta? ");
#Dá o play e assim que o input for respondido, a música para;

# Pode-se usar também o comando:
#while mixer.music.get_busy(): pass;
