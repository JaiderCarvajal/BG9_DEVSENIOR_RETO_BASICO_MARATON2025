
# Lista de productos predefinidos con cantidad disponible
productos = [
    {"nombre": "Camiseta", "precio": 20.0, "cantidad_disponible": 10},
    {"nombre": "Pantalón", "precio": 40.0, "cantidad_disponible": 5},
    {"nombre": "Zapatos", "precio": 50.0, "cantidad_disponible": 8},
    {"nombre": "Sombrero", "precio": 15.0, "cantidad_disponible": 15},
    {"nombre": "Bufanda", "precio": 10.0, "cantidad_disponible": 20},
]



def mostrar_productos():
    print("Productos disponibles:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad disponible: {producto['cantidad_disponible']}")

# Carrito de compras para almacenar los productos
carrito = []
# Función para agregar un producto al carrito
def agregar_producto():
    while True:
        mostrar_productos()
        try:
            # Validar selección del producto
            seleccion = input("Seleccione el número del producto que desea agregar (o 'q' para salir): ")
            if seleccion.lower() == 'q':  # Permitir salir del proceso
                print("Volviendo al menú principal...")
                return
            
            seleccion = int(seleccion) - 1  # Convertir a índice
            if 0 <= seleccion < len(productos):
                producto = productos[seleccion]
                
                # Validar cantidad
                while True:
                    try:
                        cantidad = input(f"Ingrese la cantidad (máximo {producto['cantidad_disponible']}, o 'q' para salir): ")
                        if cantidad.lower() == 'q':  # Permitir salir del proceso
                            print("Volviendo a la selección de productos...")
                            break
                        
                        cantidad = int(cantidad)  # Convertir a entero
                        if cantidad > 0 and cantidad <= producto["cantidad_disponible"]:
                            # Verificar si el producto ya está en el carrito
                            encontrado = False
                            for item in carrito:
                                if item["nombre"] == producto["nombre"]:
                                    item["cantidad"] += cantidad
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                item = {
                                    "nombre": producto["nombre"],
                                    "cantidad": cantidad,
                                    "precio": producto["precio"]
                                }
                                carrito.append(item)
                            
                            # Actualizar la cantidad disponible
                            producto["cantidad_disponible"] -= cantidad
                            print(f"Producto '{producto['nombre']}' agregado al carrito.")
                            
                            # Preguntar si desea agregar otro producto
                            continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
                            if continuar != 's':
                                return  # Salir de la función si no desea agregar más productos
                            break  # Salir del bucle de cantidad para seleccionar otro producto
                        else:
                            print("Error: La cantidad no es válida o supera el stock disponible.")
                    except ValueError:
                        print("Error: Ingrese un número entero válido.")
            else:
                print("Error: Selección no válida. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

# Función para calcular el subtotal, descuentos y total
def calcular_total():
    subtotal = sum(item["cantidad"] * item["precio"] for item in carrito)
    descuentos = 0
    
    # Descuento por cantidad total de productos
    total_productos = sum(item["cantidad"] for item in carrito)
    if total_productos > 10:
        descuento_cantidad = subtotal * 0.10  # 10% de descuento
        descuentos += descuento_cantidad
        print(f"Descuento por cantidad de productos (10%): -${descuento_cantidad:.2f}")
    
    # Descuento por subtotal
    if subtotal > 100:
        descuento_subtotal = subtotal * 0.05  # 5% de descuento
        descuentos += descuento_subtotal
        print(f"Descuento por subtotal mayor a $100 (5%): -${descuento_subtotal:.2f}")
    
    # Descuento especial por cantidad de un mismo producto
    for item in carrito:
        if item["cantidad"] > 5:
            descuento_especial = item["cantidad"] * item["precio"] * 0.15  # 15% de descuento
            descuentos += descuento_especial
            print(f"Descuento especial por más de 5 unidades de '{item['nombre']}' (15%): -${descuento_especial:.2f}")
    
    total = subtotal - descuentos

    print("\nRESUMEN DE COMPRA")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total descuentos: -${descuentos:.2f}")
    print(f"Total a pagar: ${total:.2f}\n")
    
    return subtotal, descuentos, total

# Función para mostrar el carrito
def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("\n--- Carrito de Compras ---")
        for item in carrito:
            print(f"Producto: {item['nombre']}, Cantidad: {item['cantidad']}, Precio Unitario: ${item['precio']:.2f}")
        
        subtotal, descuentos, total = calcular_total()
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Descuentos aplicados: ${descuentos:.2f}")
        print(f"Total a Pagar: ${total:.2f}")
def eliminar_producto():
    while True:
        mostrar_carrito()
        try:
            # Validar selección del producto
            seleccion = input("Seleccione el número del producto que desea eliminar (o 'q' para salir): ")
            if seleccion.lower() == 'q':  # Permitir salir del proceso
                print("Volviendo al menú principal...")
                return
            
            seleccion = int(seleccion) - 1  # Convertir a índice
            if 0 <= seleccion < len(carrito):
                producto = carrito[seleccion]
                carrito.pop(seleccion)
                print(f"Producto '{producto['nombre']}' eliminado del carrito.")
            else:
                print("Error: Selección no válida. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

# Función para generar e imprimir la factura
def imprimir_factura():
    if not carrito:
        print("El carrito está vacío. No hay factura para generar.")
        return
    
    print("\n--- Factura de Compra ---")
    print("Detalle de la compra:")
    for item in carrito:
        print(f"Producto: {item['nombre']}, Cantidad: {item['cantidad']}, Precio Unitario: ${item['precio']:.2f}, Total: ${item['cantidad'] * item['precio']:.2f}")
    
    subtotal, descuentos, total = calcular_total()
    print("\nResumen de la factura:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuentos aplicados: ${descuentos:.2f}")
    print(f"Total a Pagar: ${total:.2f}")
    print("\n¡Gracias por su compra!")

#Menu interactivo
def menu():
    while True:
        print("\n Menu Mercado Inteligente")
        print("1. Agregar producto al carrito.")
        print("2. Ver carrito.")
        print("3. Eliminar producto del carrito.")
        print("4. Total a pagar.")
        print("5. Finalizar compra.")
        print("6. Salir.")

        opcion = input("Seleccione la opcion: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_carrito()
           
        elif opcion == "3":
            eliminar_producto()
            
        elif opcion == "4":
            calcular_total()
            
        elif opcion == "5":
            imprimir_factura()
            carrito.clear()  # Vaciar el carrito después de finalizar la compra
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida.")
menu()