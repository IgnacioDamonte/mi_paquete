from cliente import Cliente

def main():
   
    cliente1 = Cliente("Juan Perez", "juan.perez@example.com", "123456789", "Calle Falsa 123")
    
    
    print(cliente1)
    
   
    cliente1.actualizar_direccion("Avenida Siempreviva 742")
    
 
    print(cliente1)
    
 
    print(cliente1.mensaje_bienvenida())

if __name__ == "__main__":
    main()