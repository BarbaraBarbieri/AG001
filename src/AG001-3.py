'''
Exercício 3 - Área do gráfico (integral)

Bárbara Martins Barbieri
Engenharia de Software (GES) - Matrícula: 140

'''

# Importa as funções da biblioteca 'sympy'
from sympy import Integral, Symbol

# Cálculo da constante com base no número de matrícula
c = 140 % 10

# Define a função da curva
def funcao(x):
    return 1/(x ** (1/3)) - x ** 5 - 6 * x - 2 * c
    
# Define x como uma variável
x = Symbol('x')



# Cálculo da área sob a curva
resultado = Integral(funcao(x), (x, 3, 6)).doit()
print('Área sob a curva entre os pontos 3 e 6: ', round(float(resultado), 3))
