"""
Split, Join, Enumerate em Python
* Split Dividir uma string # str -
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
string = 'o Brasil é o país do futebol, o Brasil é penta.'
l1 = string.split(" ");
l2 = string.split(',');
for valor in l1:
    print(f'A palavra {valor} apareceu {l1.count(valor)}x na frase.');
