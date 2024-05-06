try:
    print(20/0)
except TypeError as e :
    print("Error en el sistema - tipo: ",e)
except ZeroDivisionError as ex :
    print("Error en el sistema - Division: ",ex)
finally:
    print("Practica terminada")