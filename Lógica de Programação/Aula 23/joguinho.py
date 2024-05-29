secreto = 'perfume';
digitadas = [];
chances = 3;
while True:
    if chances <= 0:
        print("Você perdeu!!");
        break;
    letra = input('Digite uma letra: ');
    if len(letra) > 1:
        print("Isso não vale, apenas uma letra.")
        continue;
    digitadas.append(letra)
    if letra in secreto:
        print(f'A letra "{letra}" está correta!!');
    else:
        print(f'A letra "{letra}" não está na palavra!');
        digitadas.pop();
    secretoTemporario = '';
    for letraSecreta in secreto:
        if letraSecreta in digitadas:
            secretoTemporario += letraSecreta;
        else:
            secretoTemporario += '*';
    if secretoTemporario == secreto:
        print(f'Parabéns, VOCÊ GANHOU!!! A palavra era {secreto}');
        break;
    else:
        print(f'A palavra secreta está assim: {secretoTemporario}')
    if letra not in secreto:
        chances -= 1;
    print(f'Você ainda tem {chances} chances.')
    print()