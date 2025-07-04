class Articulo():
    descripcion: str #descripcion del articulo
    precio: int #el precio del articulo 
    ID: int #el identificador del articulo  
    #replicas: int
    def __init__(self, descripcion, precio, ID):
        self.descripcion = descripcion
        self.precio = precio
        self.ID = ID

algo = Articulo("tele", 20, 33)
print(algo.descripcion)

