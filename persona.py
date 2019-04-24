class Persona:
    nombre = None
    edad = None
    def __init__(self,el_nombre,la_edad):
        self.nombre=el_nombre
        self.edad = la_edad
        print("Hola me llamo",self.nombre,"tengo",self.edad)

    def get_edad(self):
        return self.edad
    
    def set_edad(self, cantidad):
        self.edad=cantidad
        
name = Persona("Mathias",20)
