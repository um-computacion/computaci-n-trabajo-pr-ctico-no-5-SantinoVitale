import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_crear_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.dni, "12345678")
        self.assertEqual(alumno.legajo, "A123")

    def test_repr_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Legajo: A123"
        self.assertEqual(str(alumno), expected)
        
    def test_herencia_persona(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        alumno.pensar("Tengo que estudiar más")
        self.assertEqual(alumno.pensamientos, 1)
        self.assertEqual(alumno.ultima_idea, "Tengo que estudiar más")
        
    def test_legajo_no_vacio(self):
        with self.assertRaises(ValueError):
            Alumno("Juan", "Pérez", "12345678", "")
            
    def test_legajo_formato_valido(self):
        # Comprueba que el legajo comience con una letra y luego tenga números
        with self.assertRaises(ValueError):
            Alumno("Juan", "Pérez", "12345678", "123A")  # Formato incorrecto
        
        # Esto debería funcionar (formato correcto)
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        self.assertEqual(alumno.legajo, "A123")

if __name__ == "__main__":
    unittest.main()