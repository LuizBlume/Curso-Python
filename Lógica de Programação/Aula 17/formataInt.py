"""
Formatando valores com modificadores 
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO) - Quantidade de casas decimais (float) 
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
"""
n1 = 10;
n2 = 3;
divisao = n1 / n2;
print('{:.2f}'.format(divisao));