import unittest
from triangulos_final import identifica_triangulo

class TestTriangulo(unittest.TestCase):

    def test_equilatero(self):
        pontos = {'ponto_A': [0, 0], 'ponto_B': [2, 0], 'ponto_C': [1, 1.732]}
        self.assertEqual(identifica_triangulo(pontos), "equilátero")

    def test_isosceles(self):
        pontos = {'ponto_A': [0, 0], 'ponto_B': [4, 0], 'ponto_C': [2, 2.46]}
        self.assertEqual(identifica_triangulo(pontos), "isósceles")

    def test_escaleno(self):
        pontos = {'ponto_A': [0, 0], 'ponto_B': [3, 4], 'ponto_C': [5, 1]}
        self.assertEqual(identifica_triangulo(pontos), "escaleno")

    def test_invalido(self):
        pontos = {'ponto_A': [0, 0], 'ponto_B': [0, 0], 'ponto_C': [1, 1]}
        self.assertEqual(identifica_triangulo(pontos), "inválido")
    
    def test_equilatero(self):
        pontos = {'ponto_A': [0, 0], 'ponto_B': [6, 0], 'ponto_C': [3, 5]}
        self.assertEqual(identifica_triangulo(pontos), "equilátero")

if __name__ == '__main__':
    unittest.main()
