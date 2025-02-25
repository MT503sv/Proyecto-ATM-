class Cuenta: #class sirve para organizar mejor el código y hacer que cada cuenta bancaria funcione como un objeto independiente, con sus propios datos y funciones.
    
    #Representa una cuenta bancaria con funcionalidades básicas como consultar saldo, retirar, depositar y transferir dinero.

    def __init__(self, usuario, pin, saldo=0):#__init__No recibe parámetros adicionales, solo self (referencia a la instancia).
        self.usuario = usuario
        self.pin = str(pin)  # Asegurar que el PIN se almacene como string
        self.saldo = saldo
        self.intentos_fallidos = 0  # Contador de intentos de PIN fallidos
        self.bloqueada = False  # Indica si la cuenta está bloqueada

    def consultar_saldo(self):
        #Devuelve el saldo actual de la cuenta.
        return self.saldo

    def retirar_dinero(self, cantidad):
        #Permite retirar dinero de la cuenta si hay saldo suficiente.
        if cantidad > self.saldo:
            print("Fondos insuficientes.") # Mensaje si no hay saldo suficiente
        elif cantidad <= 0:
            print("Ingrese una cantidad válida.")    # Evita retirar valores inválidos
        else:
            self.saldo -= cantidad # Resta la cantidad del saldo
            print(f"Has retirado {cantidad}. Nuevo saldo: {self.saldo}")

    def depositar_dinero(self, cantidad):
        #Permite depositar dinero en la cuenta.
        if cantidad <= 0:
            print("Ingrese una cantidad válida.")
        else:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Nuevo saldo: {self.saldo}")

    def transferir_dinero(self, cantidad, cuenta_destino):
        #Permite transferir dinero a otra cuenta si hay saldo suficiente.
        if self.usuario == cuenta_destino.usuario:
            print("No puedes transferirte dinero a ti mismo.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para la transferencia.")
        elif cantidad <= 0:
            print("Ingrese una cantidad válida.")
        else:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print(f"Has transferido {cantidad} a {cuenta_destino.usuario}. Nuevo saldo: {self.saldo}")

    def verificar_pin(self, pin_ingresado):
        #Verifica si el PIN ingresado es correcto y maneja intentos fallidos.
        if self.bloqueada:
            print("La cuenta está bloqueada.")
            return False
        if self.pin == str(pin_ingresado):  # Comparar como string
            self.intentos_fallidos = 0  # Reiniciar intentos fallidos
            return True
        else:
            self.intentos_fallidos += 1
            print(f"PIN incorrecto. Intentos restantes: {3 - self.intentos_fallidos}")
            if self.intentos_fallidos >= 3:
                self.bloqueada = True
                print("Tu cuenta ha sido bloqueada debido a intentos fallidos.")
            return False


class Cajero:
    #Simula un cajero automático con múltiples cuentas.
    def __init__(self):
        self.cuentas = {}  # Diccionario para almacenar cuentas

    def crear_cuenta(self, usuario, pin):
        #Crea una nueva cuenta si el usuario no existe.
        if usuario not in self.cuentas:
            self.cuentas[usuario] = Cuenta(usuario, pin)
            print(f"Cuenta creada para {usuario}.")
        else:
            print(f"Ya existe una cuenta para el usuario {usuario}.")

    def iniciar_sesion(self, usuario):
        #Permite al usuario iniciar sesión ingresando el PIN correctamente.
        cuenta = self.cuentas.get(usuario)
        if not cuenta:
            print("Usuario no encontrado.")
            return None
        if cuenta.bloqueada:
            print(f"La cuenta de {usuario} está bloqueada.")
            return None
        
        for _ in range(3):  # Permite hasta 3 intentos
            pin_ingresado = input(f"Ingrese el PIN para {usuario}: ")
            if cuenta.verificar_pin(pin_ingresado):
                print("PIN correcto. Bienvenido.")
                return cuenta
        return None


def menu():
    #Muestra el menú de opciones del cajero automático.
    print("\n*** Menú del Cajero Automático ***")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Transferir dinero")
    print("5. Salir")


def ejecutar_cajero():
    #Ejecuta el flujo principal del cajero automático.
    cajero = Cajero()
    
    # Crear cuentas de prueba
    cajero.crear_cuenta("usuario1", "1234")
    cajero.crear_cuenta("usuario2", "5678")
    cajero.crear_cuenta("usuario3", "7974")

    usuario = input("Ingrese su nombre de usuario: ")
    cuenta = cajero.iniciar_sesion(usuario)
    
    if cuenta:
        while True:
            menu()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print(f"Tu saldo es: {cuenta.consultar_saldo()}")
            elif opcion == "2":
                try:
                    cantidad = float(input("¿Cuánto dinero desea retirar? "))
                    cuenta.retirar_dinero(cantidad)
                except ValueError:
                    print("Error: Ingrese un número válido.")
            elif opcion == "3":
                try:
                    cantidad = float(input("¿Cuánto dinero desea depositar? "))
                    cuenta.depositar_dinero(cantidad)
                except ValueError:
                    print("Error: Ingrese un número válido.")
            elif opcion == "4":
                destino = input("Ingrese el usuario de destino: ")
                cuenta_destino = cajero.cuentas.get(destino)
                if cuenta_destino:
                    try:
                        cantidad = float(input("¿Cuánto dinero desea transferir? ")) #input() devuelve una cadena de texto (string).float() convierte esa cadena en un número decimal.Esto permite manejar cantidades con decimales (ej. 50.75 en lugar de solo 50).
                        cuenta.transferir_dinero(cantidad, cuenta_destino)
                    except ValueError: #ValueError es un tipo de error en Python que ocurre cuando se pasa un valor incorrecto a una función o método que espera un tipo de dato específico.
                        print("Error: Ingrese un número válido.")
                else:
                    print("Usuario destino no encontrado.")
            elif opcion == "5":
                print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción no válida.")
    else:
        print("No se pudo iniciar sesión. Saliendo...")


if __name__ == "__main__":
    ejecutar_cajero()