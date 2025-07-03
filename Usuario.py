class Usuario():
    #los atributos
    nombre: str # nombre del usuario
    apellido: str # apellido del usuario
    DNI: int # el DNI del usuario  
    #EL constructor de la clase, inicializa los atributos
    def __init__(nombre, apellido, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
    def MostarDatos(self):
        print(f"El nombre del cliente {self.nombre} {self.apellido}")  
Usuarionuevo = Usuario
Usuarionuevo.apellido = "Cardozo"
Usuarionuevo.nombre = "Joaquin"
Usuarionuevo.MostarDatos(Usuarionuevo)