from src.persona import Persona

class Profesor(Persona):
  """
  Clase que representa a un profesor, hereda de Persona.
  
  Attributes:
    nombre (str): Nombre del profesor.
    apellido (str): Apellido del profesor.
    dni (str): Número de documento del profesor.
    sueldo (float): Sueldo del profesor.
  """
  
  def __init__(self, nombre, apellido, dni, sueldo):
    """
    Inicializa una nueva instancia de Profesor.
    
    Args:
      nombre (str): Nombre del profesor.
      apellido (str): Apellido del profesor.
      dni (str): Número de documento del profesor.
      sueldo (float): Sueldo del profesor.
    """
    super().__init__(nombre, apellido, dni)
    self.sueldo = sueldo
  
  def __repr__(self):
    """
    Devuelve una representación en string del profesor.
    
    Returns:
      str: Representación del profesor.
    """
    return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"