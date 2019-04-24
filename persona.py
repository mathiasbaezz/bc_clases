class Persona:
    nombre = None
    def __init__(self,el_nombre):
        self.nombre=el_nombre
        print("Hola me llamo",self.nombre)
name = Persona("Maa")
