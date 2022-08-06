class autoMovil: 
  def __init__(self):
    print("Bienvenido a AutoCom")
  
  def consultaVehiculo(self):
    print("1.- Comprar Carro")
    print("2.- Vender vehículo")
    print("3.- Cotizar vehículo")
    op = int(input("Ingrese la opción que desee: "))
    
    if (op == 1):
      print("\n Opción de comprar automóvil\n")
      carro = input("Que carro desea adquirir: ")
      puertas = input("Cuantas puertas desea que tenga: ")
      color = input("Que color lo desea: ")
      
      print("\n\nMuchas gracias por ingresar los datos, sus datos son los siguentes: \n\n")
      print(f"Carro: {carro}")
      print(f"Puertas: {puertas}")
      print(f"Color: {color}")
      
      print("\n Enviaremos los datos al correo que nos proporcionara.")
      correo = input("Por favor ingrese el correo de contacto: ")
      print(f"Correo {correo}, registrado correctamente.")
      
    if (op == 2):
      print("\nOpción de vender vehículo\n")
      marca = input("Ingrese la marca de su vehículo: ")
      modelo = int(input("Ingrese el modelo del vehículo a vender: "))
      color1 = input("Color del vehículo: ")
      precioVenta = int(input("Ingrese el precio en el que lo quiere vender: "))
      
      print("\n\nGracias, datos ingresados correctamente: ")
      print(f"Marca: {marca}")
      print(f"Modelo: {modelo}")
      print(f"Color: {color1}")
      print(f"Precio de Venta: {precioVenta}")
  
      
    if (op == 3): 
      print("Opción en construcción")
    
if __name__ == '__main__':
  predio = autoMovil()
  predio.consultaVehiculo()