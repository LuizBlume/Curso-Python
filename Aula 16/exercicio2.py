# Faça um programa que pergunte a hora alo usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
hora = input("Informe um horário: ");
if hora.isdigit():
    hora = int(hora);
    if hora >= 0 and hora <= 11:
        print("Bom dia!");
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!");
    elif hora >= 18 and hora <= 23:
        print("Boa noite!");
    else: 
        print("Erro")
else: 
    print("Erro");