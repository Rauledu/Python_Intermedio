import pyodbc

connection = pyodbc.connect('DRIVER={SQL server};SERVER=RAUL;DATABASE=Inventario;Trusted_Connection=yes;')
    
    #-----------------------------------{{Practica 12}}----------------------------------------------------------#
def consulta(connection):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Products;")
        
        product = cursor.fetchall()
       
        return product


def OperacionMath(num1, num2=10, num3=20):
    resultado = num1 * num2 * num3
    return resultado

