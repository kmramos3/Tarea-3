class Estudiante: 
  
  def __init__(self): # Método Constructor
    print("Bienvenido al Software de estudiantes")
    

  def solicitudDatos(self): 
    global nombre
    nombre = input("Ingrese su nombre: ")
    global facultad
    facultad = input("Ingrese a que facultad quiere pertenecer: ")
    global edad
    edad = int(input("Ingrese su edad: "))
    
    self._analisisEdad()
    
    
  def _analisisEdad(self):
    
    if (edad >= 18):
      print("\nEste usuario cuenta con la edad necesaria para estudiar...")
      print(f"Bienvenido a la Fac. de {facultad}, {nombre}")
      
    if (edad < 18): 
      print("\nNo cuenta con la edad necesaria para ingresar a una facultad...")
      print("Esfuérzate al máximo y saca lo mejor de tu potencial en el estudio, eres muy joven.")
      print("\n\n           -- Aprovecha tu vida al máximo -- \n\n")
 

if __name__ == '__main__':
  estudiante = Estudiante()
  estudiante.solicitudDatos()