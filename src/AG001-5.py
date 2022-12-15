'''
Exercício 5 - Equações

Bárbara Martins Barbieri
Engenharia de Software (GES) - Matrícula: 140

'''

# Importa as funções da biblioteca 'sympy'
from sympy import Symbol, solve, cos, exp

# Cálculo da constante com base no número de matrícula
c = 140 % 10


# Define as equações

def equacao1(x):
    return exp(x - 2) + exp(x - 4) + exp(x) - 5 * (c + 1)

def equacao2(x):
    return 3 * x ** 3 - 2 * x ** 2 - 5 * x - 4 * c

def equacao3(x):
    return 2 * cos(4 * (c + 1) * x) + 5


# Define x como uma variável
x = Symbol('x')



# Cálculo das equações

# Equação 1
equacao = equacao1(x)
resultado = solve(equacao)
print('Resultado da primeira equação: ', resultado)

# Equação 2
equacao = equacao2(x)
resultado = solve(equacao)
print('Resultado da primeira equação: ', resultado)

# Equação 3
equacao = equacao3(x)
resultado = solve(equacao)
print('Resultado da primeira equação: ', resultado)
