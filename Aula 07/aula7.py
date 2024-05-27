nome = "Luiz Fernando"; # str
idade = 16; # int
altura = 1.77; # float
maior = idade >= 18; # boolean
peso = 80; # int
imc = peso / (altura ** 2);
print(f'{nome} tem {idade} anos de idade e seu imc e de {imc:.2f}');
print('{} tem {} anos de idade e seu imc e de {:.2f}'.format(nome, idade, imc))