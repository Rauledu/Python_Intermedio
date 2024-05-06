class Persona:
    nombre =""
    apellido = ""
    edad= ""
    nrotelefono = ""
    ID =""
    Sexo =""
    
    
    def __init__(self, nombrex, apellidos, nID ): #Constructor#
        self.nombre = nombrex
        self.apellido = apellidos
        self.ID = nID
    
    def saludar (self):
        saludo = "Hola, mi nombre es: " + self.nombre
        return saludo
    

p1 = Persona("Raul","Luna Diaz","20616230")
print(p1.saludar())
