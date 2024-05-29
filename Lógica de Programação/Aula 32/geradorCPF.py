from random import randint
numero = str(randint(10000000, 999999999));
novoCPF = numero;
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
print(novoCPF);
# sequencia = novoCPF == str(novoCPF[0]) * 11;
# if cpf == novoCPF and not sequencia:
#     print("Válido");
# else:
#     print("Inválido");