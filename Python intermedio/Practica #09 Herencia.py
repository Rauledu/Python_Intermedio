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
    
class planilla(Persona):
    salario = 15000
    moneda = "USD"

    def misalario(self):
        msj = "mi salario es de: " + str(self.salario)
        return msj


p2 = planilla("Raul","Luna Diaz","20616230")
print(p2.saludar())
print(p2.misalario())

