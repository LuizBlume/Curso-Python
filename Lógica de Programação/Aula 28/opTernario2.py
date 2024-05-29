idade = input('Qual a sua idade: ');
if not idade.isnumeric():
    print('Você precisa digitar pelo menos um número');
else:
    idade = int(idade);
    maior = (idade >= 18);
    msg = 'Pode acessar' if maior else 'Não pode acessar';
    print(msg)