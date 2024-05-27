texto = "Python";
novaString = ''; 
for letra in texto:
    if letra == "t":
        # continue;
        novaString = novaString + letra.upper();
    elif letra == "h":
        novaString += letra.upper();
        # break;
    else:
        novaString += letra;
print(novaString);

# Continue - Pula para o próximo laço
# Break - Termina o laço