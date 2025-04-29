from src.persona import Persona

class Profesor(Persona):
    """Clase que representa a un profesor en el sistema educativo.
    
    Hereda de la clase Persona y agrega el atributo de sueldo.
    
    Attributes:
        nombre (str): Nombre del profesor.
        apellido (str): Apellido del profesor.
        dni (str): Número de DNI del profesor.
        sueldo (float): Sueldo del profesor.
    """
    
    def __init__(self, nombre, apellido, dni, sueldo):
        """Inicializa una nueva instancia de Profesor.
        
        Args:
            nombre (str): Nombre del profesor.
            apellido (str): Apellido del profesor.
            dni (str): Número de DNI del profesor.
            sueldo (float): Sueldo del profesor.
            
        Raises:
            ValueError: Si el sueldo es menor o igual a cero.
        """
        super().__init__(nombre, apellido, dni)
        
        if sueldo <= 0:
            raise ValueError("El sueldo debe ser mayor a cero")
            
        self.sueldo = sueldo
    
    def __repr__(self):
        """Representación en cadena del profesor.
        
        Returns:
            str: Representación textual del profesor.
        """
        return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"