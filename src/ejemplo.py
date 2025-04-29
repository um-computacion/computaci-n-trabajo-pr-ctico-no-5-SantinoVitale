#!/usr/bin/env python3
"""
Ejemplo de uso del sistema de gestión de personas en una institución educativa.
Este script muestra cómo utilizar las clases implementadas.
"""

from persona import Persona
from profesor import Profesor
from alumno import Alumno

def main():
    """Función principal que demuestra el uso del sistema."""
    
    print("==== Sistema de Gestión de Personas ====")
    print("\n1. Creando instancias de diferentes personas:")
    
    # Crear una persona común
    try:
        persona = Persona("María", "González", "35689452")
        print(f"Persona creada: {persona}")
    except ValueError as e:
        print(f"Error al crear persona: {e}")
    
    # Crear un profesor
    try:
        profesor = Profesor("Carlos", "Rodríguez", "25478963", 75000)
        print(f"Profesor creado: {profesor}")
    except ValueError as e:
        print(f"Error al crear profesor: {e}")
    
    # Crear un alumno
    try:
        alumno = Alumno("Lucía", "Fernández", "42568971", "A578")
        print(f"Alumno creado: {alumno}")
    except ValueError as e:
        print(f"Error al crear alumno: {e}")
    
    print("\n2. Demostración de herencia y comportamiento:")
    
    # Hacer que las personas piensen
    persona.pensar("Qué lindo día para caminar")
    profesor.pensar("Debo preparar el examen final")
    alumno.pensar("Necesito estudiar para el parcial")
    
    print(f"\nDespués de pensar:")
    print(f"Persona: '{persona.ultima_idea}' (Pensamientos: {persona.pensamientos})")
    print(f"Profesor: '{profesor.ultima_idea}' (Pensamientos: {profesor.pensamientos})")
    print(f"Alumno: '{alumno.ultima_idea}' (Pensamientos: {alumno.pensamientos})")
    
    print("\n3. Demostración de validación de datos:")
    
    # Intentar crear instancias con datos inválidos
    print("\nIntentos con datos inválidos:")
    
    try:
        persona_invalida = Persona("", "López", "12345678")
    except ValueError as e:
        print(f"- Error (nombre vacío): {e}")
    
    try:
        profesor_invalido = Profesor("Juan", "Pérez", "12345678", -5000)
    except ValueError as e:
        print(f"- Error (sueldo negativo): {e}")
    
    try:
        alumno_invalido = Alumno("Ana", "Martínez", "12345678", "123")
    except ValueError as e:
        print(f"- Error (formato de legajo): {e}")
    
    print("\n==== Fin del ejemplo ====")

if __name__ == "__main__":
    main()