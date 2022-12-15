'''
Exercício 1 - Limites

Bárbara Martins Barbieri
Engenharia de Software (GES) - Matrícula: 140

'''

# Importa as funções da biblioteca 'sympy'
from sympy import Limit, Symbol, S

# Cálculo da constante com base no número de matrícula
c = 140 % 10

# Define a função f(x)
def funcao(x):
    return ((2 * x ** 4 - 2) / (5 - 5 * x ** 2)) * (c + 4)

# Define x como uma variável
x = Symbol('x')



# Cálculo dos limites

# Limite 1 
limite = Limit(funcao(x), x, 1).doit()
print('Limite de f(x) para x -> 1: ', limite)

# Limite 2
limite = Limit(funcao(x), x, S.Infinity).doit()
print('Limite de f(x) para x -> +oo: ', limite)

# Limite 3
limite = Limit(funcao(x), x, -S.Infinity).doit()
print('Limite de f(x) para x -> -oo: ', limite)
