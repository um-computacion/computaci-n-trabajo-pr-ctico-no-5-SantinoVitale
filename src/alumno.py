from src.persona import Persona

class Alumno(Persona):
  """
  Clase que representa a un alumno, hereda de Persona.
  
  Attributes:
    nombre (str): Nombre del alumno.
    apellido (str): Apellido del alumno.
    dni (str): Número de documento del alumno.
    legajo (str): Número de legajo del alumno.
  """
  
  def __init__(self, nombre, apellido, dni, legajo):
    """
    Inicializa una nueva instancia de Alumno.
    
    Args:
      nombre (str): Nombre del alumno.
      apellido (str): Apellido del alumno.
      dni (str): Número de documento del alumno.
      legajo (str): Número de legajo del alumno.
    """
    super().__init__(nombre, apellido, dni)
    self.legajo = legajo
  
  def __repr__(self):
    """
    Devuelve una representación en string del alumno.
    
    Returns:
      str: Representación del alumno.
    """
    return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"