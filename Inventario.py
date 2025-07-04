from Articulo import Articulo
class Inventario():
    inventario: list #la lista de aticulos
    cantidad: int #cantidad total de articulos
    
    #se incializa el inventario y la cantidad
    def __init__(self, inventario, cantidad):
        self.inventario = []
        self.cantidad = 0
        
    #el metodo agrega un nuevo produto al inventario
    #si ya existe articulo con la misma descripcion en el inventario actualiza las copias
    def agregarArticulo(self, articulo_nuevo):
        i = 0
        flag = False
        for articulo in self.inventario:
            i = i + 1
            if articulo.descripcion == articulo_nuevo.descripcion:
                articulo.replicas += articulo_nuevo.replicas  
                self.cantidad += articulo_nuevo.replicas 
                flag = True
        if not flag:
            self.inventario.append(articulo_nuevo)
            self.cantidad += articulo_nuevo.replicas
                
    #elimina el articulo si no se encuentra o se intenta eliminar mas de lo que se tiene 
    # se informa por mensaje
    def eliminarArticulo(self, articuloAEliminar, unidadesEliminadas):
        cantidad = 0
        for articulo in self.inventario:
            i = i + 1
            if articuloAEliminar == articulo:
                if articulo.replicas >= articuloAEliminar.replicas:
                    articulo.replicas -= unidadesEliminadas
                    self.cantidad -= unidadesEliminadas
                    print(f"se elimino correctamente, quedan {cantidad} unidades")
                else:
                    print("se intenta eliminar mas de lo que hay")
            print("no se encontro el articulo")