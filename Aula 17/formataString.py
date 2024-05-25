"""
Formatando valores com modificadores 
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO) - Quantidade de casas decimais (float) 
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
"""
nome = "Luiz";
print(f'{nome:s}')
nomeFormatado = "{:@>50}".format(nome);
print(nomeFormatado);