class Persona:
    nombre =""
    apellido = ""
    edad= ""
    nrotelefono = ""
    ID =""
    Sexo =""
    
    def saludar (self):
        saludo = "Hola, mi nombre es: " + self.nombre
        return saludo
    

p1 = Persona()
print(p1.saludar())
