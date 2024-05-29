# Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe uma mensagem de erro.

n1 = input("Digite um número inteiro: ");
if n1.isdigit():
    n1 = int(n1)
    if n1 % 2 == 0:
        print(f'O número {n1} é par');
    else: 
        print(f'O número {n1} é ímpar');
else: 
    print("O número não é inteiro")