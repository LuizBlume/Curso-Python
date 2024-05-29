variavel = ["Luiz", "Fernando", "Joãozinho", "Maria"];
for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)