# Desafio
nome = 'Luiz';
idade = 17;
altura = 1.77;
peso = 80;
anoAtual = 2024;
dataNasc = anoAtual - idade;
imc = peso / (altura ** 2);
print(f'{nome} tem {idade} anos');
print(f'Nasceu no ano de {dataNasc}');
print(f'Seu IMC é de {imc:.2f}');
