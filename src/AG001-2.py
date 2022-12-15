'''
Exercício 2 - Cinemática (integral e derivada)

Bárbara Martins Barbieri
Engenharia de Software (GES) - Matrícula: 140

'''

# Importa as funções da biblioteca 'sympy'
from sympy import Derivative, Symbol

# Cálculo da constante com base no número de matrícula
c = 140 % 10

# Define a função do deslocamento
def deslocamento(t):
    return t ** (1/4) + (1 / (t ** 2)) - 3 * c

# Define t como uma variável
t = Symbol('t')



# Cálculo da equação da velocidade
velocidade = Derivative(deslocamento(t), t).doit()
print('Equação da velocidade: ', velocidade)

# Cálculo do valor da velocidade para t = 7s
resultado = velocidade.subs({t:7})
print('Velocidade para t = 7s: ', round(float(resultado), 3))

# Cálculo da equação da aceleração
aceleracao = Derivative(deslocamento(t), t, 2).doit()
print('Equação da aceleração: ', aceleracao)

# Cálculo do valor da aceleração para t = 2s
resultado = aceleracao.subs({t:2})
print('Aceleração para t = 2s: ', round(float(resultado), 3))
