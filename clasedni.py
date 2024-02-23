class persona:
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def __str__(self):
        return f"""Nombre : {self.nombre},
        edad : {self.edad}, 
        DNI : {self.dni}"""
    
class documento:
        def __init__(self) :
             self.personas= []

        def AgregarDatos(self,personas):
             self.personas.append(personas)

        def mostrar(self):
             for persona in self.personas:
                  print(persona)
        
