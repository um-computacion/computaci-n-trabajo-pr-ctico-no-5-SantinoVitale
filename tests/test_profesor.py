import unittest
from src.profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_crear_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.apellido, "Pérez")
        self.assertEqual(profesor.dni, "12345678")
        self.assertEqual(profesor.sueldo, 50000)

    def test_repr_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000"
        self.assertEqual(str(profesor), expected)
        
    def test_herencia_persona(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        profesor.pensar("Como mejorar mis clases")
        self.assertEqual(profesor.pensamientos, 1)
        self.assertEqual(profesor.ultima_idea, "Como mejorar mis clases")
        
    def test_sueldo_positivo(self):
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", -1000)
            
    def test_sueldo_cero(self):
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", 0)

if __name__ == "__main__":
    unittest.main()