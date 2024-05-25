"""
Formatando valores com modificadores 
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO) - Quantidade de casas decimais (float) 
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
"""
n1 = 1;
print(f'{n1:0>10}');
n2 = 10;
print(f'{n2:0<10}');
n3 = 100;
print(f'{n3:0^10}');