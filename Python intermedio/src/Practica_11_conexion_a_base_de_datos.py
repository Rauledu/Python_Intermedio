#----------------------------------------{{Practica 11}}--------------------------------------------------------#
import pyodbc


try:
    connection = pyodbc.connect('DRIVER={SQL server};SERVER=RAUL;DATABASE=Inventario;Trusted_Connection=yes;')
    
    #-----------------------------------{{Practica 12}}----------------------------------------------------------#
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
   
    #--------------------------------------------{{practica #13}}----------------------------------------------#
    # cursor_insert = connection.cursor()
    # cursor_insert.execute(''' SET IDENTITY_INSERT Products OFF INSERT INTO Products(Name, Model) 
    #                       values 
    #                       ('samsung', 'Galaxy Flip 6')''')

    # connection.commit()
    # print("Registro insertado con exito")
    
    #Parte de esta practica se utilizo el set identity_insert para Permite insertar valores explícitos en la columna de identidad de una tabla.#
    
    #---------------------------------------------{{Practica 14}}-------------------------------------------#
    
    # cursor_update = connection.cursor()
    # cursor_update.execute("Update Products set Model = 'Galaxy_A35' where ID = 12")
    
    # connection.commit()
    # print("El registro se ha actualizado.")
    
    #----------------------------------------------{{Practica 15}}------------------------------------------#
    
    # cursor_eliminar = connection.cursor()
    # cursor_eliminar.execute("delete from Products where ID = 12")
    
    # connection.commit()
    # print("El registro se ha eliminado.")
    
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
   
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")

