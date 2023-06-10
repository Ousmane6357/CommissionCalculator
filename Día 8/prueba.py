import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra= 'Hola mundo'
        resultado= cambia_texto.todo_mayusculas(palabra)
        self.assertEquals(resultado, 'HOLA MUNDO')


if __name__ == '__main__':
    unittest.main()
