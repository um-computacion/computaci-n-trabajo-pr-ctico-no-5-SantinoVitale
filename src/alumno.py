from src.persona import Persona

class Alumno(Persona):
    """Clase que representa a un alumno en el sistema educativo.
    
    Hereda de la clase Persona y agrega el atributo de legajo.
    
    Attributes:
        nombre (str): Nombre del alumno.
        apellido (str): Apellido del alumno.
        dni (str): Número de DNI del alumno.
        legajo (str): Número de legajo del alumno.
    """
    
    def __init__(self, nombre, apellido, dni, legajo):
        """Inicializa una nueva instancia de Alumno.
        
        Args:
            nombre (str): Nombre del alumno.
            apellido (str): Apellido del alumno.
            dni (str): Número de DNI del alumno.
            legajo (str): Número de legajo del alumno.
            
        Raises:
            ValueError: Si el legajo está vacío.
            ValueError: Si el legajo no tiene el formato correcto (letra seguida de números).
        """
        super().__init__(nombre, apellido, dni)
        
        if not legajo:
            raise ValueError("El legajo no puede estar vacío")
            
        if not (legajo[0].isalpha() and legajo[1:].isdigit()):
            raise ValueError("El legajo debe comenzar con una letra seguida de números")
            
        self.legajo = legajo
    
    def __repr__(self):
        """Representación en cadena del alumno.
        
        Returns:
            str: Representación textual del alumno.
        """
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"