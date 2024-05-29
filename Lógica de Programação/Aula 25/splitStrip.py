string = 'o Brasil é o país do futebol, o Brasil é penta.'
l1 = string.split(" ");
l2 = string.split(',');
for valor in l2:
    print(valor.strip().capitalize());