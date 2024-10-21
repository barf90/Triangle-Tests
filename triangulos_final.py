import math

# Função para calcular a distância entre dois pontos
def calcula_distancia(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

# Função para identificar o tipo de triângulo
def identifica_triangulo(pontos_triangulo):
    distancia_AB = calcula_distancia(pontos_triangulo['ponto_A'][0], pontos_triangulo['ponto_A'][1], pontos_triangulo['ponto_B'][0], pontos_triangulo['ponto_B'][1])
    distancia_BC = calcula_distancia(pontos_triangulo['ponto_B'][0], pontos_triangulo['ponto_B'][1], pontos_triangulo['ponto_C'][0], pontos_triangulo['ponto_C'][1])
    distancia_CA = calcula_distancia(pontos_triangulo['ponto_A'][0], pontos_triangulo['ponto_A'][1], pontos_triangulo['ponto_C'][0], pontos_triangulo['ponto_C'][1])

    epsilon = ((distancia_AB + distancia_BC + distancia_CA)/ 3) * 0.03
    # Condição de existência do triângulo
    if abs(distancia_BC - distancia_CA) < distancia_AB < distancia_BC + distancia_CA and \
       abs(distancia_AB - distancia_CA) < distancia_BC < distancia_AB + distancia_CA and \
       abs(distancia_AB - distancia_BC) < distancia_CA < distancia_AB + distancia_BC:
        
        # Comparação com tolerância (epsilon)
        if abs(distancia_AB - distancia_BC) < epsilon and abs(distancia_BC - distancia_CA) < epsilon:
            return "equilátero"
        elif abs(distancia_AB - distancia_BC) < epsilon or abs(distancia_BC - distancia_CA) < epsilon or abs(distancia_CA - distancia_AB) < epsilon:
            return "isósceles"
        else:
            return "escaleno"
    else:
        return "inválido"
