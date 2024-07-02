from cliente import Cliente

# Diccionario para almacenar los usuarios registrados
usuarios = {}

# Función para registrar un usuario
def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if usuario in usuarios:
        print("El nombre de usuario ya está registrado. Pruebe con otro.")
    else:
        usuarios[usuario] = contraseña
        print("Usuario registrado exitosamente.")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    if usuarios:
        print("Usuarios registrados:")
        for usuario, contraseña in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")
    else:
        print("No hay usuarios registrados.")

# Función para el login de usuarios
def login_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False

# Función para manejar clientes
def manejar_clientes():
    clientes = {}

    def registrar_cliente():
        nombre = input("Ingrese el nombre del cliente: ")
        correo = input("Ingrese el correo del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        cliente = Cliente(nombre, correo, telefono, direccion)
        clientes[nombre] = cliente
        print("Cliente registrado exitosamente.")
    
    def mostrar_clientes():
        if clientes:
            print("Clientes registrados:")
            for cliente in clientes.values():
                print(cliente)
        else:
            print("No hay clientes registrados.")
    
    def actualizar_direccion_cliente():
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre in clientes:
            nueva_direccion = input("Ingrese la nueva dirección: ")
            clientes[nombre].actualizar_direccion(nueva_direccion)
            print("Dirección actualizada exitosamente.")
        else:
            print("Cliente no encontrado.")

    def menu_clientes():
        while True:
            print("\nSeleccione una opción:")
            print("1. Registrar cliente")
            print("2. Mostrar clientes")
            print("3. Actualizar dirección de cliente")
            print("4. Volver al menú principal")

            opcion = input("Opción: ")

            if opcion == "1":
                registrar_cliente()
            elif opcion == "2":
                mostrar_clientes()
            elif opcion == "3":
                actualizar_direccion_cliente()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    
    menu_clientes()

# Menú principal
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Login de usuario")
        print("4. Manejar clientes")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            if login_usuario():
                manejar_clientes()
        elif opcion == "4":
            manejar_clientes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()