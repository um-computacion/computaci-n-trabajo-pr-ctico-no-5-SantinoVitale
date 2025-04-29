class Persona:
    """Clase base que representa a una persona en el sistema educativo.
    
    Attributes:
        nombre (str): Nombre de la persona.
        apellido (str): Apellido de la persona.
        dni (str): Número de DNI de la persona.
        pensamientos (int): Contador de pensamientos realizados.
        ultima_idea (str): Último pensamiento registrado.
    """
    
    def __init__(self, nombre, apellido, dni):
        """Inicializa una nueva instancia de Persona.
        
        Args:
            nombre (str): Nombre de la persona.
            apellido (str): Apellido de la persona.
            dni (str): Número de DNI de la persona.
            
        Raises:
            ValueError: Si el nombre o apellido están vacíos.
            ValueError: Si el DNI no contiene solo dígitos.
            ValueError: Si el DNI no tiene la longitud correcta.
        """
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not apellido:
            raise ValueError("El apellido no puede estar vacío")
        if not dni.isdigit():
            raise ValueError("El DNI debe contener solo números")
        if len(dni) < 7 or len(dni) > 8:
            raise ValueError("El DNI debe tener entre 7 y 8 dígitos")
        
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"
    
    def __repr__(self):
        """Representación en cadena de la persona.
        
        Returns:
            str: Representación textual de la persona.
        """
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    
    def pensar(self, idea):
        """Registra un nuevo pensamiento de la persona.
        
        Args:
            idea (str): El contenido del pensamiento.
        """
        self.pensamientos += 1
        self.ultima_idea = idea