class Persona:
  """
  Clase que representa a una persona.
  
  Attributes:
    nombre (str): Nombre de la persona.
    apellido (str): Apellido de la persona.
    dni (str): Número de documento de la persona.
    pensamientos (int): Contador de pensamientos.
    ultima_idea (str): Último pensamiento de la persona.
  """
  
  def __init__(self, nombre, apellido, dni):
    """
    Inicializa una nueva instancia de Persona.
    
    Args:
      nombre (str): Nombre de la persona.
      apellido (str): Apellido de la persona.
      dni (str): Número de documento de la persona.
    """
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.pensamientos = 0
    self.ultima_idea = "<no penso en nada>"
  
  def __repr__(self):
    """
    Devuelve una representación en string de la persona.
    
    Returns:
      str: Representación de la persona.
    """
    return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    
  def pensar(self, idea):
    """
    Registra un nuevo pensamiento y aumenta el contador.
    
    Args:
      idea (str): El pensamiento o idea a registrar.
    """
    self.pensamientos += 1
    self.ultima_idea = idea