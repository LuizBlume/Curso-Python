# Indices
#        0123456789.......................33;
frase = 'O rato roeu a roupa do rei de roma'; # Iterável
tamanhoFrase = len(frase)
contador = 0;
novaString = '';
usuario = input("Qual letra deseja colocar maiúscula: ");
while contador < tamanhoFrase:
    letra = frase[contador]
    if letra == usuario:
        novaString += usuario.upper();
    else:
        novaString += letra;
    contador += 1;
print(novaString)