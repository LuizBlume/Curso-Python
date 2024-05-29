# isdigit
n1 = input("Digite um número: ");
n2 = input("Digite outro número: ");
try:
    n1 = float(n1);
    n2 = float(n2);
    print(n1 + n2);
except: 
    print("Não pude converter os números para realizar a conta")