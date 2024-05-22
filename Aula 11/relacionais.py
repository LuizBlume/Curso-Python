nome = input("Digite seu nome: ");
idade = int(input("Qual a sua idade? "));
idadeLimite = 18;
if idade >= idadeLimite: 
    print(f'{nome} pode realizar o emprestimo');
elif idade < idadeLimite: 
    print(f'{nome} nao pode realizar o emprestimo');
else:
    print('Erro')