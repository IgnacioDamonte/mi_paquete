class Cliente:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

# Código de prueba
if __name__ == "__main__":
    cliente1 = Cliente("Juan Pérez", "juan.perez@example.com", "Calle Falsa 123", "123456789")
    print(cliente1)
    cliente1.actualizar_direccion("Avenida Siempre Viva 742")
    cliente1.actualizar_telefono("987654321")
    print(cliente1)
