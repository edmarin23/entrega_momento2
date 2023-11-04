# Para crear una clase en Python, usamos la palabra reservada class
class Persona:
   # Ahora vamos a crear un método constructor
   def __init__(self, id, nombre, apellido, correo, password):
       # Este contiene la palabra reservada self,
       # similar a 'this' en Java, por ejemplo:
       self._id = id
       self._nombre = nombre
       self._apellido = apellido
       self._correo = correo
       self._password = password


   # ------- ENCAPSULAMIENTO CON PYTHON -----------


   # se usa un guion bajo al principio de la variable para indicar que será encapsulada


   # Ahora usaremos decoradores para crear los getters and setters


   # @property => indica los getters
   # @<atributo>.setter => Indica los setters


   # Esto es un SET = setter
   @property
   def id(self):
       return self._id


   @id.setter
   def id(self, id):
       self._id = id


   # Esto es un GET = getter
   @property
   def nombre(self):
       return self._nombre


   @nombre.setter
   def nombre(self, nombre):
       self._nombre = nombre


   @property
   def apellido(self):
       return self._apellido


   @apellido.setter
   def apellido(self, apellido):
       self._apellido = apellido


   @property
   def correo(self):
       return self._correo


   @correo.setter
   def correo(self, correo):
       self._correo = correo


   @property
   def password(self):
       return self._password


   @password.setter
   def password(self, password):
       self._password = password


   # Vamos a generar los métodos para registrar los usuarios e imprimir el registro


   def registrar_usuario(self):
       self._id = input(f"Ingrese el id del usuario: ")
       self._nombre = input(f"Ingrese el nombre del usuario: ")
       self._apellido = input(f"Ingrese el apellido del usuario: ")
       self._correo = input(f"Ingrese el correo del usuario: ")
       self._password = input(f"Ingrese la contraseña del usuario: ")


   def imprimir_registro(self):
       print(f"id: {self.id} Nombre: {self.nombre} Apellido: {self.apellido} Correo: {self.correo} Contraseña: {self.password}")


