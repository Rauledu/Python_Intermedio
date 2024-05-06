
# connection = pyodbc.connect('DRIVER={SQL server};SERVER=RAUL;DATABASE=Inventario;Trusted_Connection=yes;')
    
#     cursor = connection.cursor()
#     # cursor.execute("SELECT @@version;")
#     # row = cursor.fetchone()
#     # print("Versión del servidor de SQL Server: {}".format(row))
#     cursor.execute("SELECT * FROM Products;")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
# except Exception as ex:
#     print("Error durante la conexión: {}".format(ex))
# finally:
#     connection.close()  # Se cerró la conexión a la BD.
#     print("La conexión ha finalizado.")

#Esta practica va anclada a la practica nro 11 por la conexion a la base de datos.#
