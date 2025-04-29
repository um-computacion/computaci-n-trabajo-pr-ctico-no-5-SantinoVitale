import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

    def test_repr_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)
        
    def test_pensar_incrementa_contador(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.ultima_idea, "Hola mundo")
        
    def test_dni_solo_numeros(self):
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", "ABC123")
            
    def test_dni_longitud_correcta(self):
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", "123")
            
    def test_nombre_apellido_no_vacios(self):
        with self.assertRaises(ValueError):
            Persona("", "Pérez", "12345678")
        with self.assertRaises(ValueError):
            Persona("Juan", "", "12345678")
            
    def test_pensamientos_multiples(self):
        persona = Persona("Juan", "Pérez", "12345678")
        ideas = ["Idea 1", "Idea 2", "Idea 3"]
        for idea in ideas:
            persona.pensar(idea)
        self.assertEqual(persona.pensamientos, len(ideas))
        self.assertEqual(persona.ultima_idea, ideas[-1])

if __name__ == "__main__":
    unittest.main()