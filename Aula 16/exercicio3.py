# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
nome = input("Informe seu primeiro nome: ");
tamanho = len(nome);
if tamanho <= 4:
    print("Seu nome é curto");
elif tamanho > 4 and tamanho <= 6:
    print("Seu nome é normal");
elif tamanho > 6:
    print("Seu nome é muito grande");
else:
    print("Erro");