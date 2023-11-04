from Persona import Persona
from Empleado import Empleado

clientes_registrados = []
empleados_registrados = []

class Empleado(Empleado):
    def calcular_salario_neto(self):
        salud_pension = 0.08  # Descuento por salud y pensión (8%)
        descuento = self.salario * salud_pension  # Calcular el descuento
        salario_neto = self.salario - descuento  # Restar el descuento al salario base

        if self.salario <= 2320000:  # Si el salario es menor o igual a 2,320,000
            salario_neto += 140000  # Se suma el auxilio de transporte

        return salario_neto

    def iniciar_sesion(self, id_usuario, contrasena):
        if self._id == id_usuario and self._password == contrasena:
            return True
        return False

class Persona(Persona):
    def iniciar_sesion(self, id_usuario, contrasena):
        if self._id == id_usuario and self._password == contrasena:
            return True
        return False

def iniciar_sesion_empleado(empleados_registrados):
    id_emp = input("Ingrese el ID del empleado: ")
    contrasena_emp = input("Ingrese la contraseña del empleado: ")

    for empleado in empleados_registrados:
        if empleado.iniciar_sesion(id_emp, contrasena_emp):
            print("Has iniciado sesión como empleado.")
            return
    print("Inicio de sesión incorrecto como empleado.")

def iniciar_sesion_cliente(clientes_registrados):
    id_cliente = input("Ingrese el ID del cliente: ")
    contrasena_cliente = input("Ingrese la contraseña del cliente: ")

    for cliente in clientes_registrados:
        if cliente.iniciar_sesion(id_cliente, contrasena_cliente):
            print("Has iniciado sesión como cliente.")
            return
    print("Inicio de sesión incorrecto como cliente.")

def menuApp():
    print("Inicialice con 1")
    init = int(input("Escriba 1"))

    while init != 0:
        print("Seleccione 1 para registrar cliente\n",
              "Seleccione 2 para registrar empleado\n",
              "Seleccione 3 para iniciar sesión como empleado\n",
              "Seleccione 4 para iniciar sesión como cliente\n",
              "Seleccione 5 para ver registros\n",
              "Seleccione 6 para calcular salario neto\n",
              "Seleccione 7 para salir")

        opc = int(input("Ingrese una opción: "))

        if opc == 1:
            cliente = Persona(id=None, nombre=None, apellido=None, correo=None, password=None)
            cliente.registrar_usuario()
            clientes_registrados.append(cliente)
        elif opc == 2:
            empleado = Empleado(id=None, nombre=None, apellido=None, correo=None, password=None, cargo=None, salario=None, tipo_contrato=None)
            empleado.registrar_usuario()
            empleados_registrados.append(empleado)
        elif opc == 3:
            if empleados_registrados:
                iniciar_sesion_empleado(empleados_registrados)
            else:
                print("No hay empleados registrados para iniciar sesión.")
        elif opc == 4:
            if clientes_registrados:
                iniciar_sesion_cliente(clientes_registrados)
            else:
                print("No hay clientes registrados para iniciar sesión.")
        elif opc == 5:
            print("Registros de clientes:")
            for cliente in clientes_registrados:
                print(cliente.__dict__)
            print("\nRegistros de empleados:")
            for empleado in empleados_registrados:
                print(empleado.__dict__)
        elif opc == 6:
            if empleados_registrados:
                print("Calcular salario neto de empleados:")
                for empleado in empleados_registrados:
                    salario_neto = empleado.calcular_salario_neto()
                    print(f"Salario neto de {empleado.nombre}: {salario_neto}")
            else:
                print("No hay empleados registrados para calcular el salario neto.")
        elif opc == 7:
            print("Saliendo...")
            break

# Llamar a la función menuApp para iniciar el programa
menuApp()


