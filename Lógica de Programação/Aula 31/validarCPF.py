while True:
    cpf = input('Digite um CPF: ')
    novoCPF = cpf[:-2];
    reverso = 10;
    total = 0;
    for index in range(19):
        if index > 8:
            index -= 9;
        total += int(novoCPF[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11;
            d = 11 - (total  % 11)
            if d > 9:
                d = 0;
            total = 0;
            novoCPF += str(d);
    if cpf == novoCPF:
        print("Válido");
    else:
        print("Inválido");