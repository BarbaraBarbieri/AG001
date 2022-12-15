'''
Exercício 4 - Leis de Kirchoff (sistemas lineares)

Bárbara Martins Barbieri
Engenharia de Software (GES) - Matrícula: 140

'''

# Importa as funções da biblioteca 'sympy'
from sympy import Symbol, solve

# Cálculo da constante com base no número de matrícula
c = 140 % 10


# Define as constantes da malha

# Valores das fontes de tensão
V1 = 10 + 2 * c
V2 = 5 + 2 * c

# Valores dos resistores
R1 = 10
R2 = 20
R3 = 25


# Define as equações do circuito

# Lei dos Nós
def no(i1, i2, i3):
    return i1 + i2 + i3

# Lei das Malhas - Malha 1
def malha1(i1, i3):
    return - V1 + R1 * i1 - R3 * i3 + V2

# Lei das Malhas - Malha 2
def malha2(i1, i2):
    return - V1 + R1 * i1 - R2 * i2

# Lei das Malhas - Malha 3
def malha3(i2, i3):
    return R2 * i2 - R3 * i3 + V2

    
# Define i1, i2 e i3 como variáveis
i1 = Symbol('i1')
i2 = Symbol('i2')
i3 = Symbol('i3')



# Resolve o sistema de equações e calcula o valor das correntes
m1 = malha1(i1, i3)
m2 = malha2(i1, i2)
m3 = malha3(i2, i3)
n = no(i1, i2, i3)
correntes = solve((m1, m2, m3, n))

print('Corrente 1: ', correntes[i1])
print('Corrente 2: ', correntes[i2])
print('Corrente 3: ', correntes[i3])
