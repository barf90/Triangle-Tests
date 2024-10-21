# Identificação de tipo de triângulo
# Elaborar os casos de teste
# Executar os casos de teste

import math
import matplotlib.pyplot as plt

# Dicionário para armazenar as coordenadas X e Y dos pontos to triangulo
pontos_triangulo = {'ponto_A' : [], 'ponto_B' : [], 'ponto_C': []}

# Descobrir o tamanho das retas de acordo com os pontos X,Y

# função para calcular distancia de dois pontos
def calcula_distancia(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return distancia



# loop para pegar coordenadas de cada ponto
for ponto in pontos_triangulo:
    try:
        x = float(input(f"Digite a coordenada X de {ponto}: "))
        y = float(input(f"Digite a coordenada Y de {ponto}: "))
    except:
        print("O valor digitado NÃO É UM NÚMERO!")
        

    pontos_triangulo[ponto] = [x, y]

print(pontos_triangulo)

distancia_AB = calcula_distancia(pontos_triangulo['ponto_A'][0], pontos_triangulo['ponto_A'][1], pontos_triangulo['ponto_B'][0], pontos_triangulo['ponto_B'][1])
distancia_BC = calcula_distancia(pontos_triangulo['ponto_B'][0], pontos_triangulo['ponto_B'][1], pontos_triangulo['ponto_C'][0], pontos_triangulo['ponto_C'][1])
distancia_CA = calcula_distancia(pontos_triangulo['ponto_A'][0], pontos_triangulo['ponto_A'][1], pontos_triangulo['ponto_C'][0], pontos_triangulo['ponto_C'][1])

epsilon = ((distancia_AB + distancia_BC + distancia_CA)/ 3) * 0.03

print(f"Lado a: {distancia_AB:.6f}")
print(f"Lado b: {distancia_BC:.6f}")
print(f"Lado c: {distancia_CA:.6f}")
# condição de existencia do triangulo
# Condição de existência do triângulo (usando and)
if abs(distancia_BC - distancia_CA) < distancia_AB < distancia_BC + distancia_CA and \
   abs(distancia_AB - distancia_CA) < distancia_BC < distancia_AB + distancia_CA and \
   abs(distancia_AB - distancia_BC) < distancia_CA < distancia_AB + distancia_BC:

    # Comparação com tolerância (epsilon)
    if abs(distancia_AB - distancia_BC) < epsilon and abs(distancia_BC - distancia_CA) < epsilon:
        print("O triângulo é equilátero")
    elif abs(distancia_AB - distancia_BC) < epsilon or abs(distancia_BC - distancia_CA) < epsilon or abs(distancia_CA - distancia_AB) < epsilon:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")

    valores_x = [pontos_triangulo['ponto_A'][0], pontos_triangulo['ponto_B'][0], pontos_triangulo['ponto_C'][0], pontos_triangulo['ponto_A'][0]]
    valores_y = [pontos_triangulo['ponto_A'][1], pontos_triangulo['ponto_B'][1], pontos_triangulo['ponto_C'][1], pontos_triangulo['ponto_A'][1]]

    # Plotando os pontos e o triângulo
    plt.plot(valores_x, valores_y, marker='o', linestyle='-', color='b', label='Triângulo')

    # Adicionando etiquetas nos pontos
    plt.text(pontos_triangulo['ponto_A'][0], pontos_triangulo['ponto_A'][1], 'A', fontsize=12, ha='right')
    plt.text(pontos_triangulo['ponto_B'][0], pontos_triangulo['ponto_B'][1], 'B', fontsize=12, ha='right')
    plt.text(pontos_triangulo['ponto_C'][0], pontos_triangulo['ponto_C'][1], 'C', fontsize=12, ha='right')

    # Ajustes no gráfico
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico do Triângulo')
    plt.grid(True)
    plt.legend()

    # Exibir o gráfico
    plt.show()

else:
    print(f"Digite um triângulo válido!")


