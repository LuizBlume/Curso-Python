"""
Split, Join, Enumerate em Python
* Split Dividir uma string # str -
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
string = 'o Brasil é o país do futebol, o Brasil é penta.'
l1 = string.split(" ");
l2 = string.split(',');
palavra =  '';
contagem = 0;
for valor in l1:
    qtdVezes = l1.count(valor);
    if qtdVezes > contagem:
        contagem = qtdVezes;
        palavra = valor;
print(f'A palavra que apareceu mais vezes foi "{palavra}" ({contagem}x)')